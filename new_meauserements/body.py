import cv2            #opencv, computer vision
import mediapipe as mp  #detecting body parts
from cvzone.PoseModule import PoseDetector #detecting body parts
import time   #import time

mpDraw = mp.solutions.drawing_utils #drawing
mpPose = mp.solutions.pose  #calculate the pose
pose = mpPose.Pose()       #calculate the pose

pTime = 0  #iniziating variable time

cap = cv2.VideoCapture("Transformed/test_1_front_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#saving = cv2.VideoWriter('body.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  h, w, c = img.shape  #parameters of the images
  results = pose.process(img) #obtain the pose
  lmList = []   #iniziate the list
  sum=0    #iniziating variable
  if results.pose_landmarks:  #if it finds the points
    for id, lm in enumerate(results.pose_landmarks.landmark): #obtain the data
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) #draw them
        if (id>10):    #not counting the face                  
            #print(id, lm)  #print data of each point
            cx, cy = int(lm.x * w), int(lm.y * h) #obtain the pxls
            lmList.append([id, cx, cy])  #create list of point and coordinates x and y
            #print(lmList) #print data of every point
            #cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)  #draw each point
            sum=cx-w/2+sum   #calculating the position
            if sum >200:     #if it is in the right
              print("Right side")
            elif sum <200:   #if it is in the left
              print ("Left side")

  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3) #write it in the window

  #saving.write(img)

  cv2.imshow("video", img)  #show the video
  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear