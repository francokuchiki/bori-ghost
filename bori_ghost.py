import discord
import listas

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

if __name__ == "__main__":
	for tarea in listas.tasks:
		client.loop.create_task(tarea(client))
	client.run("NDUyOTYxNTgzMzE2OTkyMDAw.DfX-pA.c8OkFlftDWIt3I8jR2Y9I7tRgyU")
