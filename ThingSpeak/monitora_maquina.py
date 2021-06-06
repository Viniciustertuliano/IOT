#!/usr/bin/env python3


from time import sleep
import sys
import http.client
import urllib.request
import subprocess
import psutil


# Chave de escrida deste canal
chave = '09YO59VRYDP77O7A'
# URL do canal
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % chave


def TempProcessador():
    #obtem informacao da frequencia do processador
    cur_tempcpu = "cat /sys/class/thermal/thermal_zone0/temp"
    tempcpu = subprocess.check_output(cur_tempcpu, shell=True)
    return float(tempcpu)/1000


#Funcao: obtem uso percentual da CPU
#Parametros: nenhum
#Retorno: % de uso da CPU.
def UsoCPU():
    #obtem informacao da freq do processador
    cur_uso_cpu = psutil.cpu_percent()
    return cur_uso_cpu


while True:
    temp_cpu = str(TempProcessador())
    uso_cpu = str(UsoCPU())
    # Envia dado para o thingspeak
    conn = urllib.request.urlopen(baseURL +
        "&field1="+str(temp_cpu)+
        "&field2="+str(uso_cpu))
    print (conn.read())
    
    # Fecha a conexao
    conn.close()
    sleep(5)
