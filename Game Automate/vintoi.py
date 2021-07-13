import cv2
vidcap = cv2.VideoCapture('punch3.mp4')
success,image = vidcap.read()
count = 102
while success:
  cv2.imwrite("dataset/punch/punch"+str(count)+".jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
