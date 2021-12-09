import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ag az ketab khuneye plt baraye show kardan mikhastim estefade konim
#plt.imshow(img, cmap = "gray")
img = cv2.equalizeHist(img)
rows, cols = img.shape

def search_pixel_on_top_left():
    #az koja shoroo kon ta koja boro jelo v step ha chanta chanta pish beran
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if img[i, j] != 255:
               print("hooora")
               #print(i, j)
               return i, j
           
x1, y1 = search_pixel_on_top_left()
print(x1, y1)

cv2.circle(img, (172, 150), 20, (0, 0, 0), -1)
cv2.imwrite("result.jpg", img)

def search_for_right_pixel():
    for i in range(rows-1, 0, -1):
        for j in range(cols-1, 0, -1):
            if img[i, j] != 255:
                return i, j
            
x2, y2 = search_for_right_pixel()
print(x2,y2)

img_sudoku = img[x1:x2, y1:y2]

width, height = img_sudoku.shape
print(width, height)

cell_width = width // 9
cell_height = height // 9
print(cell_width, cell_height)

def count_none_white_pixels(img):
    rows, cols = img.shape
    dah_darsad = rows // 10
    counter = 0
    for i in range (rows):
        for j in range(cols):
            if img[i, j] != 255:
               counter +=1
    return counter

counter = 0
a = (cell_width * cell_height) / 35

for i in range(0, width, cell_width):
    for j in range(0, height, cell_height):
        small_img = img_sudoku[i : i+cell_width , j:j+cell_height]
        if small_img.shape == (cell_width, cell_height):
            if count_none_white_pixels(small_img) > a:
                cv2.imwrite(f"cells/{counter}.jpg", small_img)
                counter += 1
        
        
        
    



cv2.imshow("result", img_sudoku)
cv2.waitKey()



