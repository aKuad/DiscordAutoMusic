# coding: UTF-8
#
# dcommands/help.py
#
# Author: aKuad
#
# Published with CC0 license
#

# Modules importing
import discord


# Messages definitions
HELP_MES_SCMD = \
"""`h           , help            ` Print this help
`c [vol]     , connect [vol]  ` Connect and start music playing
`                             ` (with setting volume to [vol])
`p [vol]     , play [vol]     ` - (same as `c`)
`dc          , disconnect     ` Stop music playing and disconnect
`st          , stop           ` - (same as `dc`)
`sk          , skip           ` Skip and play next music
`v [vol]     , volume [vol]   ` Print current volume or set volume to [vol]
`                             ` (accept from next music)
`i           , info           ` Print current music information
`cl [st] [ed], close [st] [ed]` Print current closed time or set closed time
`r [st] [ed] , rest [st] [ed] ` - (same as `cl`)"""

HELP_MES_CLTM = \
"""Between the time [st] to [ed], music will be play only closing music.
Argument format of [st] [ed] is `HH:MM`.
-- example: `!ncs cl 1:00 7:00`
To disable closing time, specify same time.
-- example: `!ncs cl 0:00 0:00`"""

HELP_MES = discord.Embed(title=":notebook: Help of :musical_note:", color=0xa3ff66)
HELP_MES.add_field(name=":desktop: Useage", value="`!ncs <sub command>`", inline=False)
HELP_MES.add_field(name=":page_with_curl: List of subcommands", value=HELP_MES_SCMD, inline=False)
HELP_MES.add_field(name=":u55b6: About closed time", value=HELP_MES_CLTM, inline=False)


# Function definitions
async def help(message: discord.Message, name: str):
  HELP_MES.title = ":notebook: Help of %s :musical_note:" % name
  HELP_MES.set_footer(text=name)
  await message.reply(embed=HELP_MES)
  return
