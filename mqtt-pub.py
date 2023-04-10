

import paho.mqtt.client as mqtt

payload="Hello:
topic="IOT/test"
client = mqtt.Client()
client.connect('34.131.170.190',1883,60)
(rc,mid)=client.publish(topic,payload);
client.disconnect();
