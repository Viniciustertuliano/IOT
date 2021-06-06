#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep

TOPICO = "aulas/ads/si/ac3"

client = mqtt.Client()

client.connect("test.mosquitto.org", 1883, 60)

n = 0
while True:
    n += 1
    texto = "Bom dia {}".format(n)
    payload = texto.encode()
    client.publish(TOPICO, payload, qos=0)
    print(TOPICO+" "+payload.decode())
    sleep(5)