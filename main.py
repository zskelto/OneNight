import discord

TOKEN = 'NDU5ODExOTY1ODY3NjU1MTY4.DlSdKw.XMHT8u93bcUSlr_dWudh8j6qevc'

client = discord.Client()

@client.event
async def on_message(message):
	
	#Bot should not reply to itself
	if message.author == client.user:
		return
	
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
