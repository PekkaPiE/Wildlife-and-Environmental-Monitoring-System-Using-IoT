# Wildlife & Environmental Monitoring System Using IoT

In this project, I have introduced a couple of systems in which one is used for detecting changes
in its surrounding like motion PIR (passive Infrared) sensors and immediately captures the photograph 
whenever it detects a motion in front of the camera. The environmental conditions of the surroundings 
can also be monitored using this device like the Temperature and Humidity of the surroundings all the time. 
The location of the device can be monitored using the GPS module. The location of this device can also be 
viewed on Google Maps. 

The sensor data collected from the DHT11 sensor, data from the GPS module, and the 
image captured when motion is detected can be viewed in the local GUI created using the python library 
guizero. The details regarding the components used for developing the device, dependencies installed and 
library used have been discussed.

![image](https://user-images.githubusercontent.com/108731838/183908623-b2107176-bcc6-4ee9-a008-16fe50a33d74.png)



                                    **COMPONENTS USED IN THIS PROJECT**

(A) Raspberry Pi 3 B+

The Raspberry Pi is a minimal expense, Visa estimated PC that plugs into a PC screen or TV, and utilizations 
a standard console and mouse. A skilled little gadget empowers individuals, all things considered, to 
investigate registering and to figure out how to program in dialects like Scratch and Python. It can do all 
that you'd anticipate that a personal computer should do, from perusing the web and playing top quality video,
to making bookkeeping sheets, word-handling, and messing around. The Raspberry Pi can collaborate with the 
rest of the world and has been utilized in a wide exhibit of computerized creator projects, from music 
machines & parent finders to weather conditions stations and tweeting bird enclosures with infra-red cameras.

![image](https://user-images.githubusercontent.com/108731838/183886472-f554e39c-09ed-4348-b2d5-42554535a8a2.png)


(B) PIR Motion Sensor

PIR sensors permit you to detect movement, quite often used to identify whether a human has moved in or out 
of the sensors range. They are little, modest, low power, simple to utilize, and don't break down. Thus, they 
are normally found in apparatuses and devices utilized in homes or organizations. They are frequently alluded 
to as PIR, "Inactive Infrared", "Pyroelectric", or "IR movement" sensors.

PIR Motion Sensor has 3 pins:

•	Vcc: It powers the sensor module, typically +5 volt.

•	GND: It connects the module to the ground. 

•	Data: We can get the digital output from this pin, it is a single wire 2 way pin and is used for communication with the sensor.

![image](https://user-images.githubusercontent.com/108731838/183886943-18f717b4-e211-4b39-b05f-9679dc5e6106.png)

(C) DHT-11 Temperature and Humidity Sensor

DHT-11 Temperature & Humidity Sensor features a temperature & humidity sensor complex with a calibrated digital 
signal output. By using the exclusive digital-signal-acquisition technique and temperature & humidity sensing 
technology, it ensures high reliability and excellent long-term stability. This sensor includes a resistive-type 
humidity measurement component and an NTC temperature measurement component, and connects to a high-performance 
8-bit microcontroller, offering excellent quality, fast response, anti-interference ability, and cost-effectiveness.

DHT-11 Sensor has 3 pins:

•	Vcc: It powers the sensor module, typically +5 volt.

•	GND: It connects the module to the ground. 

•	Data: We can get the digital output from this pin, it is a single wire 2 way pin and is used for communication with the sensor.

![WhatsApp Image 2022-08-10 at 4 43 09 PM](https://user-images.githubusercontent.com/108731838/183887722-647bd424-6200-430c-95e7-4bffbe8c06d6.jpeg)

(D) Ublox NEO-6M GPS Module

The NEO-6M GPS module is a well-performing total GPS collector with an inherent 25 x 25 x 4mm fired recieving 
wire, which gives areas of strength for a hunt capacity. With the power and sign pointers, you can screen the 
situation with the module. Because of the information reinforcement battery, the module can save the information 
when the principal power is closed down unintentionally. Its 3mm mounting openings can guarantee simple 
gathering on your airplane, which in this manner can fly consistently at a decent position, return to Home 
consequently, and programmed waypoint flying, and so on. Or on the other hand you can apply it on your 
savvy robot vehicle for programmed returning or going to a specific objective, making it a genuine "shrewd" bot!

Ublox NEO-6M GPS module has 4 pins:

•	Vcc: It powers the sensor module, typically +5 volt.

•	GND: It connects the module to the ground. 

•	Tx: Transmitter pin used in serial communication.

•	Rx: receiver pin used in serial communication.

![adi 2022-08-10 at 4 49 54 PM](https://user-images.githubusercontent.com/108731838/183889400-f16f6e91-c8a7-4247-be90-f85dac74a503.jpg)

(E) Raspberry Pi Night Vision Camera

My Raspberry Pi Night Vision Camera plugs straightforwardly into the CSI connector on the Raspberry Pi 
(requires a connector for use with a Pi Zero), and elements two focused energy Infrared LED spotlights for 
evening time recording! The IR LED's are fueled straightforwardly from the CSI port, and are fit for lighting 
a region a ways off of up to 8m! 

In testing, the best pictures were caught a good ways off of 3m to 5m. 
The camera additionally includes a movable 3.6mm central length focal point and 75.7 degree seeing point. 
This Raspberry Pi night vision camera involves a similar OV5647 as the standard Raspberry Pi camera, and is 
subsequently ready to convey a completely clear 5MP goal picture, or 1080p HD video recording at 30fps.

![image](https://user-images.githubusercontent.com/108731838/183889948-09c650d0-2781-4f9d-a9e7-97742b0f406e.png)


                                              **DEPENDENCIES INSTALLED**

* To Install Pip

      sudo apt-get install python-pip        // for python2
      sudo apt-get install python3-pip       // for python3
      
* To Install Python3

      sudo apt-get install python3           // python2 is installed Bydefault
      
* To Update/Upgrade packages

      sudo apt-get update
      sudo apt-get upgrade
      

      

For DHT-11 Temperature & Humidity Sensor
      
* Install Adafruit

      pip3 install adafruit-circuitpython-dht
      
* Install System Wide (required in some cases)

      sudo pip3 install adafruit-circuitpython-dht
      
* Install a Virtual environment 

      mkdir project-name && cd project-name
      python3 -m venv .venv
      source .venv/bin/activate
      pip3 install adafruit-circuitpython-dht
 
For NEO-6M GPS:
      
* Install Pynmea 2

      sudo pip install pynmea2
    
* Install one GPS software
    
      sudo apt-get install gpsd gpsd-clients python-gps minicom
* Modify the Serial Port 

      sudo nano /boot/cmdline.txt
      
      change with this path:
      
      dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
      
* Change the setting
      
      sudo nano /boot/config.txt
      
      and add these files:
      
      dtparam=spi=on
      dtoverlay=pi3-disable-bt
      core_freq=250
      enable_uart=1
      force_turbo=1
      init_uart_baud=9600
      
* Reboot 

      sudo reboot now
      
* Change the module to 9600
 
      stty -F /dev/ttyAMA0 9600
      
* Connect AMA0
      
      sudo killall gpsd
      sudo nano /etc/default/gpsd
      
* Then 
 
      DEVICES="/dev/ttyAMA0"
      
* At the end but not the least restart the software 

      sudo systemctl enable gpsd.socket
      sudo systemctl start gpsd.socket 
      sudo cgps -s

Setting up Raspberry PiCamera

* Write

      sudo raspi-config
      
* Select Interfacing Option--> Camera (Enable)--> Finish 

* Reboot 
 
      sudo reboot now
      
      
Step-By-Step Explanation of the Program is as follows:

![wda](https://user-images.githubusercontent.com/108731838/183928589-2f963224-c6b8-4d76-b565-088d9c0f4314.png)

At first libraries are imported  Adafruit_DHT as dht, for DHT-11 Sensor import matplot.pyplot as plt to plot charts, matplotlib.animation as activity to refresh 
the diagram continuously then we imported datetime as dt, from guizero we imported App, Text, TextBox, PushButton, Picture, Window and Box, RPI.GPIO as GPIO for 
GPIO pins, PiCamera from picamera, rest from time, sys, lastly sequential, time and pynmea2. Then, at that point, we will set GPIO.setwarning(False) after that 
we will set GPIO.setmode to be GPIO.BOARD, after this we will set up information and result pins for PIR Motion Sensor as 11 and 13 separately.

Then we will make a variable named outline and introduce its worth to be 0 then we will store PiCamera() in camera (as we are utilizing Pi Camera Module) and 
begin the camera with camera.start_preview(). After this we set dht11Pin to be 4 and figure and pivot is instated with the result of plt.subplot(1, 2) which makes 
a subplot likewise we made 4 exhibits to be specific xs, ys, xs2 and ys2 lastly introduced the port variable with the sequential port and set the baudrate to be 
9600 and break to be 0.5 and put away it in serialPort variable.

![sda](https://user-images.githubusercontent.com/108731838/183928061-8c8e1bb3-7a75-48ba-ac3a-01cf37b80af1.png)

We make two functions named close and close_window that will close the GUI and window respectively.

We will make the GUI named as IoT Project and set layout as grid and background as white, we will also make a window for image to show and make a button 
named close to close image window we kept the resolution of app to be full screen, the GUI will have the heading as SENSOR DATA and it will have all the buttons 
for showing temperature, humidity, GPS data, plotting the graph, show image, finally a close button to close GUI, every button in GUI is aligned using grid and 
app.display() is used to display the GUI. 

Our GUI will look as shown below:

![image](https://user-images.githubusercontent.com/108731838/183927527-07b7f0f5-1681-497d-a420-1f086f8c2961.png)

![image](https://user-images.githubusercontent.com/108731838/183924110-ecf19c4e-26ce-44b0-bf6f-29db7020952e.png)

After all the initialization we made a function named animate which will take i and the four arrays as the arguments, this function will store the data from DHT-11 
Sensor in humidity and temperature variables and will append the xs with present date and time and ys with humidity data stored in humidity variable similarly it 
will append xs2 with present date and time and ys2 with temperature data stored in temperature variable. Also it will limit the amount of values in the arrays to 
20 values and finally it will plot the data in arrays in two separate graphs named temperature and humidity. We also made another function named plot which will 
call animate function and will show and update the plots in real-time at an interval of every 1000 milliseconds. 

The graph is as shown below:

![image](https://user-images.githubusercontent.com/108731838/183924156-659a4cc1-6d4c-4b87-900d-cd82101af671.png)

![image](https://user-images.githubusercontent.com/108731838/183924915-7029b136-d9c2-47ad-bb23-fb6325f7f398.png)

For image capture on motion we made a function named img that will continuously check if the output from pin 13 and 11 are 1 at the same time or not using an 
infinite loop if it is same then it will on the camera and capture the image and store the image in the directory mentioned above also it will store the image in 
a variable named picture and will show it in another window, finally it will print motion detected in shell and sleep for 3 seconds, in case motion is not detected 
it will stop the camera and will display a warning message in GUI as No Motion Detected and will print No Motion in shell and will break. 

The image will be shown in GUI as follows:

![image](https://user-images.githubusercontent.com/108731838/183925147-71d2948e-6f4a-4387-97ef-2df145989d8c.png)

To show sensor data from DHT-11 Sensor another function named show_sensor_data is made, this function will simply store the data from sensor and display it on GUI 
using humidity_data.value. Similarly for GPS data another function is made named gps_info which when called will continuously check if the data in str contains 
GGA value or not if it contains that then it will store latitude and longitude data in variable named msg and round it to 6 decimal places and store it in gps 
variable and finally append the data to GUI when button is pressed. If all this does not happen it will print error and will break the loop. 

The humidity, temperature and GPS (Latitude & Longitude) data will be displayed in GUI as follows:

![image](https://user-images.githubusercontent.com/108731838/183926325-df8bf44b-e7b4-4fa0-b5d2-c1a01be2b82f.png)




                                           **The Final Project**

![ashu 2022-08-10 at 8 14 56 PM](https://user-images.githubusercontent.com/108731838/183932085-d2b16fce-7273-48ea-a7d3-0d683c7cf320.jpeg)





