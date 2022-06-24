import warnings
import librosa as lr
import numpy as np

sample_rate = 8000
image_width = 500
image_height = 256

# Convert wav file to spectrogram
def audio_to_spectrogram(path: str):
    warnings.filterwarnings("ignore") # suppress librosa warnings
    audio, _ = lr.load(path, sr=sample_rate)
    if (n_four := len(audio) / 32000) < 1:
        print("Hard to predict a file with less than 4seconds.")
        extended_audio = np.concatenate(
            (
                audio,
                np.zeros(32000 - len(audio))
            )
        )
        yield np.expand_dims(spectrogram(extended_audio), axis=2)
    else:
        for i in range(0, int(n_four)):
            start = i*32000
            end = (i+1)*32000
            yield np.expand_dims(spectrogram(audio[start:end]), axis=2)

# Spectrogram
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