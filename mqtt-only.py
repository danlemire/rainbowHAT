import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    txt = float(message.payload.decode("utf-8"))
    	
    print("message received " ,txt)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
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
client.loop_forever() #stop the loop
