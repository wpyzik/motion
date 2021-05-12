import cv2, time

#to read the video from a file or webcam , adding text, detecting pictures detecting
video=cv2.VideoCapture(0)
#if you put the number there it applies that you use the webcam; 0- internal, 1- external camera, 2- whatever else you use. If you have a file, simply pass it without any numbers)

check, frame = video.read()

print(check)
print(frame)

time.sleep(3)
cv2.imshow("Capturing", frame)

#cv2.waitKey is to show you the window and don't disappear after a sec. 0 means when you click a bottom
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
