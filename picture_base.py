from PIL import Image, ImageTk
import config
import os

# Load the image 49*22
def load_image(num,model):
    if config.PATH is None:
        raise ValueError("config.PATH is not set")
    image_path = os.path.join(config.PATH, "pic")
    file_mapping = {
        0: "colored.png",
        1: "colored-transparent.png",
        2: "monochrome.png",
        3: "monochrome-transparent.png"
    }
    if model not in file_mapping:
        raise ValueError(f"Invalid model value: {model}")

    file = file_mapping[model]
    col=num%49
    row=num//49
    image = Image.open(image_path+'/'+file)
    icon_width = 16
    icon_height = 16
    left = col * (icon_width+1)
    top = row * (icon_height+1)
    right = left + icon_width
    bottom = top + icon_height
    icon = image.crop((left, top, right, bottom))
    return icon

def map_synthesis(array):
    result_width = len(array[0]) * 16
    result_height = len(array)  * 16
    result_image = Image.new('RGBA', (result_width, result_height), (0, 0, 0, 0))
    for row in range(len(array)):
        for col in range(len(array[row])):
            num = array[row][col]
            if num is not None:
                icon_image = load_image(num,1)
                if icon_image:
                    result_image.paste(icon_image, (col * 16, row * 16, (col + 1) * 16, (row + 1) * 16))
    return ImageTk.PhotoImage(result_image)