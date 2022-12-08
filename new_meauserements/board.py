import cv2            #opencv, computer vision
import time   #import time

pTime = 0  #iniziating variable time

cap = cv2.VideoCapture("Transformed/test_1_front_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#saving = cv2.VideoWriter('board.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  
  h, w, c = img.shape  #parameters of the images

  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3) #write it in the window
 
  ret,thresh = cv2.threshold(img,206,210,cv2.THRESH_BINARY)
  
  i=1
  flag0=0
  flagw=0
  point0=(0,h)
  pointw=(w,h)
  for i in range(230):
    (b0, g0, r0)=thresh[(h-i)-1,0]
    (bw, gw, rw)=thresh[(h-i)-1,w-1]
    if (b0>190 and g0>190 and r0>190):
      flag0=1
      point0=(0,h-i)
    if (bw>190 and gw>190 and rw>190): #poner and if flag==1
      flagw=1
      pointw=(w,h-i)
  if (flagw and flag0):
    image = cv2.line(img, (0, 830), (w, 830), (0, 255, 0), 4)
    image = cv2.line(img, point0, pointw, (0, 255, 255), 4)

  #saving.write(thresh)
  #cv2.imshow("video", thresh)  #show the video
  cv2.imshow("video", img) 

  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear