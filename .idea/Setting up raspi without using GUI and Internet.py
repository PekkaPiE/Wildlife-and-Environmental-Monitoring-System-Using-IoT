#importing required libraries
import Adafruit_DHT
from time import time, sleep
from urllib.request import urlopen
import sys
import json
import requests
import RPi.GPIO as GPIO
import pynmea2
import serial
from picamera import PiCamera
import csv
import time

GPIO.setwarnings(False) #to avoid GPIO warnings
GPIO.setmode(GPIO.BOARD) #to set GPIO board mode
#WRITE_API = "JP5ATDSYB8AE03SY"
#BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)
SENSOR_PIN = 4 #connecting temperature sensor to GPIO 4 or physical pin 7
SENSOR_TYPE = Adafruit_DHT.DHT11 #defining the sensor type

#SensorPrevSec = 0
#SensorInterval = 2
#ThingSpeakPrevSec = 0
#ThingSpeakInterval = 20
GPIO.setup(11, GPIO.IN) #Read output from PIR motion sensor from pin 11
GPIO.setup(13, GPIO.IN) #Read output from PIR motion sensor from pin 11
#frame = 0
port = "/dev/serial0" # setting port to serial0
serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5) #defining serialport variable
camera = PiCamera() #creating picamera object
camera.start_preview() #starting camera
csvfile = "temperature_humidity.csv" #creating csv file to store temperaure and humidity data
csvfile2 = "GPS_info.csv" #creating csv file to store gps data
frame = 0 #creating frame variable to store image
while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN) #storing temperature and humidity data to variables
    if humidity is not None and temperature is not None: #if humidity and temperature variables are not none
        print('Temp={0:0.1f} C  Humidity={1:0.1f} %'.format(temperature, humidity)) #print temperature and humidity values
    else:
        print("cannot connect to sensor") #prints error message
    timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S") # to store time in hours, minutes and seconds
    data = [timeC, temperature, humidity,] # sequence of time, temperature and humidity data respectively into csv file 
    
    with open(csvfile, "a")as output:
        writer = csv.writer(output, delimiter=",", lineterminator = '\n')  #
        writer.writerow(data) #to store the data to csv file
        sleep(6) #sleep for 6 seconds
    str = '' 
    try:
        str = serialPort.readline().decode().strip() #read data from serial port 
        if str.find('GGA') > 0: #find string "GGA"
            msg = pynmea2.parse(str) #
            print('Lat:',round(msg.latitude,6),'Lon:',round(msg.longitude,6),'Alt:',msg.altitude,'Sats:',msg.num_sats) #printing latitude and longitude msgs 
        timeC2 = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S") #storing time in hours, minutes and seconds in timec2 variable
        data2 = [timeC2, round(msg.latitude,6), round(msg.longitude,6)] #storing timec2, latiude and longitude to data2 variable
        with open(csvfile2, "a")as output:
            writer2 = csv.writer(output, delimiter=",", lineterminator = '\n') #
            writer2.writerow(data2) #to store the data to csv fil
            sleep(6) #sleep for 6 seconds
    except:
        print("error")
    while True:
        i=GPIO.input(11) #first PIR sensor connected to pin 11
        j=GPIO.input(13) #second PIR sensor connected to pin 13
        if i==0 or j==0:                 #When output from motion sensor is LOW
            camera.stop_preview() #camera stops working
            print("No motion",j) # prints no motion
            sleep(3) # sleeps for 3 seconds
            break
        if i==1 and j==1:               #When output from motion sensor is HIGH
            camera.start_preview() #camera starts working
            camera.capture('/home/pi/Desktop/final_iot_folder_final/frame%03d.gif'%frame) # saves the captured image to local folder
            frame = frame + 1 #increments the frame to save different images
            print("motion detected",i) #prints motion detected
            sleep(3) #sleeps for 3 secs