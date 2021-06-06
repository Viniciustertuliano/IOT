#!/usr/bin/env python3

from time import sleep
import sys
import http.client
import urllib.request
import random


# Inicia a semente dos numeros pseudo randomicos
random.seed()


# Chave de escrida deste canal
chave = '09YO59VRYDP77O7A'
# URL do canal
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % chave


while True:
    valor = random.randint(0,50)
    # Envia dado para o thingspeak
    conn = urllib.request.urlopen(baseURL + "&field2="+str(valor))
    print (conn.read())
    print ("Valor enviado: "+str(valor))
    # Fecha a conexao
    conn.close()
    sleep(10)
