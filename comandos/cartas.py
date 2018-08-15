import discord
import random
from comandos.cartas_objetos import *

async def da_carta(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	servidor = discord.utils.get(client.servers, id = "310951366736609281")
	if len(message.mentions) == 0:
		jugadores = (client.user, message.author)
	else:
		jugadores = (message.mentions[0], message.author)
	manos = [[],[]]
	while len(manos[1]) < 3:
		i = random.randint(0,39)
		i2 = random.randint(0,39)
		while i2 == i:
			i2 = random.randint(0,39)
		if baraja[i] not in manos[0]:
			manos[0].append(baraja[i])
		if baraja[i2] not in manos[1]:
			manos[1].append(baraja[i2])
	i = 0
	mensajes = [[],[]]
	while i < 1:
		mensajes[i] = ""
		for carta in manos[i]:
			emoji = discord.utils.get(servidor.emojis, name=carta.emoji)
			mensajes[i] += str(emoji)
		if jugadores[i] != client.user:
			await client.send_message(jugadores[i], mensajes[i])
		await client.send_message(message.channel, mensajes[i])
		i += 1