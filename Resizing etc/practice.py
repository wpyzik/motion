import cv2
import glob

#glob finds names of the pathways to give us a pattern
#create a list of all the files with the jpg extension

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image, 0)
    re=cv2.resize(img, (100,100))
    cv2.imshow(" "+image, re)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_ "+image, re)
