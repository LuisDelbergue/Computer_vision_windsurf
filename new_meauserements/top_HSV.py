import cv2            #opencv, computer vision
import numpy as np
import time   #import time
import math
import csv

pTime = 0  #iniziating variable time
cap = cv2.VideoCapture("Transformed/test_1_top_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

data = [] 

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#saving = cv2.VideoWriter('top.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  h, w, c = img.shape  #parameters of the images
 
  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps))+'fps', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3) #write it in the window

  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  low_ = np.array([22,34,29])
  high_ = np.array([54,255,255])
  mask1=cv2.inRange(hsv,low_,high_)
  filtered=cv2.bitwise_and(img,img,mask=mask1)

  kernel = np.ones((2, 2), np.uint8)
  dilation = cv2.dilate(filtered, kernel, iterations=2)
  closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

  imgGrey = cv2.cvtColor(closing, cv2.COLOR_BGR2GRAY)
  _, thrash = cv2.threshold(imgGrey, 20, 70, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
  contours, hierarchy = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  dmin=50000
  c1=0
  c2=0
  if len(contours) != 0:
    for contour in contours:
      if (cv2.contourArea(contour)>10000):
          approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)           
          #cv2.drawContours(thrash, [approx], 0, (255, 255, 0), 3)

          rows,cols = thrash.shape[:2]
          [vx,vy,x,y] = cv2.fitLine(contour, cv2.DIST_L2,0,0.01,0.01)
          lefty = int((-x*vy/vx) + y)
          righty = int(((cols-x)*vy/vx)+y)

          m=(righty-lefty)/(cols-1)
          dy=m*(960-cols-1)+righty
          dy=abs(dy-540)

          if(dmin>dy):
            dmin=dy
            c1=lefty
            c2=righty
            
  cv2.line(img,(cols-1,c2),(0,c1),(255,255,255),3) 

  cv2.line(img, [850,0], [1180,h], (255, 0, 255), 3)

  m2=(c1-c2)/(0-(cols-1))
  m1=(h)/(1180-850)
  angle=math.degrees(math.atan((m2-m1)/(1+m2*m1)))
  data.append(angle)

  cv2.putText(img, (str(float(angle))), (70,100), cv2.FONT_HERSHEY_PLAIN, 3,(150, 250, 0), 4)

  #saving.write(img)  
  cv2.imshow("video", img) 

  #with open('yaw.csv', 'w') as file:
    #writer = csv.writer(file)
    #writer.writerow(data)

  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear

