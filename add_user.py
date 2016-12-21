import cv2
import time

"""A script for creating a data set of known faces"""
__author__ = "tedfoodlin"

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

id = raw_input('Enter user ID: ')
index = 0

while(687):
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        index += 1
        cv2.imwrite("face_set/User." + str(id) + "." + str(index) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)
    cv2.imshow("Face",img);
    time.sleep(1)
    if(index>20):
        print("Face set created")
        break

cap.release()
cv2.destroyAllWindows()