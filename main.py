from wifi_network import WiFi
from thingspeak import ThingSpeakApi
from time import sleep
from machine import Pin, ADC

status_led = Pin("LED", Pin.OUT)
status_led.on()
sleep(0.5)
status_led.off()

upload_interval = 16 # seconds
num_samples = 128 # number of samples to average

#Sensor Initialization
wind_sensor = ADC(26)

#ThingSpeak Initialization
thingspeak = ThingSpeakApi()

#Network Initialization
network = WiFi()
ip = network.connect()

#Main Program
while True:
    samples= []
    for sample in range (num_samples):
        wind = wind_sensor.read_u16() # type: ignore
        print("wind:", wind)
        samples.append(wind)
        sleep(upload_interval/num_samples)
    thingspeak.write_single_field(sum(samples)/len(samples))
    print("Wind Upload:", sum(samples)/len(samples))
    status_led.on()
    sleep(0.1)
    status_led.off()


    