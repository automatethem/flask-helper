import io
import base64
from PIL import Image
import numpy

'''
image = Image.open("rock.jpg")
base64 = base64_encode(image)
print(base64) #data:image/png;base64,/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             
'''
'''

base64 = base64_encode(audio)
print(base64) #data:audio/wav;base64,UklGRiTuAgBXQVZFZm...At84WACNZGwA=
'''
def base64_encode(image):
    if isinstance(image, Image.Image):
        bytes_io = io.BytesIO()
        image.save(bytes_io, image.format)
        bytes = bytes_io.getvalue()
    elif isinstance(image, numpy.ndarray):
        bytes = image
    base64_encoded = base64.b64encode(bytes)
    base64_encoded = base64_encoded.decode("utf-8") 
    if isinstance(image, Image.Image):
        #return "data:image/png;base64,"+base64_encoded
        return "data:image/"+image.format.lower()+";base64,"+base64_encoded
    elif isinstance(image, numpy.ndarray): 
        return "data:audio/wav;base64,"+base64_encoded
