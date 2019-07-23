# Rename this file to be "filters.py"

# Add commands to import modules here
from PIL import Image

# Define your load_img() function here.

#       Parameters: The name of the file to be opened (string)

#       Returns: The image object with the opened file.

def load_img(pic_name):
    im = Image.open(pic_name)
    return im

# Define your show_img() function here.

#       Parameters: The image object to display.

#       Returns: nothing.

def show_img(pic_name):
    pic_name.show()

# Define your save_img() function here.

#       Parameters: The image object to save, the name to save the file as (string)

#       Returns: nothing.

def save_img(pic0, filename):
    pic0.save(filename)

# Define your obamicon() function here.

#       Parameters: The image object to apply the filter to.

#       Returns: A New Image object with the filter applied.

def obamicon(pic1):
    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)

    pixel = list(pic1.getdata())

    newImg = []

    for i in pixel:
        intensity = i[0] + i[1] + i[2]
        if intensity < 182:
            newImg.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            newImg.append(red)
        elif intensity >= 364 and intensity < 564:
            newImg.append(lightblue)
        elif intensity >= 564:
            newImg.append(yellow)

    newImage = Image.new("RGB", (736, 1189), i)
    newImage.putdata(newImg)
    return newImage


def inverse(pic1): #subtracted obama numbers from 255; comes out bright blues
    darkblue = (255, 204, 179)
    red = (38, 229, 222)
    lightblue = (143, 105, 97)
    yellow = (3, 28, 89)


    pixel = list(pic1.getdata())

    newImg = []

    for i in pixel:
        intensity = i[0] + i[1] + i[2]
        if intensity < 182:
            newImg.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            newImg.append(red)
        elif intensity >= 364 and intensity < 564:
            newImg.append(lightblue)
        elif intensity >= 564:
            newImg.append(yellow)

    newImage = Image.new("RGB", (736, 1189), i)
    newImage.putdata(newImg)
    return newImage

def grayscale(pic1):
    pixel = list(pic1.getdata())
    newImg = []
    for i in pixel:
        grayscale = (int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3))
        newImg.append(grayscale)
    newImage = Image.new("RGB", (736, 1189), i)
    newImage.putdata(newImg)
    return newImage

def inverted(pic1):
    pixel = list(pic1.getdata())
    newImg = []
    for i in pixel:
        inverted = (255-i[0], 255-i[1], 255-i[2])
        newImg.append(inverted)
    newImage = Image.new("RGB", (736, 1189), i)
    newImage.putdata(newImg)
    return newImage
#im = load_img("flowers.jpg")
#show_img(im)
#save_img(im, "Myflower.jpg")
