# Predict English/French from sound using AI

## Train the AI
You'll find the notebook used to create the model under `/notebook.ipynb`.

Open the notebook using [Google Colab](https://colab.research.google.com/) or [Kaggle](https://www.kaggle.com/) then run all blocks and download the `model.tflite`.

> **Note**:
> 
> The model is a _Binary classification_;
>
> It means in our case, 0 == English, 1 == French

## Predict Language using a Directory of wav files

1. Clone the project on your machine.
2. Create a directory in the project.
> **Note**:
> 
> The default directory name is `wav`, create a directory with this name if you don't want to change the code below
> 
> https://github.com/algosup/2022-Project-Artificial-Intelligence-Group-D/blob/d61e7a4d57c084972b0b6d6a27f6bedb2728d08b/predict.py#L67-L70
3. Put your wav files in the directory.
> **Note**: 
> 
> Non-wav files will not be taken in consideration by the code.
4. Install the `requirements.txt`
> **Note**: 
> 
> You might have tensorflow installed, the requirements.txt will not automaticly install tensorflow
5. Run the `predict.py` with python3.
> **Note**:
> 
> You should have something similar:
>
> ![output-predict.py](https://user-images.githubusercontent.com/71769515/175771701-737fc438-5754-48ae-bbcb-6ac035e05ad5.png)

## Predict Language using a Raspberry Pi

- Install Debian x64 Lite using [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on a Raspberry Pi, then follow [this guide](https://gist.github.com/PaulMarisOUMary/791a572c8635b757aaece37dcc06d325).
- Install all required dependencies for python3 on the Raspberry Pi.
- Using ssh, upload in the same directory: `formaterio.py`, `model.tflite` (or your model), `main.py`
- Run using python3 `main.py` 
> **Note**: (you must have a microphone plugged on your Raspberry Pi)

## Documents

- [Functionnal Specifications](https://github.com/algosup/2022-Project-Artificial-Intelligence-Group-D/blob/main/Documents/Functional_Specification.md)
- [Technical Specifications](https://github.com/algosup/2022-Project-Artificial-Intelligence-Group-D/blob/main/Documents/Technical_Specification.md)
