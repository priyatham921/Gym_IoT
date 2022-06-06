import paho.mqtt.client as mqtt
import time

broker_address = "broker-cn.emqx.io"
connected = False
messageRecieved = False



def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("client is connected to broker\n")
        global connected
        connected = True
        
    else:
        print("client not connected")


def on_message(client, userdata, message):
    
    print("\n")
    #Trying to print time stamp 
    #print(time.time())
    topic = str(message.topic)
    msg = message.payload.decode("utf-8")
    print(topic + "  :  " + msg)
    #print(type(message.payload.decode("utf-8")))
    
    
    


print("creating new instance\n")
client = mqtt.Client("MQTT")
client.on_connect=on_connect

print("connecting to broker\n")
client.connect(broker_address)

client.on_message=on_message
client.loop_start()

print("subscribing to topic: ", "sensornode/livestream/#")
client.subscribe("sensornode/livestream/#")


while connected != True:
    time.sleep(0.01)

while messageRecieved != True:
    time.sleep(0.01)



client.loop_stop()

