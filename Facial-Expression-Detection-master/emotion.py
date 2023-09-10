import cv2
import label_image
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

#Save just the rectangle faces in SubRecFaces
sub_face = im[y:y+h, x:x+w]

FaceFileName = "test.jpg" #Saving the current image from the webcam for testing.
cv2.imwrite(FaceFileName, sub_face)

text = label_image.main(FaceFileName)# Getting the Result from the label_image file, i.e., Classification Result.
text = text.title()# Title Case looks Stunning.
#print (text)
if (text == "Angry"):
    print ("CHILD IS ANGRY")
    
if (text == "Happiness"):
    print ("CHILD IS HAPPY")
if (text == "Sadness"):
    print ("CHILD IS CRYING")
if (text == "Yawning"):
    print ("CHILD IS Yawning")    
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)
rawCapture.truncate(0)

# Show the image
cv2.imshow('Capture',   im)
rawCapture.truncate(0)
key = cv2.waitKey(10)
