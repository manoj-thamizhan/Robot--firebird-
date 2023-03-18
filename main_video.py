import cv2
from simple_facerec import SimpleFacerec
import serial
import time

ser = serial.Serial('COM8') 

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

detect_count =4

ser.write(b'8')

def rotate():
    ser.write(b'5')
    time.sleep(1)       # check which port was really used
    ser.write(b'6')
    time.sleep(0.6 )       # check which port was really used
    ser.write(b'8')
    time.sleep(1)
    ser.write(b'5')  
    ser.write(b'7')   # write a string
    time.sleep(1)
    ser.write(b'9')   # write a string
    ser.close()  



def callback():
    global detect_count
    print("detected")
    detect_count+=1

    if detect_count >4:
        rotate()


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame,callback)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()