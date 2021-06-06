#!/usr/bin/env python3

from time import sleep
import sys
import http.client
import urllib.request

# Chave de escrida deste canal
chave = '09YO59VRYDP77O7A'
# URL do canal
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % chave
# Envia dado para o thingspeak
conn = urllib.request.urlopen(baseURL + "&field1="+str(15))
print (conn.read())
# Fecha a conexao
conn.close()
sleep(15)


# Envia dado para o thingspeak
conn = urllib.request.urlopen(baseURL + "&field1="+str(20))
print (conn.read())
# Fecha a conexao
conn.close()
sleep(15)
# Envia dado para o thingspeak
conn = urllib.request.urlopen(baseURL + "&field1="+str(5))
print (conn.read())
# Fecha a conexao
conn.close()
sleep(15)
