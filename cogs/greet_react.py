from pydoc import describe
from turtle import color
from discord.ext import commands
import discord
import random

class g_r_mod(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.Cog.listener()
	#on ready function to display login :)
	async def on_ready(self):
		print(f"logged in as :: >> {self.bot.user.name}")

	
	@commands.Cog.listener()
	async def on_member_join(self,ctx,member):
		#welcomes new users to server :)
		channel=member.guild.system_channel
		cvalue = random.randint(0, 0xffffff)
		embed  = discord.Embed(description=f"Sangha Shathiyileeku swagatham {member} Mitramee",color=cvalue)
		file= discord.File("/app/files/pm_modi.jpg")
		embed.set_image(url="attachment://pm_modi.jpg")
		await ctx.send(embed=embed)

	# @commands.Cog.listener()
	# async def on_reaction_add(self,reaction,user):
	# 	#notify when users react to messages :)
	# 	channel=reaction.message.channel
	# 	async for user in reaction.users():
	# 		await channel.send(f"<{user.name}> gave reaction to user <{reaction.message.author.name}> with {reaction.emoji}")

	@commands.command()
	async def help(self,ctx):
		#send help message
		cvalue = random.randint(0, 0xffffff)
		embed = discord.Embed(title=" HELP ", description="Mem Modi ji Hum.Mere pyari Sangha_Vashiyoo.",color=cvalue)
		embed.add_field(name="!dwajapranamam",value="Mitrangale Ashirwadikkum", inline=False)
		await ctx.send(embed=embed)

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error): 
		if isinstance(error, commands.CommandNotFound): 
			await ctx.send("Command not found!")

	@commands.command()
	async def dwajapranam(self,ctx):
		cvalue = random.randint(0, 0xffffff)
		embed=discord.Embed(description="Dwajaprenam Mitramee :)")
		file= discord.File("/app/files/pranamam.png")
		embed.set_image(url="attachment://pranamam.png")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(g_r_mod(bot))	
		