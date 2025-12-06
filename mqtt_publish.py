import paho.mqtt.client as mqtt
import time

BROKER = "192.168.0.110"    
PORT = 1883
USERNAME = "durgareddy"     
PASSWORD = "Durga@1291"  

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

try:
    client.connect(BROKER, PORT, 60)
    print("Connected to MQTT broker")
except Exception as e:
    print("Connection error:", e)
    exit()

while True:
    temperature = 25
    humidity = 65
    light = 120

    client.publish("home/sensor/temperature", temperature)
    client.publish("home/sensor/humidity", humidity)
    client.publish("home/sensor/light", light)

    print(f"Sent → Temp: {temperature}, Humidity: {humidity}, Light: {light}")

    time.sleep(5)
