# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
import numpy as np
import threading
import time
import csv


count = 10
stop_timer=True

def on_timeout():
    global count
    global timer
    if count>0: 
        print(count)
        count = count - 1
        timer = threading.Timer(1.0, on_timeout)
        timer.start()
    else:
        timer.cancel()
        print("Timer stopped")
    






def display(datums):
    global count
    datum = datums[0]
    img = datum.cvOutputData
    # define the font and text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(count)
    font_scale = 4
    thickness = 2

    # get the size of the text
    size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    # calculate the x and y coordinates to center the text
    x = int((img.shape[1] - size[0]) / 2)
    y = int((img.shape[0] + size[1]) / 2)

    # draw the text on the image
    cv2.putText(img, text, (x, y), font, font_scale, (255, 255, 255), thickness)

    # Create a window and set it to full screen mode
    cv2.namedWindow("fullscreen", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("fullscreen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("fullscreen", img)
    key = cv2.waitKey(1)
    
    return (key == 27)


def printKeypoints(datums):
    datum = datums[0]
    print("Body keypoints: \n" + str(datum.poseKeypoints))
    print(type(str(datum.poseKeypoints)))
    print("Face keypoints: \n" + str(datum.faceKeypoints))
    print("Left hand keypoints: \n" + str(datum.handKeypoints[0]))
    print("Right hand keypoints: \n" + str(datum.handKeypoints[1]))
    
    
    # Open a CSV file for writing
    with open('floats.csv', 'a', newline='') as file:
        
        # Create a CSV writer object
        writer = csv.writer(file)
        
        # Write each float in the array as a row in the CSV file
        for f in datum.poseKeypoints:
            writer.writerow([f])


def run():
    global stop_timer
    global count
    count = 10
    stop_timer=True
    try:
        # Import Openpose (Windows/Ubuntu/OSX)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            # Windows Import
            if platform == "win32":
                # Change these variables to point to the correct folder (Release/x64 etc.)
                sys.path.append(dir_path + '/../../build/python/openpose/Release');
                os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../build/x64/Release;' +  dir_path + '/../../build/bin;'
                import pyopenpose as op
            else:
                # Change these variables to point to the correct folder (Release/x64 etc.)
                sys.path.append('../../python');
                # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
                # sys.path.append('/usr/local/python')
                from openpose import pyopenpose as op
        except ImportError as e:
            print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
            raise e

        # Flags
        parser = argparse.ArgumentParser()
        parser.add_argument("--no-display", action="store_true", help="Disable display.")
        args = parser.parse_known_args()

        # Custom Params (refer to include/openpose/flags.hpp for more parameters)
        params = dict()
        params["model_folder"] = "../../models/"

        # Add others in path?
        for i in range(0, len(args[1])):
            curr_item = args[1][i]
            if i != len(args[1])-1: next_item = args[1][i+1]
            else: next_item = "1"
            if "--" in curr_item and "--" in next_item:
                key = curr_item.replace('-','')
                if key not in params:  params[key] = "1"
            elif "--" in curr_item and "--" not in next_item:
                key = curr_item.replace('-','')
                if key not in params: params[key] = next_item

        # Construct it from system arguments
        # op.init_argv(args[1])
        # oppython = op.OpenposePython()

        # Starting OpenPose
        opWrapper = op.WrapperPython(op.ThreadManagerMode.AsynchronousOut)
        opWrapper.configure(params)
        opWrapper.start()

        # start timer
        timer = threading.Timer(1.0, on_timeout)
        timer.start()
        # Main loop
        userWantsToExit = False
        while not userWantsToExit and count > 0:
            # Pop frame
            datumProcessed = op.VectorDatum()
            if opWrapper.waitAndPop(datumProcessed):
                if not args[0].no_display:
                    # Display image
                    userWantsToExit = display(datumProcessed)

                printKeypoints(datumProcessed)

            
            else:
                break

    except Exception as e:
        print(e)
        sys.exit(-1)
