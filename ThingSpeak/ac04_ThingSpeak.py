#!/usr/bin/env python3

#Abner de Melo Porto - 1800074
#Isabella Mota Franco - 1802189
#José Alves de Oliveira - 1902135
#Laura Tazue Tavares Chirazawa - 1900628
#Vinicius Tertuliano da Silva - 1901646

from time import sleep
import urllib.request
from random import randint
from urllib.request import Request
import urllib



chave = "6KW2476NSXRN2AA1"
chave_Tweet = "PS1GTQU45X6TUWJB"

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % chave
baseURL_Tweet = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update/"

def notification(num):
    status = "Valor randomico=" + str(num)
    data = urllib.parse.urlencode({"api_key" : chave_Tweet, "status": status})
    data = data.encode('ascii')
    response = urllib.request.urlopen(baseURL_Tweet,  data=data)
    print(response.read())

while True:
    num_rand = randint(20, 70)
    if num_rand > 50:
        notification(num_rand)
        conn = urllib.request.urlopen(baseURL + "&field1="+ str(num_rand))
        print(conn.read())
        print("Valor enviado: "+str(num_rand))
        conn.close()
        sleep(10)
