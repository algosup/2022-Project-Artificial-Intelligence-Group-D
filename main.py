import numpy as np
import sounddevice as sd
import RPi.GPIO as GPIO
import scipy.signal
import colorama

from typing import Any, Optional
from tflite_runtime.interpreter import Interpreter

from formaterio import *

# Terminal colors
colorama.init()

# Constant Parameters
SAMPLE_RATE = 48000
RE_SAMPLE_RATE = 16000
RECORD_DURATION = 4 # in seconds
NUM_MFCC = 16
MODEL_PATH = "model.tflite"
GREEN_PIN = 8
YELLOW_PIN = 10
RED_PIN = 12

# GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)

# Model initialisation
interpreter = Interpreter(
    model_path=MODEL_PATH,
)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def decimate(
    signal: np.ndarray,
    new_sr: int,
    old_sr: int,
    ) -> Any:

    decimate_factor = old_sr / new_sr

    resampled_signal = scipy.signal.decimate(signal, int(decimate_factor))
    return resampled_signal

def stream_callback(
    indata: np.ndarray,
    frames: int,
    time: Any,
    status: Optional[sd.CallbackFlags],
    ) -> None:

    GPIO.output(YELLOW_PIN, GPIO.HIGH)

    record = decimate(np.squeeze(indata), RE_SAMPLE_RATE, SAMPLE_RATE)

    spectro = np.expand_dims(spectrogram(record), axis=2)

    interpreter.set_tensor(input_details[0]["index"], [spectro])
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]["index"])
    prediction = output_data[0][0]

    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)

    if prediction > 0.5:
        print(f"{colorama.Fore.RED  }French  |{prediction}{colorama.Fore.RESET}")
        GPIO.output(RED_PIN, GPIO.HIGH)
    else:
        print(f"{colorama.Fore.GREEN}English |{prediction}{colorama.Fore.RESET}")
        GPIO.output(GREEN_PIN, GPIO.HIGH)

# doc: https://python-sounddevice.readthedocs.io/en/0.3.12/api.html#sounddevice.InputStream
try:
    with sd.InputStream(
        channels = 1,
        samplerate = SAMPLE_RATE,
        blocksize = int(SAMPLE_RATE * RECORD_DURATION),
        callback = stream_callback
        ):
        while True:
            pass
except KeyboardInterrupt:
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)