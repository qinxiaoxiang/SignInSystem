import os
import cv2
import numpy as np
from PIL import Image

"""Trainer for face set"""
__author__ = "tedfoodlin"

recognizer = cv2.face.createLBPHFaceRecognizer()
path = 'face_set'

def getImages(m_path):
    imagePaths = [os.path.join(m_path, f) for f in os.listdir(m_path)]
    print(imagePaths)
    m_faceArray = []
    m_idArray = []
    for imagePath in imagePaths:
        if (str(imagePath).split("/")[1].startswith('U')):
            faceImg = Image.open(imagePath).convert('L')
            face = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            m_faceArray.append(face)
            m_idArray.append(ID)
    print("Training done")
    return m_faceArray, np.array(m_idArray)

face_array, ID_array = getImages(path)
recognizer.train(face_array, ID_array)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
