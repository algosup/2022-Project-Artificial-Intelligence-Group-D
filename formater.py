import warnings
import librosa as lr
import numpy as np
import imageio

from PIL import Image

sample_rate = 8000
image_width = 500
image_height = 256
batch_size = 64

def load_audio_file(audio_file_path):
    warnings.filterwarnings("ignore")
    audio_segment, _ = lr.load(audio_file_path, sr=sample_rate)
    return audio_segment

def spectrogram(audio_segment):
    # Compute mel-scaled spectrogram image
    hl = audio_segment.shape[0] // image_width
    spec = lr.feature.melspectrogram(audio_segment, n_mels=image_height, hop_length=int(hl))

    # Logarithmic amplitudes
    image = lr.core.power_to_db(spec)

    # Convert to numpy matrix
    image_np = np.asmatrix(image)

    # Normalize and scale
    image_np_scaled_temp = (image_np - np.min(image_np))
    
    image_np_scaled = image_np_scaled_temp / np.max(image_np_scaled_temp)

    return image_np_scaled[:, 0:image_width]

def to_integer(image_float):
    # range (0,1) -> (0,255)
    image_float_255 = image_float * 255.
    
    # Convert to uint8 in range [0:255]
    image_int = image_float_255.astype(np.uint8)
    
    return image_int

def audio_to_image_file(audio_file):
    out_image_file = audio_file + '.png'
    audio = load_audio_file(audio_file)
    if np.count_nonzero(audio) != 0:
        spectro = spectrogram(audio)
        spectro_int = to_integer(spectro)
        imageio.imwrite(out_image_file, spectro_int)
    else:
        print('WARNING! Detected an empty audio signal. Skipping...')

def spectrogram_to_tensor(path):
    im = Image.open(path)
    im.thumbnail((image_width, image_height))

    tensor = np.array(object=im, dtype=np.float32)

    tensor /= 255
    return np.expand_dims(tensor, axis=2)