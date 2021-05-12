import cv2

#if color = 1, if black and white = 0,3rd parameter -1 = color image bt also alpha channel meaning you have transparency in the image
img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
#(1485 rows and 990 columns)
print(img.ndim)
#3 dimensions

cv2.imshow("Galaxy",img)

#it resized imagine in half. The zero index = 1485, 1 index =990
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#to display image on the screen
#here "Galaxy' is the window name, then what do you wanna show
cv2.imshow("Galaxy",resized_image)
#to specify how long it will be on the screen - if 0, it will close when user clicks any botton, 2000 - 2000mili seconds so 2 seconds
#first you give the new name of the image,then you provide the image you want to store in this file
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
