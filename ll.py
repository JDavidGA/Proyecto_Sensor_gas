import network, time, urequests

from machine import Pin, I2C, ADC
from utime import sleep

sensorG = ADC(Pin(39))


def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect('RedMiHugo', '12345678')         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True

if conectaWifi("RedMiHugo", "12345678"):
    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    url = "https://maker.ifttt.com/trigger/sonido/with/key/kL1ivfciS0Dyd-lVIT8qtEKQfTafto-HkecXapfUdiS?"
 
while True:
    
    
    sleep(0.5)
    lectura= int(sensorG.read_u16())
    print( "Nivel de sonido = {:02}".format(lectura))
   
    
    if lectura > 500:
        respuesta = urequests.get(url+"&value2="+str(lectura))
        print (respuesta.status_code)
        respuesta.close ()
         
    
    
    