from machine import Pin, I2C

# PINOUT https://docs.micropython.org/en/latest/rp2/quickref.html

#i2c = I2C(0)   # default assignment: scl=Pin(9), sda=Pin(8)

# --- I2C 0 ---

# Pins SCL=2, SDA=1
#i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

# Pins SCL=7, SDA=6
#i2c0 = I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)

# Pins SCL=12, SDA=11
#i2c0 = I2C(0, scl=Pin(9), sda=Pin(8), freq=400_000)

# etc

# --- I2C 1 ---

# Pins unConFused:
# I2C1 SCL GPIO 3 = Pin 5
# I2C1 SDA GPIO 2 = Pin 4
i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=400_000)

# Pins SCL=10, SDA=9
#i2c1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

# Pins SCL=15, SDA=14
#i2c1 = I2C(1, scl=Pin(11), sda=Pin(10), freq=400_000)

# Pins SCL=20, SDA=19
#i2c1 = I2C(1, scl=Pin(15), sda=Pin(14), freq=400_000)

# Pins SCL=22, SDA=21
#i2c1 = I2C(1, scl=Pin(17), sda=Pin(16), freq=400_000)


print("Config:", i2c1)

devs = i2c1.scan()

if len(devs) == 0:
    print("Devices found: 0")
else:
    print("Total devices:", len(devs))
    for i in devs:
        print("-- Address:", hex(i))
