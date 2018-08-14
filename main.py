import discord

TOKEN = 'NDU5ODExOTY1ODY3NjU1MTY4.DlSdKw.XMHT8u93bcUSlr_dWudh8j6qevc'

client = discord.Client()

#Setup for One Night
class Player:
    username = " "
    team = " "
    role = " "
    action = " "

    def __init__(self, n, r):
        self.username = n
        self.role = role

#Determines the Player Base.
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
