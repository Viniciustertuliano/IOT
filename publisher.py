#!/usr/bin/env python3

import paho.mqtt.client as mqtt

from time import sleep

TOPICO = "testes/segundo"

# cria um identificador baseado no id definido
client = mqtt.Client()

# conecta ao broker
client.connect("test.mosquitto.org", 1883, 60)

num = 0
while True:
    # codificando o payload
    num += 1
    st = "ola {}".format(num)
    payload = st.encode()

    # envia a publicação
    client.publish(TOPICO,payload,qos=0)
    print (TOPICO + " " + payload.decode())
    sleep(5)
