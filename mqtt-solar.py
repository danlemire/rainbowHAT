#!/usr/bin/env python
import colorsys
import paho.mqtt.client as mqtt #import the client1
import time
import rainbowhat as rh

RAINBOW_BRIGHTNESS = 255

HUE_LOW = 225
HUE_HIGH = 0

#this variable keeps things running until set to false by touching 'A'
running = True
txt = 0
@rh.touch.A.press()
def touch_a(channel):
    global running
    running = False


############
def on_message(client, userdata, message):
    global txt
    txt = float(message.payload.decode("utf-8"))
    print("message received " ,txt)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    rh.display.clear()
    rh.display.set_decimal(1, True)
    rh.display.print_float(txt)
    rh.display.show()
    set_rainbow(int(txt));

########################################

########################################
broker_address="192.168.1.4"
print("creating new instance")
client = mqtt.Client("zeroHAT") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("feeds/helloworld")
print("Publishing message to topic","feeds/helloworld")
client.publish("feeds/helloworld","OFF")
#time.sleep(20) # wait



try:
    while running:          	
        print("message received " ,txt)
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)
        rh.display.clear()
        rh.display.set_decimal(1, True)
        rh.display.print_float(txt)
        rh.display.show()
        set_rainbow(int(txt));
        
        #pressure = rainbowhat.weather.pressure()
        #set_rainbow(pressure)
        #rainbowhat.display.print_float(pressure)
        #rainbowhat.display.show()
        client.loop_forever() #stop the loop
        time.sleep(1)

except KeyboardInterrupt:
    pass


rainbowhat.display.clear()
rainbowhat.display.show()