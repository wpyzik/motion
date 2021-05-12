#when there is something white - it means there was a movement

import cv2, time, pandas
from datetime import datetime

#this variable has nothing inside. You need it only so that later on when you call it there won't be an error
first_frame=None
status_list=[None, None]
times=[]
df= pandas.DataFrame(columns=["start", "end"])

video=cv2.VideoCapture(0)


while True:
    check, frame = video.read()
    frame=cv2.resize(frame, (640, 400))

    status=0
#we added this line to create a table that records entrance in and out. status is 0 when where is no motion
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
#this function clears the picture and eliminates the unnecessary blur, the numbers are the color specification, just pass it

#we want gray to become the first initiation of the video -> so first frame (background)
#you have this condition because you want to make the first frame of the picture non-moving option. The condition is met, it's not, so the first picture will become the one you are going to compare to. then then you want to convert it to gray so that's why you need this condition
    if first_frame is None:
        first_frame=gray
        continue
#once gray is the fisrt frame we don't want the loop to continue to the cv2.imshow... we want it to continue to the second frame so we write "continue"

    delta_frame=cv2.absdiff(first_frame,gray)
#this gives us a new picture

    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY) [1]
#you want to make it less blur, smooth white areas
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

#find and draw contours in the image, so first we want to find the area that the contour descrbes and save them in the new variable
#so (cntr,-) is a variable that stors contours of all white objects = frame of areas
    (cnts,_) =cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#we want to keep only those that have more than xx pixels draw rectangle
#if cv2.contourArea(contour) < 10000: <- bigger number, more objects it will omit
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1
#status one must finish after the background is set
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)
#to save memory, instead of having rows of 0s and 1s, we will keep only last two numbers in the list to save time ofchanges
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Tresh Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"start":times[i], "end":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
#to ignore index you pass ignore_index=True
#must be at the end of the loop

video.release()
cv2.destroyAllWindows()
