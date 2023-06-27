import base64
from PIL import Image
import re

def base64_decode(base64):
    #print(base64) #data:image/jpeg;base64,/9j/4TT...
    if "base64," in base64:
        front = base64.split('base64,')[0]
        encoded = base64.split('base64,')[1]
        decoded = base64.b64decode(encoded)
        if "image" in front:
            image = Image.open(decoded)
            #print(image) #<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=386x262 at 0x1074728F0>
            return image
        elif "audio" in front:
            return decoded
    else:
        image = Image.open(decoded)
        #print(image) #<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=386x262 at 0x1074728F0>
        return image
