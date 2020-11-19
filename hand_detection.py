import numpy as np
import cv2
import argparse
import orien_lines
import datetime
from datetime import date
import xlrd
from xlwt import Workbook

lst1=[]
lst2=[]
ap=argparse.ArgumentParser()
ap.add_argument("-d" , '--display' , dest='display' , type=int , default=1 , help='Display the detected image using opencv . This reduce FPS')


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()