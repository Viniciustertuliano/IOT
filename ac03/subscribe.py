#!/usr/bin/env python3

# Abner de Melo Porto - 1800074
# Isabella Mota Franco - 1802189
# José Alves de Oliveira - 1902135
# Laura Tazue Tavares Chirazawa - 1900628
# Vinicius Tertuliano da Silva - 1901646

import paho.mqtt.client as mqtt

TOPICO = "aulas/ads/si/ac3"

def conectou(client, userdata, flags, rc):
    print("Conectado! Código recebido:"+str(rc))
    client.subscribe(TOPICO)


def chegou_mensagem(client, userdata, msg):
    v = msg.payload
    print(msg.topic+" "+v.decode())

client = mqtt.Client()
client.on_connect = conectou
client.on_message = chegou_mensagem

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
