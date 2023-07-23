import io
import base64
from PIL import Image
import numpy as np
import random
import soundfile as sf
import os

def base64_encode_image(image):
    if isinstance(image, Image.Image): #이미지
        #'''
        bytes_io = io.BytesIO()
        image_format = image.format
        if not image_format:
            image_format = "PNG"
        image.save(bytes_io, image_format)
        bytes_value = bytes_io.getvalue()
        #'''
        '''
        file = "image.png"
        try:
            image.save(file)
            with open(file, "rb") as f:
                bytes_value = f.read() #bytes
        finally:
            os.remove(file)
        '''
        base64_encoded = base64.b64encode(bytes_value)
        base64_encoded = base64_encoded.decode("utf-8") 
        #return "data:image/png;base64,"+base64_encoded
        return "data:image/"+image_format.lower()+";base64,"+base64_encoded
    
