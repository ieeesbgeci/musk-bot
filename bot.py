import os
import discord
from discord.ext import commands
#get required intents and also remember to enable privilaged intents : )
intents=discord.Intents.default()
intents.members = True
intents.reactions = True
#add command prefix and specify intents and instantiate bot :)
bot=commands.Bot(command_prefix="!",help_command=None,intents=intents)
#create environment variable named BOT_TOKEN and add the bot token
token=os.environ['BOT_TOKEN']
#add extension files from cog folder :)
bot.load_extension("cogs.greet")
#bot.load_extension("cogs.modi_talks")
#bot.load_extension("cogs.role")
#bot.load_extension("cogs.admin")
#run bot using bot token :)
bot.run(token)
