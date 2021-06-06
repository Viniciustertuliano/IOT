#!/usr/bin/env python3

#Abner de Melo Porto - 1800074
#Isabella Mota Franco - 1802189
#José Alves de Oliveira - 1902135
#Laura Tazue Tavares Chirazawa - 1900628
#Vinicius Tertuliano da Silva - 1901646

import time
import random
import telepot
import requests
import json


def opcoes(msg):
    chat_id = msg['chat']['id']
    commando = msg['text']
    print(str(random.choice(menssagens)))
    if commando == "/temp":
        bot.sendMessage(chat_id, temp())
    elif commando == "/frase":
        bot.sendMessage(chat_id,random.choice(menssagens))
    elif commando == "/cep":
        bot.sendMessage(chat_id, cep())
    print("to esperando...")



def temp():
    temp = requests.get("https://api.hgbrasil.com/weather?woeid=455827")
    aux = json.loads(temp.content)
    return 'A temperatura atual na cidade de {} é de {}°C'.format(aux['results']['city_name'],
                                                                aux['results']['temp'])


def cep():
    cep = requests.get('https://brasilapi.com.br/api/cep/v2/05889190')
    aux = json.loads(cep.content)
    return 'Rua {}, {}, {} - {}'.format(aux['street'][27:], 
                                        aux['neighborhood'],
                                        aux['city'],
                                        aux['state'])



menssagens = ["Vamos nessa!", "Já acabou, Jéssica?", "Cachorro? Que cachorro o quê! Eu não sou cachorro, não!" ]
mensagem = random.choice(menssagens)
bot = telepot.Bot('1836010764:AAEZQWCCu7uW2rldUXGQjovdGkPCZBSQWF8')
bot.message_loop(opcoes)
print("to esperando...")
while True:
    time.sleep(10)
