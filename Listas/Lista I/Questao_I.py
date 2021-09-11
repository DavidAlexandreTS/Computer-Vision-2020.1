import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imagem =cv.imread("kiki.png")

k_size = input("Enter the kernel size:")
k_weight = input("Now, give me the weights:")

a = int(k_size)
b = int(k_weight)

kernel = np.ones((a, a),np.float32)/b

img_filtred = cv.filter2D(imagem,-1,kernel)

plt.subplot(121),plt.imshow(imagem),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_filtred),plt.title('Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

cv.imwrite('kikis_filtred.png', img_filtred)