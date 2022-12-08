import cv2            #opencv, computer vision
import time   #import time

pTime = 0  #iniziating variable time

cap = cv2.VideoCapture("Transformed/test_1_front_view.mp4") #open the video
cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)   #full screen
cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #full screen

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
saving = cv2.VideoWriter('sail.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

while True:    #while the video is playing
  success, img = cap.read()  #read the video link
  
  h, w, c = img.shape  #parameters of the images

  cTime = time.time()  #obtain the time
  fps = 1 / (cTime - pTime) #calculate frames per second
  pTime = cTime      #restart the timer
  cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3) #write it in the window

  cropped=img[410:850,700:1200]
  #blurred = cv2.pyrMeanShiftFiltering(cropped, 2, 2)  #tarde en procesar y vaya lento

  imgGrey = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
  _, thrash = cv2.threshold(imgGrey, 20, 70, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  #print (contours[0][0][0]) #x1,y1
  #print (contours[0][0][0][1]) #y1
  #print (contours[1][0][0][0]) #x2

  for contour in contours:
    vertical=800
    for a in range(1,len(contours)):
      approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
      if (cv2.contourArea(contour)>17000 and cv2.contourArea(contour)<90000): 
        cv2.drawContours(cropped, [approx], 0, (255, 255, 0), 3)
        if (abs(contours[a-1][0][0][1]-contours[a][0][0][1])>250) and (abs(contours[a-1][0][0][1]-contours[a][0][0][1])<350):
          if (vertical>(abs(contours[a-1][0][0][0]-contours[a][0][0][0]))):
            vertical=(abs(contours[a-1][0][0][0]-contours[a][0][0][0]))
            min=a
    if (vertical !=800):
      image = cv2.line(cropped, contours[min-1][0][0], contours[min][0][0], (0, 255, 255), 4)
  image2 = cv2.line(img, [960,0], [960,h], (255, 0, 255), 4)

  saving.write(img)
  cv2.imshow("video", img)  #show the video

  if cv2.waitKey(1) & 0xFF == ord('q'): #if you write 0 (frame by frame), quit pressing q
    break   #close the video window

cv2.destroyAllWindows()  #clear
cap.release()      #clear