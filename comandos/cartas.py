import discord
import random
from comandos.cartas_objetos import *

async def da_carta(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	servidor = discord.utils.get(client.servers, id = "310951366736609281")
	manos = [[],[]]
	for mano in manos:
		while len(mano) < 3:
			i = random.randint(0,39)
			if baraja[i] not in manos[0] and baraja[i] not in manos[1]:
				mano.append(baraja[i])
	mensaje = ""
	for carta in mano_1:
		emoji = discord.utils.get(servidor.emojis, name=carta.emoji)
		mensaje += str(emoji)
		print(mensaje)
	await client.send_message(message.channel, mensaje)
	await client.send_message(message.author, mensaje)