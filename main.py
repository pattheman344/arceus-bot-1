import discord
import random
import praw
import requests
import json
import asyncio
from discord.ext import commands

reddit = praw.Reddit(client_id="[]",
                     client_secret="",
                     password="PASSWORD HERE",
                     user_agent="pat's bot",
                     username="zosly")

client = commands.Bot(command_prefix = '$')
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is ready!')
    game = discord.Game("$help | Currently in 2 servers :)")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You must be a moderator to do this command.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Your ping is `{round (client.latency * 1000)}ms` {ctx.author.mention} ')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Arceus Help Center", description="Credits to CrazyAPI for some of the commands")
    embed.add_field(name="Information :newspaper:", value="botversion\ncovid,corona,coronavirus,covid19\nping")
    embed.add_field(name="Random :shrug:", value="randominsult\nrandomjoke\nrandomlenny", inline=False)
    embed.add_field(name="Fun/jokes :joy:", value="meme\ndice\nslag\n8ball\naltmemes\ncoinflip\ntord/truthordare\nwoosh\ncursedmc")
    embed.add_field(name="Moderation :tools:", value="kick\nban\npurge", inline=False)
    embed.color=0xFF80E0
    try:
         await ctx.author.send(embed=embed)
         await ctx.send("Messaging you all of the commands.")
    except:
         await ctx.send("Turn your DMs on, or it won't work.")

@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
    await ctx.send (f"{amount} messages purged by {ctx.author.mention}")

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked by {ctx.author.mention} for {reason}")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned by {ctx.author.mention} for {reason}")

@client.command()
async def slag(ctx):
    await ctx.send(f'Zack is a slag')

@client.command(aliases=['8ball'])
async def _8ball(ctx, * , question):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
    await ctx.send(f':8ball: {random.choice(responses)}')

@client.command()
async def dice(ctx):
    responses = ["1", "2", "3", "4", "5", "6"]
    await ctx.send(f':game_die: You rolled {random.choice(responses)}')

@client.command()
async def meme(ctx):
       request = requests.get('http://www.crazyapi.tk/api-v1/RandomDankM.php')
       await ctx.send(request.text)
       print(request.text)

@client.command()
async def cursedmc(ctx):
        redditembed=discord.Embed(
        title="", 
        icon="",
        color=0xFF80E0
        )
        subreddit = reddit.subreddit("CursedMinecraft").hot()
        for submission in range(0, random.randint(1, 100)):
                    submission = next(x for x in subreddit if not x.stickied)
        redditembed.set_author(name = f"{submission.title}", icon_url = "")
        redditembed.set_image(url=submission.url)
        redditembed.set_footer(text=f"posted by u/{submission.author}")
        await ctx.send(embed=redditembed)



@client.command()
async def altmemes(ctx):
       request = requests.get('http://www.crazyapi.tk/api-v1/AltMeme.php')
       await ctx.send(request.text)
       print(request.text)

@client.command()
async def randomlenny(ctx):
       request2 = requests.get('http://www.crazyapi.tk/api-v1/RandomLenny.php')
       await ctx.send(request2.text)

@client.command()
async def coinflip(ctx):
       request2 = requests.get('http://www.crazyapi.tk/api-v1/coinflip.php')
       await ctx.send(request2.text)
    
@client.command()
async def randomjoke(ctx):
       request2 = requests.get('http://www.crazyapi.tk/api-v1/RandomJoke.php')
       await ctx.send(request2.text)

@client.command()
async def randominsult(ctx):
       request = requests.get('http://www.crazyapi.tk/api-v1/insult.php')
       await ctx.send(request.text)

@client.command()
async def botversion (ctx):
    await ctx.send('Bot is on version 2.1.')

@client.command(aliases=['truthordare'])
async def tord(ctx, tordoption=None):
    if tordoption == None:
        await ctx.send("Hey! Please say truth or dare!")
    elif tordoption == "truth":
        request = requests.get("http://www.crazyapi.tk/api-v1/TruthOrDare.php?&Truth")
        await ctx.send(request.text)
    elif tordoption == "dare":
        request = requests.get("http://www.crazyapi.tk/api-v1/TruthOrDare.php?&Dare")
        await ctx.send(request.text)
    else:
        await ctx.send("Hey! Please **ONLY** do truth or dare.")

@client.command()
async def woosh(ctx):
        redditembed=discord.Embed(
        title="", 
        icon="",
        color=0xFF80E0
        )
        subreddit = reddit.subreddit("woooosh").hot()
        for submission in range(0, random.randint(1, 100)):
                    submission = next(x for x in subreddit if not x.stickied)
        redditembed.set_author(name = f"{submission.title}", icon_url = "")
        redditembed.set_image(url=submission.url)
        redditembed.set_footer(text=f"posted by u/{submission.author}")
        await ctx.send(embed=redditembed)

@client.command(aliases=['covid','corona', 'coronavirus'])
async def covid19(ctx):
    request = requests.get("http://www.crazyapi.tk/api-v1/CovidCases.php")
    await ctx.send(request.text)
    print (request.text)

client.remove_command(help)

client.run('[]')
