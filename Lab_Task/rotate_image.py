from PIL import Image
img = Image.open('1.png')
img.rotate(45).save('newRotatePic.png')
img_new = Image.open('newRotatePic.png')
img_new.show()