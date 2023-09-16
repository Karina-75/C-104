import cv2
img = cv2.imread('butterfly.jpg')
cv2.imshow('display image',img)

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('grey_scale', gray_image)
print(img)

cv2.waitKey(0)