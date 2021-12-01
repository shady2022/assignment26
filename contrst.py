import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\python_programming\\tamrin6\\barf.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist_gray = cv2.calcHist([gray],[0], None, [256], [0, 255])

equ_gray = cv2.equalizeHist(gray)
hist_equ = cv2.calcHist([equ_gray], [0], None, [256], [0,255])

CLAHE_default = cv2.createCLAHE()
CLAHE_equ_def = CLAHE_default.apply(gray)
hist_def = cv2.calcHist([CLAHE_equ_def], [0], None, [256], [0,255])

CLAHE_select = cv2.createCLAHE(clipLimit= 3.0, tileGridSize= (5,5))
CLAHE_equ_sele = CLAHE_select.apply(gray)
hist_sele = cv2.calcHist([CLAHE_equ_sele], [0], None, [256], [0,255])

plt.subplot(241), plt.imshow (gray, "gray")
plt.title("original image"), plt.axis("off")

plt.subplot(242), plt.imshow (equ_gray, "gray")
plt.title("Normal equalization"), plt.axis("off")

plt.subplot(243), plt.imshow (CLAHE_equ_def, "gray")
plt.title("Normal equalization"), plt.axis("off")

plt.subplot(244), plt.imshow (CLAHE_equ_sele, "gray"),
plt.title("clahe equalization (select)"), plt.axis("off")

plt.subplot(245), plt.plot (hist_gray, "k")
plt.title("original image histogram")

plt.subplot(246), plt.plot (hist_equ, "k")
plt.title("normal image histogram"), plt.yticks ([])

plt.subplot(247), plt.plot (hist_def, "k")
plt.title("clahe (default) histogram"), plt.yticks ([])

plt.subplot(248), plt.plot (hist_sele, "k")
plt.title("clahe (select) histogram"), plt.yticks ([])

plt.xlim([0,256])
plt.show()