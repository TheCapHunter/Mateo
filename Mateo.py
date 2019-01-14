import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='D')
    
@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)

bot.run('NTMyMjg5NTUzNTU4NDA1MTQx.DxagPg.J3SHfnkoCVxCKbfaX0Zf-cVw-GA')
