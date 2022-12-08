import numpy as np
import cv2
import mediapipe as mp
from cvzone.PoseModule import PoseDetector

detector=PoseDetector()

cap = cv2.VideoCapture("segment4_pumping_and_foiling.mp4")
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
  success, img = cap.read()

  img=detector.findPose(img)
  lmlist,bbox=detector.findPosition(img)

  cv2.imshow("video", img)
  if cv2.waitKey(1) & 0xFF == ord('q'): #quitar con q
    break
  #cv2.waitKey(1)  #si pones 0, puedes pasar con el 0 cada fotograma y cerrar ventana
cv2.destroyAllWindows()
cap.release()