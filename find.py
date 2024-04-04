import cv2
import numpy as np
import time

from inference.interact.interactive_utils import *

import overlay
    
def detect_live(image, frame, boundary, fps):

    # image => mask
    # frame => orignal  

    # grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # thresholding to separate non-black areas
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # set boundaries
    top = int(boundary[0])
    bottom = int(boundary[1])
    left = int(boundary[2])
    right = int(boundary[3])

    boundary = {'left': left, 'top': top, 'right': right, 'bottom': bottom}

    # check the boundaries
    out_of_bounds_objects = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # check if the object is out of the boundary
        if (x < boundary['left'] or 
            x + w > boundary['right'] or
            y < boundary['top'] or 
            y + h > boundary['bottom']):
            out_of_bounds_objects.append(contour)
                
    if not contours:
            # assume frame is a PIL Image, get its dimensions
            width, height = frame.size
            # consider the entire image as out of bounds
            out_of_bounds_objects.append(np.array([[0, 0], [width, 0], [width, height], [0, height]]))
    
    out_of_bounds = out_of_bounds_objects

    # show results
    if out_of_bounds:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        # print("Some objects are out of the boundary.")
    else:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    
    image = overlay.cv2_to_pil(image)
    image = overlay.overlay(frame, image)

    cv2.imshow('Image with Boundary', image)

    ## set fps here
    key = cv2.waitKey(1)  # Wait for a key press to proceed
    if(key == 13):
        print("hello")