#!/usr/bin/env python
# coding: utf-8

# In[1]:


import paho.mqtt.client as mqtt

broker = input("IP do Broker: ")
print("Topics:")
print("temperatura")
print("pressao")
print("all")
message = input("Entrada: ")

def on_connect(client, userdata, flags, rc):
    print("Conectado! Código: "+str(rc))
    print("Tópico Escolhido: "+message)
    if (message == "temperatura"):
        print("(topic/temperatura)")
        client.subscribe("topic/temperatura")
    
    elif (message == "pressao"):
        print("(topic/pressao)")
        client.subscribe("topic/pressao")
        
    elif (message == "all"):
        print("(topic/#)")
        client.subscribe("topic/#")
    
    else:
        print("Nenhum topic com esse nome encontrado!")
        print("Desconectando")
        client.disconnect()
        

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    if msg.payload.decode() == "bye":
        print("Desconectando")
        client.disconnect()
    
    
client = mqtt.Client()
client.connect(broker,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()


# In[ ]:




