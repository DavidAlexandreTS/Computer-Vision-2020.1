import cv2 as cv
import numpy as np

# Filtro passa baixa
img = cv.imread('donzela.jpg')

kernel = np.array([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])
kernel = kernel/sum(kernel)

img_rst = cv.filter2D(img, -1, kernel)

cv.imwrite('donzela_b.jpg', img_rst)

# Filtro passa alta
kernel2 = np.array([[0.0, -1.0, 0.0],
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])

kernel2 = kernel2/(np.sum(kernel2) if np.sum(kernel2) != 0 else 1)

img_rslt = cv.filter2D(img, -1, kernel2)

cv.imwrite('donzela_a.jpg', img_rslt)

#Os filtros passa baixa tiram as altas frequências da imagem, ou seja, basicamente permanecem apenas
#as baixas frequências que incluem tons de cor mais constanstes e regiões que  são mais suaves, enquanto as altas
#frequencias incluem os detalhes da imagem. Em outras palavras, quando utilizamos um filtro passa baixa, nos jogamos fora
#os detalhes da imagem e quando aplicamos um passa alta, mantemos tais detalhes.