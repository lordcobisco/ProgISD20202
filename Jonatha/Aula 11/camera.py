import cv2
import time

# 1. Create an object. Zero for external camera
video = cv2.VideoCapture(0)
a=0
while(True):
  a += 1
  # 3. Create a frame object
  check, frame = video.read()

  print(check)
  print(frame)
  # 6. Converting to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # 4. Show the frame
  cv2.imshow('Capturing...', gray)

  # 5. For press any kay to out
  #cv2.waitKey(0)

  #7. For playing
  key = cv2.waitKey(1)
  if key == ord('q'):
    break
# 2. Shutdown the camera

print(a)
video.release()

cv2.destroyAllWindows
