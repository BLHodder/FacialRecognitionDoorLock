import cv2;
import sys;
import logging as log;
import datetime as dt;
from time import sleep;
import numpy as np;
import face_recognition





video_capture = cv2.VideoCapture(0)


while True:
  if not video_capture.isOpened():
    print("Unable to open camera.")
    sleep(5)
    pass

  faceLocations = []
  faceEncodings = []
  faceNames = []
  processThisFrame = True

while True:
  ret, frame = video_capture.read()

  smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
  rgbSmallFrame = smallFrame[:,:,::-1]

  if processThisFrame:
    faceLocations = face_recognition.face_recognition(rgbSmallFrame)
    faceEncodings = face_recognition.face_encodings(rgbSmallFrame)

  faceNames = []
  for 
  