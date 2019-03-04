import discord
import random
import configparser
import asyncio

import sys, traceback

from discord.ext.commands import Bot
from discord import Game

BOT_PREFIX='$'

cfg = configparser.ConfigParser()
cfg.read('config.cfg')

client = Bot(command_prefix=BOT_PREFIX)

ext = ['owner', 'werewolf']
if __name__ == '__main__':
    for i in ext:
        try:
            client.load_extension(i)
        except Exception as e:
            print(f"Failed to load extension {i}.", file=sys.stderr)
            traceback.print_exc()

@client.event
async def on_ready():
    random.seed()
    await client.change_presence(game=Game(name="osu!"))
    print('Logged in.')
    print('----------')

#Says hi back
@client.command(name = 'hello',
                description = 'Says hello back.',
                brief = 'A simple greeting.',
                aliases = ['hi', 'gn', 'gm']),
                pass_context = True)
async def hello(ctx):
    await client.say(f"Hello, {ctx.message.author.mention}.")
