import cv2
import csv
import os

"""Recognize faces, print, and log to CSV"""
__author__ = "tedfoodlin"

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("recognizer/trainingData.yml")
date = raw_input("Enter today's date (mm.dd.yy): ")
file = "SignIn_Sheets/" + date + ".csv"

if os.path.isfile(file):
    open(("SignIn_Sheets/" + date + ".csv"), 'a')
    writer = csv.writer(open(("SignIn_Sheets/" + date + ".csv"), 'a'))
else:
    open(("SignIn_Sheets/" + date + ".csv"), 'w')
    writer = csv.writer(open(("SignIn_Sheets/" + date + ".csv"), 'w'))

logged_ID = 0
detecting_ID = 0

while(687):
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        logged_ID = detecting_ID
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)
        detecting_ID = recognizer.predict(gray[y:y+h, x:x+w])
        if (detecting_ID != logged_ID):
            if (detecting_ID == 1):
                face_detected = "Ted"
            elif (detecting_ID == 2):
                face_detected = "Someone else"
            print(face_detected)
            writer.writerow([face_detected])
    cv2.imshow(date, img);

cap.release()
cv2.destroyAllWindows()