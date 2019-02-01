import cv2
import logging
# import sys
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# from time import sleep

class face_detection:
    def __init__(self, src_camera, camera_output, cascade_file, logger):
        self.camera = src_camera
        self.cam_output = camera_output
        self.facedata = cascade_file
        self.logger = logger
    def find_faces(self):
        self.camera.capture(self.cam_output, format="bgr")
        out_image = self.cam_output.array
        gray_image = cv2.cvtColor(out_image, cv2.COLOR_BGR2GRAY)
        faces = self.facedata.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        have_face = False
        if faces == ():
            self.logger.info("No faces detected")
        else:
            self.logger.info("Face detected")
            have_face = True
        self.cam_output.truncate(0)
        return have_face

'''
camera = PiCamera()
camera.resolution = (512, 512)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(512, 512))

sleep(0.1)

cascPath = "./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

faces = face_detection(camera, rawCapture, faceCascade)
while True:
    faces.find_faces()
'''