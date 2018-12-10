#!/usr/bin/env python
# coding: utf-8

# In[1]:


import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
loop = True
broker = input("IP do Broker: ")
while(loop):
    print("Comandos:")
    print("bye - desliga os subscribers")
    print("temp - inicia sensoriamento de temperatura")
    print("pres - inicia sensoriamento de pressao")
    message = input("Entrada: ")

    if (message == "temp"):
        i = 10
        client.connect(broker,1883,60)
        while(i > 0):
            client.publish("topic/temperatura", "Temperatura: 25°C")
            time.sleep(5)
            i = i-1
        client.disconnect()
        
    if (message == "pres"):
        i = 10
        client.connect(broker,1883,60)
        while(i > 0):
            client.publish("topic/pressao", "Pressão: 1 atm")
            time.sleep(5)
            i = i-1
        client.disconnect()

    elif (message == "bye"):
        client.connect(broker,1883,60)
        client.publish("topic/temperatura", "bye")
        client.publish("topic/pressao", "bye")
        client.disconnect()
        loop = False


# In[ ]:





# In[ ]:




