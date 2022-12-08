import cv2            #opencv, computer vision
import numpy as np

cap = cv2.VideoCapture("segment4_pumping_and_foiling.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
#cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

def trackChaned(x):
  pass
 
cv2.namedWindow('Color Track Bar')
h0='R_low'
h1='G_low'
h2='B_low'
h3='R_upp'
h4='G_upp'
h5='B_upp'
wnd = 'Colorbars'
cv2.createTrackbar("R_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("G_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("B_low", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("R_upp", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("G_upp", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("B_upp", "Color Track Bar",0,255,trackChaned)

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  
  h, w, c = img.shape  #parameters of the images
 
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  hu0=cv2.getTrackbarPos("R_low", "Color Track Bar")
  hu1=cv2.getTrackbarPos("G_low", "Color Track Bar")
  hu2=cv2.getTrackbarPos("B_low", "Color Track Bar")
  hu3=cv2.getTrackbarPos("B_upp", "Color Track Bar")
  hu4=cv2.getTrackbarPos("B_upp", "Color Track Bar")
  hu5=cv2.getTrackbarPos("B_upp", "Color Track Bar")
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