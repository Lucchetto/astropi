import csv
import face_detect
import data_acquisition
import mario
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep, gmtime, strftime
import cv2
from threading import Thread
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
face_service = Thread(target=faces_1s, args=())
face_service.start()

start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
file_name = "data_" + start_time + ".csv"
with open(file_name, 'a+') as data_file:
    data_file.write("UTC time, Face detection, Latitude, Longitude, Temperature, Pressure\n" )
    data_file.flush()
    data_writer = csv.writer(data_file)
    while True:
        current_data = data.write_data(do_you_see_any_face)
        print(current_data)
        data_writer.writerow(current_data)
        data_file.flush()
        sleep(0.75)
        #do_you_see_any_face = faces.find_faces()
        if do_you_see_any_face == False:
            sense.clear()
            mario_anim.mario_run_anim()