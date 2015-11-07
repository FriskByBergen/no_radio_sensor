# Arduino and RPi connected by USB

If the sensors are to be connected close to a power supply an Arduino and RPi can be connected by USB for transferring of data.

The sensors are as follows:

* Sharp dust sensor from DRRobot
* DHT22 temperature and humidity sensor from DFRobot
* Gas sensor V2 from DFRobot

The Arduino board is the Romeo V2.2 from DFRobot. The RPi is a standard RPi running standard Raspian OS. The Arduino and RPi are connected by USB cable.

In order to make the RPi start the Python program automatically it is advised to configure the RPi to run the python script as a service. In this way you power up the RPi and will run the script! 
A good instruction to how to do it is found at:
http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/




