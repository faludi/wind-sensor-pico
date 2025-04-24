from wifi_network import WiFi
from thingspeak import ThingSpeakApi
from time import sleep
from machine import Pin, ADC

status_led = Pin("LED", Pin.OUT)
status_led.on()
sleep(0.5)
status_led.off()

#Sensor Initialization
wind = ADC(26)

#ThingSpeak Initialization
thingspeak = ThingSpeakApi()

#Network Initialization
network = WiFi()
ip = network.connect()

#Main Program
while True:
    wind = wind.read_u16() # type: ignore
    print("Wind level:", wind)
    thingspeak.write_single_field(wind)
    status_led.on()
    sleep(0.1)
    status_led.off()
    sleep(16)