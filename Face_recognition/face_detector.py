import cv2

#this variable will search from your image looking for the face
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#create variable of the image

img=cv2.imread("news.jpg")


#if you want to search through the faces it works better with the gray

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# the haarcade works that if finds the pixel on the face, gives it's 3 dimensions and then create a rectangle that covers all front face
# create a variable that will store the weith, hight and of the face rectangle
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=20)
#scaleFactor is the function that works as the piramid and decreases the image into rectangles. 1.5 means it will decrease image by 50% and search in those rectangles for face. Plus= higher accuracy, but will go through the picture less times. So it's better to use smaller numbers)
#minNeighbors shows you how many neighbors are around, you can play with it

#so now, when we created the face arreys now let's use it to draw rectangle :

for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)


#it will take four arguments. 1- the image itself. 2-the starting point of the rectangle (x,y), another tuple of the other corner- lower right (x+w, y+h), then 3rd is the color in bhg format (blue, gray, green) 255 is for gray, and then the last one is the width of the rectangle (8) (picture in notes)
print(type(faces))
print(faces)

resized=cv2.resize (img,(int(img.shape[1]/3),int(img.shape[0]/3 )))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
