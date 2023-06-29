import io
import base64
from PIL import Image

'''
#image = Image.open("rock.jpg")
#base64 = base64_encode(image)
#print(base64) #/9j/4AAQSkZJRgABAQAAA ... bSjrTEf/9k=
def base64_encode(image):
    bytesIO = io.BytesIO()
    try:
        image.save(bytesIO, "JPEG")
    except:
        image.save(bytesIO, "PNG")
    b64encoded = base64.b64encode(bytesIO.getvalue())
    base64_str = b64encoded.decode("utf-8")
    return base64_str
'''

'''
image = Image.open("rock.jpg")
base64 = base64_encode(image)
print(base64) #data:image/png;base64,/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             
'''
'''

base64 = base64_encode(audio)
print(base64) #data:audio/wav;base64,UklGRiTuAgBXQVZFZm...At84WACNZGwA=
'''
def base64_encode(bytes):
    if isinstance(image, Image):
        bytesIO = io.BytesIO()
        try:
            image.save(bytesIO, "JPEG")
        except:
            image.save(bytesIO, "PNG")
        bytes = bytesIO.getvalue()
    b64encoded = base64.b64encode(bytes)
    base64_str = b64encoded.decode("utf-8")
    if isinstance(image, Image):    
        return "data:image/png;base64,"+base64_str
    else:    
        return "data:audio/wav;base64,"+base64_str
