from PIL import Image
import os

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        image = Image.open(img)
        image.thumbnail((200, 200))
        image.save('Resize_to200/{}'.format(img))