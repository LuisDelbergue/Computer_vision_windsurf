import cv2            #opencv, computer vision
import numpy as np
import time   #import time
import math

pTime = 0  #iniziating variable time
cap = cv2.VideoCapture("Transformed/test_1_front_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#saving = cv2.VideoWriter('front.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  h, w, c = img.shape  #parameters of the images
 
  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps))+'fps', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 255), 3) #write it in the window

  cropped=img[0:860,0:1920]

  hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
  low_ = np.array([21,220,0])
  high_ = np.array([30,255,255])
  mask1=cv2.inRange(hsv,low_,high_)
  filtered=cv2.bitwise_and(cropped,cropped,mask=mask1)

  imgGrey = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
  _, thrash = cv2.threshold(imgGrey, 20, 70, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
  contours, hierarchy = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  if len(contours) != 0:
    #cv2.drawContours(thrash, contours, -1, 255, 3)

    c = max(contours, key = cv2.contourArea)

    rows,cols = thrash.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(c, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(255, 255, 255),3)
    
  cv2.line(thrash, [960,0], [960,h], (255, 0, 255), 3)

  m2=(lefty-righty)/(0-(cols-1))
  m1=0
  angle=math.degrees(math.atan((m2-m1)/(1+m2*m1)))
  if (angle>0):
    angle=angle-90
  elif (angle<0):
    angle=angle+90
  cv2.putText(thrash, (str(float(angle))), (70,100), cv2.FONT_HERSHEY_PLAIN, 3,(150, 250, 0), 4)

  #saving.write(img) 
  cv2.imshow("video", thrash) 

  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear