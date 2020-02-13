from PIL import Image
img = Image.open('1.png')
img.resize((250, 500)).save('newSz.png')
img_new = Image.open('newSz.png')
img_new.show()