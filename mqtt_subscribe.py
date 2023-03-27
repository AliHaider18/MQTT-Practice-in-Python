import paho.mqtt.client as mqtt
import time

#Decoding the message
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
#Subscribe to Temperature 
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_end()
