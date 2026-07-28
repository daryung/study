import wlkatapython
import serial
import time

serial1 = serial.Serial("COM3", 115200)
mirobot1 = wlkatapython.Wlkata_UART()
mirobot1.init(serial1, -1)
mirobot1.speed(200)

mirobot1.writecoordinate(0,0,0,0,0,0,0,0)

mirobot1.writeangle(0,0,20,0,0,0,0) #Absolute value
mirobot1.writeangle(1,0,-10,0,0,0,0) #Incremental value