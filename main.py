import discord
import random
import math
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
class Role:
	RoleName = ""
	RoleTeam = "" 
	RoleEnable = 0
	
	def __init__(self,n,t,e):
		self.RoleName = n
		self.RoleTeam = t
		self.RoleEnable = e
		
class Player:
	PlayerInfo = discord.User()
	PlayerRole = Role("","",0)
	def __init__(self,pinfo,prole):
		self.PlayerInfo=pinfo
		self.PlayerRole=prole


def isint(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

InProgress=0
Players=0
Deck=0
Werewolves=0
DeckString=""	
prompt = ""
ROLES = []
RoleList = ["Doppleganger", "Werewolf", "Alpha Wolf", "Mystic Wolf", "Minion", "Paranormal Investigator", "Robber", "Troublemaker", "Witch", "Aura Seer", "Drunk", "Tanner"]
#Creates a list of roles
j = 0
while j < 12:
	if j == 0:
		ROLES.append(Role(RoleList[j],"Unknown",0))
	elif j>0 and j <5:
		ROLES.append(Role(RoleList[j],"Werewolves",0))
	elif j>4 and j <11:
		ROLES.append(Role(RoleList[j],"Village",0))		
	else:
		ROLES.append(Role(RoleList[j],"Tanner",0))
	j += 1
#Creates a printable list of roles.
j=1
for i in ROLES:
	prompt += str(j) + ". " + ROLES[j-1].RoleName + "\n"   
	j += 1	

#Says hi back.
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
			#for i in USERS:
			#	if(msg.author.name == i.name):
			#		storage=1
			if storage==0:	
				USERS.append(msg.author)
				await client.say("Welcome to the game, " +  msg.author.name)
	 	
		elif msg.content == "start":
			
			if len(USERS) < 3:
				await client.say("There must be atleast 3 players, there are only " + str(len(USERS)) + ".")
			
			else:
				await client.say("Starting game")
				cont = 0
		
		elif msg.content == "cancel":
			await client.say("Game is canceled")
			InProgress=0
			return
		

	#Commences the Game
	global Players
	global Deck
	Players=len(USERS)
	
	#Prepares Deck
	#Checks if there is a deck that can be reused
	reuse=0
	if Deck == Players+3:
		await client.say("A deck from a past game is available.\nWould you like to reuse previous deck?(y/n/cancel)")
		while reuse == 0:
			msg = await client.wait_for_message(channel=context.message.channel)	
			if msg.content == "y":
				reuse = 1
			elif msg.content == "n":
				reuse = 2
			elif msg.content == "cancel":
				await client.say("Game is canceled")
				InProgress = 0
				return
	#Important Variables
	global Werewolves
	global prompt
	global ROLES
	global DeckString
	#Creates custom deck:
	if reuse==0 or reuse==2:
		#Clears the Current Deck
		Deck=0
		Werewolves=0
		for i in ROLES:
			i.RoleEnable=0
		#Prompts the user for deck elements.
		await client.say("Type the number that corresponds to the role to add to the deck (or type cancel):\n" + prompt)
		#Builds Deck
		while Deck < Players+3:
			msg = await client.wait_for_message(channel=context.message.channel)
			if isint(msg.content):
				num = int(msg.content)
				if num>=1 and num<=12:
					if ROLES[num-1].RoleEnable == 1 and ROLES[num-1].RoleName != "Werewolf":
						await client.say(ROLES[num-1].RoleName + " is already in the deck(" + str(Deck) + "/" + str(Players+3) + ").")
					else:
						Deck += 1
						ROLES[num-1].RoleEnable = 1
						if(ROLES[num-1].RoleName == "Werewolf"):
							Werewolves += 1
						await client.say(ROLES[num-1].RoleName + " was added to the deck(" + str(Deck) + "/" + str(Players+3) + ").")
			elif msg.content == "cancel":
				await client.say("Game is canceled")
				InProgress=0
				return
		#DeckString will Contain the Contents of the deck created.
		DeckString = ""
		for i in ROLES:
			if i.RoleEnable == 1:
				if i.RoleName == "Werewolf":
					DeckString += i.RoleName + " x" + str(Werewolves) + "\n"
				else:
					DeckString += i.RoleName + "\n"
	#Displays the deck that will be used for the game
	await client.say("Contents of Deck:\n\n" + DeckString + "\nPrepare to play!")
	DeckIndex=[]
	j=0 
	while j < 12:
		if ROLES[j].RoleEnable == 1:
			if ROLES[j].RoleName == "Werewolf":
				k=0
				while k < Werewolves:
					DeckIndex.append(j)
					k+=1
			else:
				DeckIndex.append(j)
		j+=1
	
	#Assigns Roles to Users
	j=0
	ListofPlayers=[] 
	while j<Players:
		k = random.choice(DeckIndex)
		DeckIndex.remove(k)
		p_object = Player(USERS[j], ROLES[k])
		ListofPlayers.append(p_object) 
		j += 1
	#PM Players Their Roles
	for i in ListofPlayers:
		await client.send_message(i.PlayerInfo, "Your role is " + i.PlayerRole.RoleName + "\nYou side with the " + i.PlayerRole.RoleTeam)
	#Disperses the Rest of the Deck
	MiddleCards = []
	for i in DeckIndex:
		MiddleCards.append(ROLES[i])
	#Adds a wolf card if alpha is enabled
	WolfCard = Role(ROLES[1].RoleName, ROLES[1].RoleTeam, ROLES[1].RoleEnable)
	if ROLES[2].RoleEnable == 1:
		WolfCard.RoleEnable = 1
	else:
		WolfCard.RoleEnable = 0
	#Starts the game
	CurrentPlayer = discord.User()
	#First Role: Doppelganger
	if ROLES[0].RoleEnable == 1:
		find=0
		j=0
		while find == 0 and j < Players:
			if ListofPlayers[j].PlayerRole.RoleName == ROLES[0].RoleName:
				find = 1
				CurrentPlayer=ListofPlayers[j]
			else:
				j += 1
		if find == 1:
			description = "Select another player and you will become that player's role:\n"
			j=1
			for i in ListofPlayers:
				#if CurrentPlayer.PlayerInfo != i.PlayerInfo:
				description += str(j) + ". " + i.PlayerInfo.name + "\n"
				j += 1
			await client.send_message(CurrentPlayer.PlayerInfo, description)
			stop = False
			while stop != True:
				msg = await client.wait_for_message(author=CurrentPlayer.PlayerInfo)
				if isint(msg.content):
					num = int(msg.content)
					if num>0 & num<Players-1:
						stop=True
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
#		msg = '!hello {0.author.mention}'.format(message)
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
