import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='D')
    
@client.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)

client.command(pass_context = True)
async def reme(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='A Random Meme', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command(pass_context=True)
async def magicball():
        '''Answer a question with a response'''

        responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]

        random_number = random.randint(0, 19)
        if random_number >= 0 and random_number <= 9:
            embed = discord.Embed(color=0x60E87B)
        elif random_number >= 10 and random_number <= 14:
            embed = discord.Embed(color=0xECE357)
        else:
            embed = discord.Embed(color=0xD55050)

        header = 'Magic ball says...'
        text = responses[random_number]

        embed.add_field(name=header, value=text, inline=True)
        await client.say(embed=embed)
        print('magic ball says {responses}')
        
	
client.run(os.getenv('Token')
