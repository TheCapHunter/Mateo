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



@client.event
async def on_message(message):
    if 'hi' in message.content:
        msg = 'Hello! {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await asyncio.sleep(5)
        await client.delete_message(msg2)

@client.command(pass_context=True)
async def invite(ctx):
        invitelinknew = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
        embedMsg=discord.Embed(color=0xf41af4)
        embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
        embedMsg.set_footer(text="Discord server invited link.")
        await client.send_message(ctx.message.channel, embed=embedMsg)

@client.command(pass_context = True)
async def store(ctx):
ret = await asyncio.gather(
    client.wait_for_message(timeout=10, check=check1),
    client.wait_for_message(timeout=10, check=check2),
    client.wait_for_message(timeout=10, check=check3)
)
    msg1, msg2, msg3 = *ret
    await client.say(*ret)
