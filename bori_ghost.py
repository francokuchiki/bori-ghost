import discord
import listas
import os

TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event
async def on_ready():
	invitacion = "Invitación: https://discordapp.com/api/oauth2/authorize?client_id={}&permissions=469888071&scope=bot"
	print("Logged in as "+client.user.name, invitacion.format(client.user.id), sep="\n")

@client.event
async def on_server_join(servidor):
	for funcion in listas.evs["entra_servidor"]:
		await funcion(client, servidor)

@client.event
async def on_member_join(miembro):
	if hasattr(miembro.server, "id"): #Si es un servidor
		for funcion in listas.evs["entra_miembro"]:
			await funcion(client, miembro)

@client.event
async def on_message(message):
	if hasattr(message.server, "id"):
		for funcion in listas.evs["por_mensaje"]:
			await funcion(client, message)

@client.event
async def on_reaction_add(reaction,user):
	if hasattr(message.server, "id"):
		for funcion in listas.evs["pone_reaccion"]:
			await funcion(client,reaction,user)

@client.event
async def on_reaction_remove(reaction,user):
	if hasattr(message.server, "id"):
		for funcion in listas.evs["quita_reaccion"]:
			await funcion(client,reaction,user)

@client.event
async def on_error(event, *args, **kwargs):
	for funcion in listas.evs["en_error"]:
		await funcion(client,event,args[0])

if __name__ == "__main__":
	for tarea in listas.tasks:
		client.loop.create_task(tarea(client))
	client.run(TOKEN)