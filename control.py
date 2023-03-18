import serial
import time

ser = serial.Serial('COM3')  # open serial port
print(ser.name)  
ser.write(b'8')
time.sleep(1)       # check which port was really used
ser.write(b'4')
time.sleep(1)       # check which port was really used
ser.write(b'8')
time.sleep(1)
ser.write(b'5')     # write a string
ser.close()  