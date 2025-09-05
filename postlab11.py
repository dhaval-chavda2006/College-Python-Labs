#Write a Python program to display details of an image 
# (dimension of an image, shape of an image, min pixel value at channel B).


# import numpy as np
# from PIL import Image, ImageOps
# import matplotlib.pyplot as plt


# img = Image.open("MU.jpg")  

# img_array = np.array(img)
# dimensions = img_array.shape
# print(f"Dimensions (Height, Width, Channels): {dimensions}")

# print(f"Shape of the image array: {img_array.shape}")

# if len(dimensions) == 2:
#     print("Grayscale image: no separate color channels")
#     min_blue = np.min(img_array)
# else:
#     min_blue = np.min(img_array[:, :, 2])

# print(f"Minimum pixel value in Blue channel: {min_blue}")

# plt.imshow(img)
# plt.title("Input Image")
# plt.axis("off")
# plt.show()







#Python program to padding black spaces 

# from PIL import Image, ImageOps
# import matplotlib.pyplot as plt


# img = Image.open("MU.jpg")   


# padding = (50, 50, 50, 50)  


# padded_img = ImageOps.expand(img, border=padding, fill="black")

# padded_img.save("padded_image.jpg")

# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.title("Original Image")
# plt.axis("off")
# plt.subplot(1, 2, 2)
# plt.imshow(padded_img)
# plt.title("Padded Image")
# plt.axis("off")

# plt.show()







#Python program to visualize RGB channels 


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("MU.jpg")  
img_array = np.array(img)

R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")


plt.subplot(1, 4, 2)
plt.imshow(R, cmap="Reds")
plt.title("Red Channel")
plt.axis("off")


plt.subplot(1, 4, 3)
plt.imshow(G, cmap="Greens")
plt.title("Green Channel")
plt.axis("off")


plt.subplot(1, 4, 4)
plt.imshow(B, cmap="Blues")
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()
