import os
from PIL import Image
from natsort import natsorted



images_list = []
for file in os.listdir('./jpegs/'):
    #if file.endswith(".pdf"):
    images_list.append(file)

print(sorted(images_list))
print(natsorted(images_list))

images = []
for i in natsorted(images_list):
    images.append(Image.open('./jpegs/' + i))


images[0].save('out.pdf', "PDF", resolution=100.0, save_all=True, append_images=images[1:])

