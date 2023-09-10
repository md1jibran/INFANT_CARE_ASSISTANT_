import cv2
import label_image
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)

size = 4
IM_WIDTH = 640    
IM_HEIGHT = 480   

# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

camera = PiCamera()
camera.resolution = (640, 480)
#camera.resolution = (320, 240)
camera.framerate = 24
#rawCapture = PiRGBArray(camera, size=(640, 480))
rawCapture = PiRGBArray(camera, size=camera.resolution)
time.sleep(0.5)
#rawCapture.truncate(0)

for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
    ( im) = frame.array
    im=cv2.flip(im,1,0) #Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

    # detect MultiScale / faces 
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
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
            GPIO.output(2, True)
            GPIO.output(3, False)
            GPIO.output(4, False)
        if (text == "Happiness"):
            print ("CHILD IS HAPPY")
            GPIO.output(2, False)
            GPIO.output(3, True)
            GPIO.output(4, False)
        if (text == "Sadness"):
            print ("CHILD IS CRYING")
            GPIO.output(2, False)
            GPIO.output(3, False)
            GPIO.output(4, True)
        if (text == "Yawning"):
            print ("CHILD IS Yawning")
            GPIO.output(2, True)
            GPIO.output(3, True)
            GPIO.output(4, False)    
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)
        rawCapture.truncate(0)

    # Show the image
    cv2.imshow('Capture',   im)
    rawCapture.truncate(0)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop 
    if key == 27: #The Esc key
        break
