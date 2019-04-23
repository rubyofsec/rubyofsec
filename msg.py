# -*- coding: utf-8 -*-
#!/usr/bin/python3

# libs
import os, sys
import telepot
from chatterbot import ChatBot

# limpar
os.system("clear")

# api
api = "730100291:AAF-NfL2nLQZ3FEQFaMhVPiQLRjLul4HzWU"

# status
print("\n[+] MENSAGEIRO ONLINE [+]\n")

# receber msg
def receber(msg):
 _user = msg['from']['username']
 grupo = msg['chat']['id']
 _id = msg['from']['id']
 nome = msg['from']['first_name']
 titulo = msg['chat']['title']
 text = msg['text']
 if "/info" in text:
  print("\nO @{} digitou o comando (/info).\n".format(_user))
  tele.sendMessage(grupo, "Olá {}, bem-vindo(a) ao grupo: {}.\nSeu ID: {}\nSeu User: @{}".format(nome, titulo, _id, _user))
 elif "/cucu" in text:
  tele.sendMessage(grupo, "Me chamou senhor?")
 else:
  print("\n @{} : {}\n".format(_user, text))
  env = str(input(" Escreva: "))
  tele.sendMessage(grupo, env)


# entrelaçar
tele = telepot.Bot(api)
tele.message_loop(receber)

# manter on
while True:
 pass