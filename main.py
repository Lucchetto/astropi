import csv
import face_detect
import data_acquisition
import logging
import mario
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep, gmtime, strftime
import cv2
from threading import Thread
from sense_hat import SenseHat
from sys import stdout

start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
log_file = "log_" + start_time + ".log"


logger = logging.getLogger()
output_handler = logging.StreamHandler(stdout)
output_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
log_handler = logging.FileHandler(log_file)
log_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d"))
logger.addHandler(output_handler)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

camera = PiCamera()
camera.resolution = (1920, 1088)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(1920, 1088))

sleep(0.1)

cascPath = "./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

sense = SenseHat()

faces = face_detect.face_detection(camera, rawCapture, faceCascade, logger)
data = data_acquisition.data_acq(sense)
mario_anim = mario.mario_running(sense)

global do_you_see_any_face
do_you_see_any_face = False
global room_brightness
room_brightness = 0.0

def faces_1s():
    while True:
        global do_you_see_any_face
        global room_brightness
        do_you_see_any_face, room_brightness = faces.find_faces()
        
        # (0.9)

# Main program
face_service = Thread(target=faces_1s, args=())
face_service.start()

file_name = "data_" + start_time + ".csv"
with open(file_name, 'a+') as data_file:
    data_file.write("UTC time,Face detection,Latitude,Longitude,Temperature °C,Humidity %,Pressure mbar,Room brightness\n" )
    data_file.flush()
    data_writer = csv.writer(data_file)
    while True:
        logger.info("Acquiring data about this place...")
        current_data = data.write_data(do_you_see_any_face)
        current_data.append(room_brightness)
        data_writer.writerow(current_data)
        data_file.flush()
        sleep(0.75)
        #do_you_see_any_face = faces.find_faces()
        if do_you_see_any_face == False:
            sense.clear()
            mario_anim.mario_run_anim()