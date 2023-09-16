import cv2

img = cv2.imread('poster.jpg')
rocket = img[120:360, 400:500]

img[0:240, 500:600] = rocket

text = 'I love coding'
cv2.putText(img, text, (20, 200), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,255,0))

cv2.imshow('greeting card', img)

cv2.waitKey(6000)