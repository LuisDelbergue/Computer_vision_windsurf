import cv2            #opencv, computer vision
import mediapipe as mp  #detecting body parts
from cvzone.PoseModule import PoseDetector #detecting body parts
import time   #import time

mpDraw = mp.solutions.drawing_utils #drawing
mpPose = mp.solutions.pose  #calculate the pose
pose = mpPose.Pose()       #calculate the pose

pTime = 0  #iniziating variable time

cap = cv2.VideoCapture("segment4_pumping_and_foiling.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  
  results = pose.process(img)
  lmList = []
  h, w, c = img.shape
  if results.pose_landmarks:
    for id, lm in enumerate(results.pose_landmarks.landmark):
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) 
        if (id>10):                      
            #print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
            print(lmList)
            #cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
  
  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3) #write it in the window

  cv2.imshow("video", img)  #show the video
  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear