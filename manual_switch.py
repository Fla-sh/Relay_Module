import RPi.GPIO as GPIO

def change(pin):
    GPIO.output(pin, not GPIO.input(pin))
    print("Changed pin no. {}".format(pin))
    print("New state is: {}".format(str(GPIO.input(pin))))


def setup():
    print(GPIO.VERSION)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(list(range(1, 28)), GPIO.OUT)
    GPIO.output(list(range(1, 28)), GPIO.HIGH)

setup()
print(type(range(1,28)))
while True:
    chanel = int(input("Chanel number: "))
    change(chanel)

