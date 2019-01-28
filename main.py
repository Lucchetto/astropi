import face_detect
import data_acquisition
import mario
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import _thread
from sense_hat import SenseHat

camera = PiCamera()
camera.resolution = (2592, 1952)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(2592, 1952))

sleep(0.1)

cascPath = "./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

sense = SenseHat()

faces = face_detect.face_detection(camera, rawCapture, faceCascade)
data = data_acquisition.data_acq(sense)
mario_anim = mario.mario_running(sense)

global do_you_see_any_face
do_you_see_any_face = False

def faces_1s():
    while True:
        global do_you_see_any_face
        do_you_see_any_face = faces.find_faces()
        
        # (0.9)

# Main program
_thread.start_new_thread(faces_1s, ())
while True:
    data_file = open('dati.csv', 'a')
    data.write_data(data_file, do_you_see_any_face)
    #do_you_see_any_face = faces.find_faces()
    if do_you_see_any_face == False:
        sense.clear()
        mario_anim.mario_run_anim()