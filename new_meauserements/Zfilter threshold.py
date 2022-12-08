import cv2            #opencv, computer vision
import time   #import time
import numpy as np

pTime = 0  #iniziating variable time

cap = cv2.VideoCapture("Transformed/test_1_front_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
#cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

def trackChaned(x):
  pass
 
 
cv2.namedWindow('Color Track Bar')
hh='Max'
hl='Min'
wnd = 'Colorbars'
cv2.createTrackbar("Max", "Color Track Bar",0,255,trackChaned)
cv2.createTrackbar("Min", "Color Track Bar",0,255,trackChaned)
img = cv2.imread('lena.tif')

while True:    #while the video is playing
  success, img = cap.read()  #read the video link

  cropped=img[720:1000,600:1200]
  h, w, c = cropped.shape  #parameters of the images
 
  #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  #lower_red = np.array([250,0,0])
  #upper_red = np.array([180,255,255])
  #mask = cv2.inRange(hsv,lower_red,upper_red)
  #res = cv2.bitwise_and(img,img,mask=mask)
  hul=cv2.getTrackbarPos("Max", "Color Track Bar")
  huh=cv2.getTrackbarPos("Min", "Color Track Bar")
  ret,thresh1 = cv2.threshold(cropped,hul,huh,cv2.THRESH_BINARY)
  cv2.imshow("video", thresh1) 

  #cv2.imshow("video", img)  #show the video
  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear