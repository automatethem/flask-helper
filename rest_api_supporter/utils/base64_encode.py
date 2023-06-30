import io
import base64
from PIL import Image
import numpy
import random
import soundfile as sf
import os

def base64_encode(image):
    if isinstance(image, Image.Image):
        bytes_io = io.BytesIO()
        image_format = image.format
        if not image_format:
            image_format = "PNG"
        image.save(bytes_io, image_format)
        bytes_value = bytes_io.getvalue()
    elif isinstance(image, numpy.ndarray):
        '''
        with open("up.wav", "rb") as f:
            bytes_value = f.read()
        '''
        #'''
        wav_file = f"speech_{random.randint(1, 10000)}.wav"
        try:
            sf.write(wav_file, image, samplerate=16000)
            with open(wav_file, "rb") as f:
                bytes_value = f.read()
        finally:
            os.remove(wav_file)
        #'''
    elif isinstance(image, bytes):
        bytes_value = image
    base64_encoded = base64.b64encode(bytes_value)
    base64_encoded = base64_encoded.decode("utf-8") 
    if isinstance(image, Image.Image):
        #return "data:image/png;base64,"+base64_encoded
        return "data:image/"+image_format.lower()+";base64,"+base64_encoded
    elif isinstance(image, numpy.ndarray) or isinstance(image, bytes): 
        return "data:audio/wav;base64,"+base64_encoded
