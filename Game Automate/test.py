import tensorflow as tf
import numpy as np
import cv2
from pynput.keyboard import Key, Controller
from key import *
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import time

time.sleep(5)

def move():
    PressKey(L)
    time.sleep(0.08)
    ReleaseKey(L)

def kick():
    PressKey(X)
    time.sleep(0.08)
    ReleaseKey(X)

def normal():
    ReleaseKey(U)

def power():
    ReleaseKey(U)

def punch():
    PressKey(S)
    time.sleep(0.08)
    ReleaseKey(S)


model = tf.keras.models.load_model("100percent.h5")
url = "http://192.168.0.100:8080/video"
vidcap = cv2.VideoCapture("completed.mp4")


while True:
    
    success,images = vidcap.read()
    img = cv2.resize(images,(50,50))
    img = image.img_to_array(img)
    img = img/255
    X12 = np.array(img)
    new = X12.reshape(1,50,50,-1)
    predictionsc111 = model.predict(new)

    max_index111 = np.argmax(predictionsc111)

    emotions111 = ('kick', 'normal', 'power',"punch")
    predicted_emotion1111 = emotions111[max_index111]

    if predicted_emotion1111 == "kick":
        cv2.putText(images, "kick", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        kick()

    elif predicted_emotion1111 == "normal":
        cv2.putText(images, "normal", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        

    elif predicted_emotion1111 == "power":
        cv2.putText(images, "power", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        power()
        

    elif predicted_emotion1111 == "punch":
        cv2.putText(images, "punch", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        punch()

    cv2.imshow('frame',images)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break


    
