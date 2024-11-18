import pprint

all_images = []
for image in range(201, 401):
    all_images.append(f'./images/img_{image}.jpg')
pprint.pprint(all_images)
