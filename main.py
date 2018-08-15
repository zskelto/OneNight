import discord
import configparser
import asyncio
from discord.ext.commands import Bot
from discord import Game
BOT_PREFIX='$'

cfg = configparser.ConfigParser()
cfg.read('config.cfg')

#client = discord.Client()
client = Bot(command_prefix=BOT_PREFIX)

#Setup for One Night
class Player:
    username = " "
    team = " "
    role = " "
    action = " "

    def __init__(self, n, r):
        self.username = n
        self.role = role

InProgress=0

@client.command(name='hello',
		description='Says hello back.',
		brief='A simple greeting.',
		aliases=['hi', 'goodevening', 'goodmorning'],
		pass_context=True)
async def hello(context):
	await client.say("Hello " + context.message.author.mention)




#Playes a game of One Night Ultimate Werewolf.
@client.command(name='OneNight',
		description='Starts a game of One Night Ultimate Werewolf, 3 players are required.',
		brief='Plays a game of One Night.',
		aliases=['on','1-night','1_night','1n','onenight','one_night'],
		pass_context=True)
async def OneNight(context):
	
	#Checks if PM
	if context.message.server == None:
		await client.say("Game must be played in server")
		return
	
	#Checks to see if a Game is already in progress.
	#TODO Let the Game Run on Multiple Servers
	global InProgress
	SERVER=context.message.server
	if InProgress == 0:
		InProgress = 1
	else:
		await client.say("A game is already in progress")
		return
	#Notifies user the game is about to start.
	await client.say("Get ready for a game of One Night Ultimate Werewolf!")
	
	#Builds the player base.
	USERS = []
	await client.say("Type join to join the game.\nType start to start the game.\nType cancel to cancel the game.")
	cont = 1
	while cont == 1:
		msg = await client.wait_for_message(channel=context.message.channel)
		if msg.content == "join":
			storage=0
			i=0
			for i in USERS:
				if(msg.author.name == i.name):
					storage=1
			if storage==0:	
				USERS.append(msg.author)
				await client.say("Welcome to the game, " +  msg.author.name)
	 	
		elif msg.content == "start":
			
			if len(USERS) < 3:
				await client.say("There must be atleast 3 players, there are only " + str(len(USERS)) + ".")
			
			else:
				cont = 0
		
		elif msg.content == "cancel":
			await client.say("Game is canceled")
			InProgress=0
			return
	

	#Commences the Game
	Players=0
	Deck=0
	Werewolves=0
	Towns=0
	#Specify What Roles to Include.
	#Tanner
	Tanner=0
	#Werewolves
	Alpha=0
	Mystic=0
	Minion=0
	#Townies	
	Paranormal_Investigator=0
	Aura_Seer=0
	Robber=0
	Troublemaker=0
	Witch=0
	Drunk=0
	Doppelganger=0

	Players=len(USERS)
	Deck = Players + 3
	Werewolves = Deck/3
	Towns = Deck - Werewolves
	#Notifies the program that the game is over.
	InProgress=0



#@client.event
#async def on_message(message):
#	
#	#Bot should not reply to itself
#	if message.author == client.user:
#		return
#	
#	if message.content.startswith('!hello'):
#		msg = 'Hello {0.author.mention}'.format(message)
#		await client.send_message(message.channel, msg)



@client.event
async def on_ready():
	await client.change_presence(game=Game(name="Pokemon"))
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')



async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print("Current Servers:")
		for server in client.servers:
			print(server.name)
		await asyncio.sleep(600)



client.loop.create_task(list_servers())
client.run(cfg['Default']['token'])
