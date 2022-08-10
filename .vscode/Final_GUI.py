# importing required libaries
import Adafruit_DHT as dht 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import *
import datetime as dt
from guizero import App,Text,TextBox,PushButton,Picture,Window,Box
import matplotlib.animation as animation
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import sys
import serial,time,pynmea2
import webbrowser

GPIO.setwarnings(False) #to avoid warnings from the GPIO
GPIO.setmode(GPIO.BOARD) # seting mode to GPIO.BOARD mode
GPIO.setup(11, GPIO.IN) #setting pin 11 as input pin
GPIO.setup(13, GPIO.IN) #setting pin 13 as input pin
frame = 0 # creating a global frame variable and intializing it to zero
camera = PiCamera() #creating camera object of Picamera
camera.start_preview()  #start running camera

dht11Pin = 4 #DHT11sensor is connected to pin 7 or GPIO 4
figure, axis = plt.subplots(1, 2) #to create two plots in a row
xs = [] #create x-axis array for humidty
ys = [] #create y-axis array for humidty
xs2 = [] #create x-axis array for temperature
ys2 = [] #create y-axis array for humidty

port = "/dev/serial0" #assigning serial0 port to port variable 
serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5) 
# This function is called periodically from FuncAnimation
def animate(i, xs, ys , xs2 , ys2): #in-built function to plot using array values

    humidity, temperature = dht.read_retry(dht.DHT11, dht11Pin)  #reading data from sensor
    humidity = ('{0:0.1f} %'.format(humidity)) #assigning humidity sensor value to humiity variable
    temperature = ('{0:0.1f} C'.format(temperature)) #assigning temperature sensor value to temperature variable
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f')) #append present date and time to x-axis array 
    ys.append(humidity) #append humidity values to humidity array 
    xs2.append(dt.datetime.now().strftime('%H:%M:%S.%f'))#append present date and time to x-axis array
    ys2.append(temperature)#append temperature values to humidity array 
    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]
    xs2 = xs2[-20:]
    ys2 = ys2[-20:]
    
    axis[0].plot(ys) #plot humidity graph
    axis[0].set_title("humidity")
    
    axis[1].plot(ys2) #plot temperature graph
    axis[1].set_title("temperature")

    
def plot(): # plot function to display graphs
    ani = animation.FuncAnimation(figure, animate, fargs=(xs, ys , xs2 , ys2), interval=1000)
    plt.show()

def img(): #function to get image when motion is detected
    while True:
        i = GPIO.input(11) # motion sensor connected to pin 11
        j = GPIO.input(13) #motion sensor connected to pin 13
        if i==1 and j==1: #only when both the moton sensors detects motion
            camera.start_preview()#turns on camera 
            image = camera.capture('/home/pi/Desktop/final_iot_folder_final/frame0.gif') #capture the image and save to local folder
            #frame = frame + 1
            picture=Picture(window,image="frame0.gif") #assigning captured image to picture 
            window.show() #displays the image window with captured image
            print("motion detected", i)
            sleep(3) #sleeps for 3 seconds
#             break
        else:
            camera.stop_preview() #when no motion detected camera stops working
            warning_message.value="No Motion Detected" #message to show when no motion is detected 
            print("No Motion")
            break
        
def show_sensor_data(): #functon to display sensor data
    humidity, temperature = dht.read_retry(dht.DHT11, 4) #reading tmperature and humidity from sensor and assigning to variables
    humidity_data.value= "Humidity : " + str(humidity)+" %"  #assigning humiity value to humidity_data variable
    temperature_data.value= "Temperature : " + str(temperature) +" C" #assigning temperature value to temperature_data variable

def gps_info(): #function to get latitude and longitude info
    #port = "/dev/serial0"
    #serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
    while True: 
        str = ''
        try:
            str = serialPort.readline().decode().strip() #to read the raw data, decode and strip it 
            if str.find('GGA') > 0: #to find the string "GGA"
                msg = pynmea2.parse(str) #assigning the str wih GGA to msg
                gps = round(msg.latitude,6),round(msg.longitude,6) #getting latitude and longitude info from msg
                latitude_longitude_info.append(gps)
        except:
            print("error")
        break    
def close():
    sys.exit() #function to close the gui
def close_window():
    window.hide() #function to close hide the image window 


app = App(title="IoT Project", layout="grid", bg="white") #creating app named IoT Project
window=Window(app,title="image") #creating image window in app
window.hide() #to hide the image window just after creating image window
close_window=PushButton(window,text="close",command=close_window) #close button to close the image window

app.full_screen=True #app is strethed to full screen
welcome_message = Text(app, text="SENSOR DATA", size=18, font="Times New Roman", color="#1c7db7",grid=[0,0,20,1]) #text that displays heading "sensor data"
humidity_data=Text(app,text="Humidity :", grid=[1,1,3,1]) #text that displays humidity and stretches to 3 colums and 1 row 
temperature_data=Text(app,text="Temperature : ",grid=[8,1,3,1]) #text that displays temperture and stretches to 3 colums and 1 row 
latitude_longitude_info=Text(app,text="Latitude, Longitude : ", grid=[1,2,5,1])
update_text_1= PushButton(app, command=plot,text="      plot temp and humid       ",grid=[0,3]) #button to plot temperature and humidiy graphs
sensor_data_2= PushButton(app, command=show_sensor_data, text="              sensor data              ", grid=[0,1]) # button to display temperture and humidity data 
show_image = PushButton(app, command = img, text = "             show image              ",grid=[0,4]) #button to display image when image is observed
warning_message=Text(app,grid=[1,4]) # message to show when no motion is observed
gpsinfo = PushButton( app, command = gps_info, text = "                  gps info                ",grid=[0,2]) #button to get latitude and longitude
close = PushButton(app, command = close, text = "                   close                   ",grid=[0,6]) #close button for gui
app.display() # display and open the gui app window