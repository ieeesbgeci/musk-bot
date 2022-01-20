from discord.ext import commands
class g_r_mod(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.Cog.listener()
	#on ready function to display login :)
	async def on_ready(self):
		print(f"logged in as :: >> {self.bot.user.name}")

	
	@commands.Cog.listener()
	async def on_member_join(self,member):
		#welcomes new users to server :)
		channel=member.guild.system_channel
		await channel.send(f"Sangha Shathiyileeku swagatham {member} Mitramee")

	@commands.Cog.listener()
	async def on_reaction_add(self,reaction,user):
		#notify when users react to messages :)
		channel=reaction.message.channel
		async for user in reaction.users():
			await channel.send(f"<{user.name}> gave reaction to user <{reaction.message.author.name}> with {reaction.emoji}")

	@commands.command()
	async def help(self,ctx):
		#send help message
		await ctx.send(f"Mem Modi ji Hum.Mere pyari Sanghawasiyoo.\n1.dwajapranam")

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error): 
		if isinstance(error, commands.CommandNotFound): 
			await ctx.send("Command not found!")

	@commands.command()
	async def dwajapranam(self,ctx):
		await ctx.send(f"Dwajaprenam Mitramee :)");

def setup(bot):
	bot.add_cog(g_r_mod(bot))	
		