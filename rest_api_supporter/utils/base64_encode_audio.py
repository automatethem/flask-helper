import io
import base64
from PIL import Image
import numpy as np
import random
import soundfile as sf
import os

def base64_encode_audio(image):
    if isinstance(image, np.ndarray): #오디오
        numpy_array = image
        file = "audio.wav"
        try:
            sf.write(file, numpy_array, samplerate=16000)
            with open(file, "rb") as f:
                bytes_value = f.read() #bytes
        finally:
            os.remove(file)
        base64_encoded = base64.b64encode(bytes_value)
        base64_encoded = base64_encoded.decode("utf-8") 
     
        return "data:audio/wav;base64,"+base64_encoded
