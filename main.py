# coding: UTF-8
#
# main.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
## Standard or extension modules
import discord
from json import loads
import signal
from re import sub
## Original modules
import dcommands
from dcommands import DiscordVClients


# Object instantiation and variable definition
client = discord.Client()


# Config file reading
fp = open("conf.json", "r")
CONF = loads(fp.read())
fp.close()
BOT_TOKEN = CONF["token"]
COM_PREFIX = CONF["prefix"]
MUSIC_PATH = CONF["music_dir"]
MUSIC_PATH_CL = CONF["music_close"]


# Connection ready event
@client.event
async def on_ready():
  # Message of ready in console
  print("Ready to play.")
  print("Music dir  : %s" % MUSIC_PATH)
  print("Music close: %s" % MUSIC_PATH_CL)

  # Status set
  await client.change_presence(activity=discord.Game(name=F"To get help: {COM_PREFIX} h"))

  # Quit
  return


# Message receiving event
@client.event
async def on_message(message: discord.Message):
  # Ignore bot messages
  if message.author.bot:
    return

  # String processing
  com = message.content
  com = sub("^ +", "", com)
  com = sub(" +", " ", com)
  com = sub(" +$", "", com)
  com = message.content.split(" ")

  # Ignore non command message
  if com[0] != COM_PREFIX:
    return

  # When no subcommand
  if len(com) == 1:
    await dcommands.help(message, client.user.name, COM_PREFIX)
    return

  # Command call
  if com[1] == "h" or com[1] == "help":
    await dcommands.help(message, client.user.name, COM_PREFIX)
  elif com[1] == "c" or com[1] == "connect" or com[1] == "p" or com[1] == "play":
    await dcommands.play(message, discordVClients, com)
  elif com[1] == "dc" or com[1] == "disconnect" or com[1] == "st" or com[1] == "stop":
    await dcommands.stop(message, discordVClients)
  elif com[1] == "v" or com[1] == "volume":
    await dcommands.volume(message, discordVClients, com)
  elif com[1] == "sk" or com[1] == "skip":
    await dcommands.skip(message, discordVClients)
  elif com[1] == "i" or com[1] == "info":
    await dcommands.info(message, discordVClients)
  elif com[1] == "cl" or com[1] == "close" or com[1] == "r" or com[1] == "rest":
    await dcommands.close(message, discordVClients, com)
  else:
    await message.reply(F":stop_sign: Unknown subcommand `{com[1]}`.")

  # Quit
  return


# Run
discordVClients = DiscordVClients(MUSIC_PATH, MUSIC_PATH_CL, 0.03)
signal.signal(signal.SIGALRM, discordVClients.trigPlay)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
client.run(BOT_TOKEN)
