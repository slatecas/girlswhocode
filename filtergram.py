from filters import *
#options are (inverted, inverse, obamicon and grayscale)
newImage = load_img("flowers.jpg")
pic = inverted(newImage)
show_img(pic)

newImage1 = obamicon(pic)
show_img(newImage1)
