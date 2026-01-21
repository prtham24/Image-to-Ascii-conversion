from PIL import Image
from tkinter import Tk, filedialog
A="@%#*+=-:. "


def image_to_ascii(image_path,width):
    try:
        image=Image.open(image_path)
    except Exception as e:
        print("Cannot open image",e)
        return
    image=resize(image,width)
    image=grayscale(image)
    ascii_str=pixels_to_image(image)
    width_size=image.width
    ascii_img=""
    for i in range(0,len(ascii_str),ascii_)


image_to_ascii(file_path,width=120)