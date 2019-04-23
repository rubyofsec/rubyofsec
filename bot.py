# -*- coding: utf-8 -*-
#!/usr/bin/python3

# libs
import os, sys
import telepot
from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
#import wikipedia

# land do wiki
#wikipedia.set_lang("pt")

# limpar
os.system("clear")

bot = ChatBot('Connor')
#trainer=('chatterbot.trainers.ChatterBotCorpusTrainer')
#bot.set_trainer(ListTrainer)

f = open("palavras.txt", "r").readlines()
#bot.train('chatterbot.corpus.portuguese')
#bot.train('hacking')

# connect connor
api = "730100291:AAF-NfL2nLQZ3FEQFaMhVPiQLRjLul4HzWU"

# caracteres invalidos
#cara = ['$', '@', '%', '(', ')', '&', ']', '[', '|']
#cac = open("filtros.txt", "r").readlines()

# connor status
print("\n###########################################")
print("# [+] RubyOfSecurity | @RubyOfSec_bot [+]  #")
print("###########################################\n")
# receber mensagem
def receber(msg):
 grupo = msg['chat']['id']
 text = msg['text']
 titulo = msg['chat']['title']
 _id = msg['from']['id']
 nome = msg['from']['first_name']
 _user = msg['from']['username']
 if "/info" in text:
  tele.sendMessage(grupo, "Olá {}, bem-vindo(a) ao grupo: {}.\nSeu ID: {}\nSeu User: @{}".format(nome, titulo, _id, _user))
 #elif "/admins" in text:
 # tele.sendMessage(grupo, "Admins:\n@astrophysicist\n@OM3RPU5")
 elif "dark" in text:
  tele.sendMessage(grupo, "Você deseja algo? ")
 elif "/start" in text:
  tele.sendMessage(grupo, "Olá, {} tudo bem?".format(nome))
 elif "/rfs" in text:
  tele.sendMessage(grupo, "A central do meu desenvolvedor.")
 elif "/" in text:
  tele.sendMessage(grupo, ":/")
 elif "/cucu" in text:
  tele.sendMessage(grupo, "Me chamou senhor?")
 elif "cc" in text:
  tele.sendMessage(grupo, "Se você e carder e procura por cc, saiba que você será preso")
 elif "top" in text:
  tele.sendMessage(grupo, "Sim")
 elif "* " in text:
  tele.sendMessage(grupo, "Nunca nem vi")
 elif "deus" in text:
  tele.sendMessage(grupo, "Deuses não existem")
 elif "Deus" in text:
  tele.sendMessage(grupo, "Deuses não existem")
 elif "@"  in text:
  print("Caracteres invalidos")
 elif "#"  in text:
  print("Caracteres invalidos")
 elif "$"  in text:
  print("Caracteres invalidos")
 elif "%"  in text:
  print("Caracteres invalidos")
 elif "&"  in text:
  print("Caracteres invalidos")
 elif "("  in text:
  print("Caracteres invalidos")
 elif ")"  in text:
  print("Caracteres invalidos")
 elif "~"  in text:
  print("Caracteres invalidos")
 elif "{"  in text:
  print("Caracteres invalidos")
 elif "}"  in text:
  print("Caracteres invalidos")
 elif "|"  in text:
  print("Caracteres invalidos")
 elif ":"  in text:
  print("Caracteres invalidos")
 elif ";"  in text:
  print("Caracteres invalidos")
 elif ">"  in text:
  print("Caracteres invalidos")
 elif "<"  in text:
  print("Caracteres invalidos")
 elif '"'  in text:
  print("Caracteres invalidos")
 elif "bot" in text:
  tele.sendMessage(grupo, "Me chamou?")
 elif "Bot" in text:
  tele.sendMessage(grupo, "Me chamou?")
 elif "robô" in text:
  tele.sendMessage(grupo, "Me chamou?")
 elif "Robô" in text:
  tele.sendMessage(grupo, "Me chamou?")
 else:
  resposta = bot.get_response(text)
  if float(resposta.confidence) > 0.5:
   tele.sendMessage(grupo, str(bot.get_response(text)))
   print("ID:{} NOME:{} MENSAGEM:{}\n".format(grupo, nome, text))
  else:
   tele.sendMessage(grupo, "Eu ainda não sei responder essa pergunta..")
   print("ID:{} NOME:{} MENSAGEM:{}\n".format(grupo, nome, text))

tele = telepot.Bot(api)
tele.message_loop(receber)

# manter online
while True:
 pass
