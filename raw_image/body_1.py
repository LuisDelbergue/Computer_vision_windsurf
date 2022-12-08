import numpy as np
import cv2
import mediapipe as mp
import time
from cvzone.PoseModule import PoseDetector

detector=PoseDetector()
mpPose =  mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('segment4_pumping_and_foiling.mp4')
pTime=0

while True:
  success, img = cap.read()

  
  results=pose.process(img)
  print (results.pose_landmarks)

  img=detector.findPose(img)
  lmlist,bbox=detector.findPosition(img)

 #frames per second
  cTime = time.time()
  fps=1/(cTime-pTime)
  pTime=cTime
  cv2.putText(img,str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)

  cv2.imshow("video", img)
  cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()