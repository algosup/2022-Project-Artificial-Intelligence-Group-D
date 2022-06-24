import warnings
import librosa as lr
import numpy as np
import imageio
import io

from PIL import Image

sample_rate = 8000
image_width = 500
image_height = 256

def load_audio_file(path: str):
    warnings.filterwarnings("ignore") # suppress librosa warnings
    audio_segment, _ = lr.load(path, sr=sample_rate)

    return audio_segment

def audio_to_io(path: str):
    audio = load_audio_file(path)
    spectro = spectrogram(audio)
    spectro_int: np.matrix = to_integer(spectro)
    return imageio.imwrite("<bytes>", spectro_int)

def spectrogram(audio_segment):
    # Compute mel-scaled spectrogram image
    hl = audio_segment.shape[0] // image_width
    warnings.filterwarnings("ignore") # suppress librosa warnings
    spec = lr.feature.melspectrogram(audio_segment, n_mels=image_height, hop_length=int(hl))

    # Logarithmic amplitudes
    image = lr.core.power_to_db(spec)

    # Convert to numpy matrix
    image_np = np.asmatrix(image)

    # Normalize and scale
    image_np_scaled_temp = (image_np - np.min(image_np))

    image_np_scaled = image_np_scaled_temp / np.max(image_np_scaled_temp)

    return image_np_scaled[:, 0:image_width]

def to_integer(image_float: np.matrix):
    # range (0,1) -> (0,255)
    image_float_255 = image_float * 255.

    # Convert to uint8 in range [0:255]
    image_int = image_float_255.astype(np.uint8)

    return image_int

def iospectrogram_to_tensor(image_data: bytes):
    im = Image.open(io.BytesIO(image_data))
    im.thumbnail((image_width, image_height))

    tensor = np.array(object=im, dtype=np.float32)

    tensor /= 255
    return np.expand_dims(tensor, axis=2)