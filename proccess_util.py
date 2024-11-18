from PIL import Image

for i in range(1, 1001):
    img2 = Image.open('./images/img.jpg').copy()
    img2.save(f'./images/img_{i}.jpg')
