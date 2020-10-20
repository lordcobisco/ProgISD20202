from os import system
system('clear')
import numpy as np
import cv2
'''
azulEscuro = np.array([100, 67, 0], dtype = "uint8")
azulClaro = np.array([255, 128, 50], dtype = "uint8")
#camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('video.mp4')

while True:
  print('Entrou')
  (sucesso, frame) = camera.read()
  if not sucesso:
    break
  obj = cv2.inRange(frame, azulEscuro, azulClaro)
  obj = cv2.GaussianBlur(obj, (3, 3), 0)
  (_, cnts, _) = cv2.findContours(obj.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  if len(cnts) > 0:
    cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
    cv2.drawContours(frame, [rect], -1, (0, 255, 255),2)
  cv2.imshow("Tracking", frame)
  cv2.imshow("Binary", obj)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()
'''


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
