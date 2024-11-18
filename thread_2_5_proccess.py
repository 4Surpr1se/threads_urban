# import multiprocessing
from PIL import Image
import datetime
# 0:00:21.995841

def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


start = datetime.datetime.now()
for i in range(1, 201):
    image_path = f'./images/img_{i}.jpg'
    resize_image(image_path)
end = datetime.datetime.now()
print(end - start)
