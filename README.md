#  Smart Home Automation Using MQTT + Home Assistant  
**Student:** PADALA DURGA PRASAD REDDY  
**Register No:** 42110929  

This project sends Temperature, Humidity, and Light sensor data from a Python MQTT script to Home Assistant.

---

##  Features  
✔ Custom MQTT sensors in Home Assistant  
✔ Python script publishing 3 sensor readings  
✔ Dashboard card displaying all sensor values  
✔ Extra custom sensor → **Light (lx)**  

---

##  MQTT Topics Used  
| Sensor | MQTT Topic |
|--------|-------------|
| Temperature | home/sensor/temperature |
| Humidity | home/sensor/humidity |
| Light | home/sensor/light |

---

##  Python Script  
Located in: `mqtt_publish.py`  
Publishes sensor values every 5 seconds using MQTT.

---

##  Screenshots  
- sensors.png — Home Assistant sensor readings  
- mqtt_output.png — Terminal MQTT publish output  

---

##  Extra Sensor Explanation  
The extra sensor added is **Light (lx)**.  
It measures illumination, useful for smart lighting automation.

---

##  Steps Followed  
1. Installed Home Assistant and MQTT broker  
2. Created custom sensors using MQTT topics  
3. Published values using Python  
4. Verified updates in Home Assistant  
5. Added dashboard card  
6. Collected screenshots   

---
##  Submission Contents  
- Python code  
- Screenshots  
- README documentation  
