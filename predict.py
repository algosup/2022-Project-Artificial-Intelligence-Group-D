import tensorflow as tf

from os.path import dirname, abspath, join

from formater import *

root_directory = dirname(abspath(__file__))
model_path = join(root_directory, "model.tflite")

interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict(path: str):
    test_path = f"{root_directory}{path}"

    audio_to_image_file(test_path)
    tensor = spectrogram_to_tensor(f"{test_path}.png")

    tensor_input_index = input_details[0]['index']
    interpreter.set_tensor(tensor_input_index, [tensor])
    interpreter.invoke()

    tensor_output_index = output_details[0]["index"]
    output_data = interpreter.get_tensor(tensor_output_index)

    if (proba := output_data[0][0]) > 0.5:
        print("French", proba)
    else:
        print("English", proba)

predict("/wav/french.wav")
predict("/wav/english.wav")