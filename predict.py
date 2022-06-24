import tensorflow as tf
import os

from colorama import init, Fore
from os.path import dirname, abspath, join

from formaterio import *

init() # colorama

root_directory = dirname(abspath(__file__))
model_path = join(root_directory, "model.tflite")

# Load & init tensorflow model
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Print results
def pretty_print(label: str, perc: float, n: int, len: int, avg: float, best: float) -> None:
    print(f"{Fore.LIGHTMAGENTA_EX}{label:<9}{Fore.RESET} | {Fore.LIGHTCYAN_EX}perc: {perc:.3f}%{Fore.RESET} | n: {n}/{len} | avg: {avg:.5f} | best: {best}")

# Predict using tensorflow
def predict(path: str) -> tuple[str, float]:
    tensors = audio_to_spectrogram(path)

    for tensor in tensors:
        tensor_input_index = input_details[0]['index']
        interpreter.set_tensor(tensor_input_index, [tensor])
        interpreter.invoke()

        tensor_output_index = output_details[0]["index"]
        output_data = interpreter.get_tensor(tensor_output_index)

        if (proba := output_data[0][0]) > 0.5:
            yield ("French", proba)
        else:
            yield ("English", proba)

# Logic guessing game
def guess(predictions: list) -> None:
    n_fr, n_en, score_fr, score_en, predict_len = 0, 0, [], [], 0
    for i, (label, probability) in enumerate(predictions, start=1):
        if label == "French":
            n_fr += 1
            score_fr.append(probability)
        else:
            n_en += 1
            score_en.append(probability)
        predict_len = i

    if n_fr > n_en or score_fr > score_en: 
        avg = sum(score_fr) / len(score_fr)
        pretty_print("- French", (avg-0.5)*200, n_fr, predict_len, avg, max(score_fr))
    else:
        avg = sum(score_en) / len(score_en)
        pretty_print("+ English", ((1-avg)-0.5)*200, n_en, predict_len, avg, min(score_en))

###########################
#       !EDIT HERE!       #
###########################
DIRECTORY_PATH = join(root_directory, "wav") # CHANGE THIS VARIABLE TO YOUR DIRECTORY WAV FILES

print(f"{Fore.GREEN}{'> START':<9}{Fore.RESET} | Predicting from {DIRECTORY_PATH}")
for file in os.listdir(DIRECTORY_PATH):
    path = join(DIRECTORY_PATH, file)
    print(f"{Fore.BLUE}{'! PREDICT':<9}{Fore.RESET} | {Fore.MAGENTA}{file}{Fore.RESET}")
    if file.endswith(".wav"):
        guess(predict(path))
    else:
        print(f"{Fore.RED}{path} is not a wav file.{Fore.RESET}")