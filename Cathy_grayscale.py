def grayscale(pic1):
    pixel = list(pic1.getdata())
    newImg = []
    for i in pixel:
        grayscale = (int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3), int((i[0] + i[1] + i[2])/3))
        newImg.append(grayscale)
    newImage = Image.new("RGB", (736, 1189), i)
    newImage.putdata(newImg)
    return newImage
