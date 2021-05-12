import cv2, time

video=cv2.VideoCapture(0)

a=0

#while loop -> ctr c to stop (or z if ctr c doesn't work)
#while loop bc you want to have string of pics.
while True:
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3) -> if you use cv2.waitKey for a specific time (not 0 to stop with the button as before) you don't need this command anymore
    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print(a)
#it's to check how many iterations you have 

video.release()
cv2.destroyAllWindows()
