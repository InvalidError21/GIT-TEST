import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

led = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

mqttc = mqtt.Client()
mqttc.connect("192.168.119.94", 1883, 60)
mqttc.loop_start()
mqttc.subscribe("led")

def led_state(mqttc, userdata, message):
    if str(message.payload.decode("utf-8")) == "1":
        GPIO.output(led, 1)

    else:
        GPIO.output(led, 0)

while True:
    mqttc.on_message = led_state

GPIO.cleanup()
