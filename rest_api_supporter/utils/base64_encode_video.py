import io
import base64
from PIL import Image
import numpy as np
import random
import soundfile as sf
import os

def base64_encode_video(image):
    if isinstance(image, bytes): #비디오
        bytes_value = image

        base64_encoded = base64.b64encode(bytes_value)
        base64_encoded = base64_encoded.decode("utf-8") 
     
        return "data:video/mp4;base64,"+base64_encoded
