import cv2
import os

CASCADE_PATH = "haarcascade_frontalface_alt.xml"
facecascade = cv2.CascadeClassifier(CASCADE_PATH)
imgFormat = ".jpg"
fullimgpath = "/home/pi/Desktop/Facial-Expression-Detection-master/images/yawning/"
faceimgpath = "/home/pi/Desktop/Facial-Expression-Detection-master/images/yawning/"
imfilelist = [os.path.join(fullimgpath, f) for f in os.listdir(fullimgpath) if f.endswith(imgFormat)]

for el in imfilelist:
   print (el)
   imagen = cv2.imread(el)
   gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
   faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.CV_HAAR_SCALE_IMAGE
        flags=cv2.CASCADE_SCALE_IMAGE
   )

   for (x, y, w, h) in faces:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = imagen[y:y + h, x:x + w]


   cv2.imshow('Imagen', imagen)
   cv2.waitKey(1000)