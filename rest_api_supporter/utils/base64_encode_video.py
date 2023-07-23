import io
import base64
from PIL import Image
import numpy as np
import random
import soundfile as sf
import os

def base64_encode_video(video):
    if isinstance(video, bytes):
        base64_encoded = base64.b64encode(video)
        base64_encoded = base64_encoded.decode("utf-8") 
        return "data:video/mp4;base64,"+base64_encoded
    elif isinstance(video, np.array):
        bytes_value = video.tobytes()
        base64_encoded = base64.b64encode(bytes_value)
        base64_encoded = base64_encoded.decode("utf-8") 
        return "data:video/mp4;base64,"+base64_encoded
