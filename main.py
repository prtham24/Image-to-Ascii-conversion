from PIL import Image
from tkinter import Tk,filedialog
A="@%#*+=-:. "
def resize(image,new_width=100):
    width,height=image.size
    aspect_ratio=height/width
    new_height=int(new_width*aspect_ratio*0.55)
    return image.resize((new_width,new_height))
def greyscale(img):
    return img.convert("L")
def pixels_to_ascii(img):
    pixels=img.getdata()
    ascii_str=""
    for pixel in pixels:
        ascii_str+=A[pixel*len(A)//256]
    return ascii_str
def image_to_ascii(file_path,width):
    try:
        image = Image.open(file_path)
    except Exception as e:
        print("Cannot open image",e)
        return
    img = Image.open(file_path)
    img=resize(img,width)
    img = greyscale(img)
    ascii_str=pixels_to_ascii(img)
    ascii_img=""
    for i in range(0,len(ascii_str),width):
        ascii_img+=ascii_str[i:i+width]+"\n"
    print(ascii_img)
def upload_file():
    root=Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename()
    title="Select Image"
    filetypes=[("Image Files","*png,*jpg,.jpeg")]
    if file_path:
        image_to_ascii(file_path, width=120)
    else:
        print("No file selected")

upload_file()
