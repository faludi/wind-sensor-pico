import time
from machine import ADC

wind = ADC(26)

while True:
    print("Wind level:", wind.read_u16())
    time.sleep(1)