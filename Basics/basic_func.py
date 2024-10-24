import cv2 as cv

#reading img
img = cv.imread('/home/omar/cs/cv/compvi/Resources/Photos/park.jpg')
cv.imshow('Park',img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny',canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated',dilated)

#eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroted',eroded)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropped 
cropped =img[50:200 , 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)


