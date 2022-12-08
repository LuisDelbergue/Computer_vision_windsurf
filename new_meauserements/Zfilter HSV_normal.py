import cv2            #opencv, computer vision
import numpy as np

cap = cv2.VideoCapture("Transformed/a.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
#cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

def trackChaned(x):
  pass
 
cv2.namedWindow('Color Track Bar',cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Track Bar", 300, 200)
h0='H_low'
h1='S_low'
h2='V_low'
h3='H_upp'
h4='S_upp'
h5='V_upp'
wnd = 'Colorbars'
cv2.createTrackbar("H_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("S_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("V_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("H_upp", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("S_upp", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("V_upp", "Color Track Bar",0,255,trackChaned)

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  
  h, w, c = img.shape  #parameters of the images
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  hu0=cv2.getTrackbarPos("H_low", "Color Track Bar")
  hu1=cv2.getTrackbarPos("S_low", "Color Track Bar")
  hu2=cv2.getTrackbarPos("V_low", "Color Track Bar")
  hu3=cv2.getTrackbarPos("H_upp", "Color Track Bar")
  hu4=cv2.getTrackbarPos("S_upp", "Color Track Bar")
  hu5=cv2.getTrackbarPos("V_upp", "Color Track Bar")
  low_ = np.array([hu0,hu1,hu2])
  high_ = np.array([hu3,hu4,hu5])
  mask1=cv2.inRange(hsv,low_,high_)
  final=cv2.bitwise_and(img,img,mask=mask1)
  cv2.imshow("video", final) 

  #cv2.imshow("video", img)  #show the video
  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear