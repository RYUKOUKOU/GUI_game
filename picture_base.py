from PIL import Image
import config
import os

# Load the image 49*22
def load_image(num):
    if config.PATH is None:
        raise ValueError("config.PATH is not set")
    image_path = os.path.join(config.PATH, "pic")
    coloed="colored.png"
    coloed_tran="colored-transparent.png"

    col=num%49
    row=num//49
    image = Image.open(image_path+'/'+coloed_tran)
    icon_width = 16
    icon_height = 16
    left = col * (icon_width+1)
    top = row * (icon_height+1)
    right = left + icon_width
    bottom = top + icon_height
    icon = image.crop((left, top, right, bottom))
    return icon
