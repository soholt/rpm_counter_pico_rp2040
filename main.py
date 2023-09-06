from machine import Pin
import time

# uncomment for OLED SSD1306 display (remove all 3 single quotes ''')
'''
from machine import I2C # https://docs.micropython.org/en/latest/rp2/quickref.html
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000) # set i2c display pins

WIDTH  = 128
HEIGHT = 32

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.text(" -- GIN LAB --", 4, 16) # <-- add your tt name
oled.show()
'''

led = machine.Pin("LED", machine.Pin.OUT)
ir_vcc = Pin(5, Pin.OUT, value=1) # using this pin to power infrared led (can connect it to 3.3v directly)
rpm_pin = Pin(6, Pin.IN, Pin.PULL_UP) # or Pin.PULL_DOWN # enable internal pull-up resistor

rpm_laps = 0

rpm_start = time.ticks_us() # get microseconds

def rpm_calc():
    global rpm_start, rpm_laps, wow_data, enc_ticks
    
    delta_usec = time.ticks_diff(time.ticks_us(), rpm_start) # compute time difference
    rpm_start = time.ticks_us() # note new time
    
    led.on()
    delta_sec = delta_usec / 1000000
    rpm = 60 / delta_sec
    
    if rpm > 80 or rpm < 30: # 0 if out of range
        rpm = 0
        
    rpm_display = "{speed:.5f}" # add zeros to the end
    print("rpm", rpm_display.format(speed=rpm))
    
    # uncomment for OLED SSD1306 display
    '''
    oled.fill(0) # adjust number of lines and x,y text coords to your liking
    oled.text(" -- GIN LAB --", 4, 0) # <-- add your tt name
    oled.text(" LAP: " + str(rpm_laps), 4, 9)
    oled.text(" RPM: " + rpm_display.format(speed=rpm), 4, 17)
    oled.text(" WOW: 00.0000%", 4, 25)
    oled.show()
    '''
    
    rpm_laps += 1
    time.sleep_ms(33)
    led.off()
    
rpm_pin.irq(lambda t: rpm_calc(), Pin.IRQ_FALLING) # or Pin.IRQ_RISING

print("RPM counter started")
