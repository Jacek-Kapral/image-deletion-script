import os
from PIL import Image

directory = "/path-to-images/"

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        image = Image.open(os.path.join(directory, filename))
        width, height = image.size
        
        if width < 1920 or height < 1080:
            os.remove(os.path.join(directory, filename))