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
-- example: `{} cl 1:00 7:00`
To disable closing time, specify same time.
-- example: `{} cl 0:00 0:00`"""


# Function definitions
async def help(message: discord.Message, name: str, prefix: str):
  mes = discord.Embed(title=F":notebook: Help of {name} :musical_note:", color=0xa3ff66)

  mes.add_field(name=":desktop: Useage",                     value=F"`{prefix} <sub command>`", inline=False)
  mes.add_field(name=":page_with_curl: List of subcommands", value=HELP_MES_SCMD, inline=False)
  mes.add_field(name=":u55b6: About closed time",            value=HELP_MES_CLTM.format(prefix, prefix), inline=False)

  mes.set_footer(text=name)

  await message.reply(embed=mes)
  return
