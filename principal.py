# -*- coding: utf-8 -*-

import os
import sys
import matplotlib
import numpy as np
from PyQt5 import QtCore, QtGui, Qt, QtWidgets, uic
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('qt5Agg')
import images
#from digi.xbee.devices import XBeeDevice
#from digi.xbee.io import IOLine,IOMode
#from __future__ import print_function
# Python imports
#import http.client
#import time
#import urllib

recoleccion_datos= 200
sensor_presion= np.random.rand(recoleccion_datos)
sensor_etiquetado= np.random.rand(recoleccion_datos)
sensor_nivel= np.random.randint(0, 1000, recoleccion_datos)
sensor_temperatura= np.random.randint(0, 100, recoleccion_datos)



class principal (QtWidgets.QMainWindow):
  
    def __init__(self):
        super (principal, self).__init__()
        uic.loadUi('principal.ui',self)
                  
        #self.Adquisicion.clicked.connect(self.AD)                  
        self.sensor_presion.clicked.connect(self.a)
        self.sensor_etiquetado.clicked.connect(self.b)
        self.sensor_nivel.clicked.connect(self.c)
        self.sensor_temperatura.clicked.connect(self.d)
        self.Datos()
        self.BOTON_LED.clicked.connect(self.e)

#    def AD(self):        
#        # Serial port on Raspberry Pi
#        SERIAL_PORT = "/dev/ttyUSB0"  # "/dev/ttyS0"
#        # BAUD rate for the XBee module connected to the Raspberry Pi
#        BAUD_RATE = 9600
#        # The name of the remote node (NI)
##        REMOTE_NODE_ID = "TMP36"
##        # Analog pin we want to monitor/request data
#        ANALOG_LINE = IOLine.DIO3_AD3
#        # Sampling rate
#        SAMPLING_RATE = 15
#        # Get an instance of the XBee device class
#        device = XBeeDevice(SERIAL_PORT, BAUD_RATE)
#
#        # Method to connect to the network and get the remote node by id
#        def get_remote_device():
#           """Get the remote node from the network 
#           Returns:
#           """
#           # Request the network class and search the network for the remote node
#           xbee_network = device.get_network()
#           remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
#           if remote_device is None:
#              print("ERROR: Remote node id {0} not found.".format(REMOTE_NODE_ID))
#              exit(1)
#           remote_device.set_dest_address(device.get_64bit_addr())
#           remote_device.set_io_configuration(ANALOG_LINE, IOMode.ADC)
#           remote_device.set_io_sampling_rate(SAMPLING_RATE)
#
#        def io_sample_callback(sample, remote, time):
#           print("Reading from {0} at {1}:".format(REMOTE_NODE_ID, remote.get_64bit_addr()))
#           # Get the temperature in Celsius
#           temp_c = ((sample.get_analog_value(ANALOG_LINE) * 1200.0 / 1024.0) - 500.0) / 10.0
#           # Calculate temperature in Fahrenheit
#           temp_f = ((temp_c * 9.0) / 5.0) + 32.0
#           print("\tTemperature is {0}C. {1}F".format(temp_c, temp_f))
#           # Calculate supply voltage
#           volts = (sample.power_supply_value * (1200.0 / 1024.0)) / 1000.0
#           print("\tSupply voltage = {0}v".format(volts))
#
#        try:
#           print("Welcome to example of reading a remote TMP36 sensor!")
#           device.open() # Open the device class
#           # Setup the remote device
#           get_remote_device()
#           # Register a listener to handle the samples received by the local device.
#           device.add_io_sample_received_callback(io_sample_callback)
#           while True:
#               pass
#        except KeyboardInterrupt:
#           if device is not None and device.is_open():
#              device.close()
#        
#        # API KEY
#        THINGSPEAK_APIKEY = 'ILDHV1W21A9NOEMZ'
#        print("SE GRAFICA LA MEDICION DE SENSORES UTILIZADOS EN LA PRODUCCION DEL LADRILLO")
#        try:
#          while 1:
#             # Get temperature in Celsius
#             temp_c = ((500 * 3.30) - 0.5) * 10
#             # Calculate temperature in Fahrenheit
#             temp_f = (temp_c * 9.0 / 5.0) + 32.0
#             # Display the results for diagnostics
#             print("Uploading {0:.2f} C, {1:.2f} F" "".format(temp_c, temp_f), end=' ... ')
#             # Setup the data to send in a JSON (dictionary)
#             params = urllib.parse.urlencode(
#                  {
#                     'field1': temp_c,
#                     'field2': temp_f,
#                     'key': THINGSPEAK_APIKEY,
#                  }
#             )
#             # Create the header
#             headers = { "Content-type": "application/x-www-form-urlencoded", 'Accept': "text/plain"}
#             # Create a connection over HTTP
#             conn = http.client.HTTPConnection("api.thingspeak.com:80")
#             try:
#                 # Execute the post (or update) request to upload the data
#                 conn.request("POST", "/update", params, headers)
#                 # Check response from server (200 is success)
#                 response = conn.getresponse()
#                 # Display response (should be 200)
#                 print("Response: {0} {1}".format(response.status,response.reason))
#                 # Read the data for diagnostics
#                 data = response.read()
#                 conn.close()
#             except Exception as err:
#                 print("WARNING: ThingSpeak connection failed: {0}, " "data: {1}".format(err, data))
#             # Sleep for 20 seconds
#             time.sleep(20)
#        except KeyboardInterrupt:
#            print("Thanks, bye!")
#        exit(0)
        
        
    def Datos(self):
        
        data = []
        with open ("./datos_taller.txt", "r") as file:
            for line in file:
                line_data = line.strip().split()
                data.append(line_data)
        
        self.Tabla.setColumnCount(len(data[0]))
        self.Tabla.setRowCount(len(data))
        
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.Tabla.setItem(i, j, QtWidgets.QTableWidgetItem(item))
    
    def a(self):
            x= np.arange(1,201,1)
                    
            plt.plot(x, sensor_presion, linestyle='-', markerfacecolor='red')
            plt.xlabel('Tiempo (t)')
            plt.ylabel('Distancia (m)')
            plt.grid(True)
            plt.show()
        
    def b(self):
           x= np.arange(1,201,1)
           
           plt.plot(x, sensor_etiquetado,linestyle='-', markerfacecolor='yellow') 
           plt.xlabel('Tiempo(t)')
           plt.ylabel('Velocidad (km/h)')
           plt.grid(True)
           plt.show()
        
    def c(self):
          x= np.arange(1,201,1)
         
          plt.plot(x, sensor_nivel,linestyle='-', markerfacecolor='blue') 
          plt.xlabel('Tiempo (s)')
          plt.ylabel('Peso(Kg)')
          plt.grid(True)
          plt.show()
    def d(self):
          x= np.arange(1,201,1)
                  
          plt.plot(x, sensor_temperatura,linestyle='-', markerfacecolor='red') 
          plt.xlabel('Tiempo (t)')
          plt.ylabel('Temperatura(°C)')
          plt.grid(True)
          plt.show()
          
    def e(self):
         # Pin assignments
         import  RPi.GPIO as GPIO
         LED_PIN = 7
         BUTTON_PIN = 17
         # Setup GPIO module and pins
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(LED_PIN, GPIO.OUT)
         GPIO.setup(BUTTON_PIN, GPIO.IN)
         # Set LED pin to OFF (no voltage)
         GPIO.output(LED_PIN, GPIO.LOW)
         try:
             # Loop forever
             while 1:
                 # Detect voltage on button pin
                 if GPIO.input(BUTTON_PIN) == 1:
                 # Turn on the LED
                    GPIO.output(LED_PIN, GPIO.HIGH)
                 else:
                   # Turn off the LED
                   GPIO.output(LED_PIN, GPIO.LOW)
         except KeyboardInterrupt:
             print('error')
         finally:
             GPIO.cleanup()
                  
def main():
        print('inicia')
        app=QtWidgets.QApplication(sys.argv)
        ventana=principal()
        ventana.show()
        sys.exit(app.exec_())
    
if  __name__=="__main__":
      main()   