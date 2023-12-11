import discord, json, os, random
import asyncio
from discord.ext import commands

kiwiGreen = discord.Colour.from_rgb(0, 200, 118)
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents = intents)

# logged in message
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# ----- Fun Commands start here ----- #

# owo event
@client.event
async def on_message(message):
    if "owo" in message.content.lower() and message.author.id != 894472594118557777:
        if random.randint(1, 2) == 1: await message.channel.send("OwO")
    await client.process_commands(message)

# confess command
@client.command(brief = "Makes your message anonymous")
async def confess(ctx, *args):
    """Confess your deepest, darkest secrets to Kiwi. Kiwi will not tell anyone, promise"""
    await ctx.message.delete()
    await ctx.send(' '.join(args))

# howgamer command
@client.command(brief = "Ok, but can your chair do this?")
async def howgamer(ctx, taggedUser: discord.Member = None):
    """Type this command and get the answer of how gamer you or the person you tagged is, based on a percentage."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = "Gamer Rating",
        description = f"{taggedUser.name if taggedUser else ctx.author.name} is {random.randint(0, 100)}% gamer",
        color = kiwiGreen
    ))

# howgay command
@client.command(brief = "Should have said no homo...")
async def howgay(ctx, taggedUser: discord.Member = None):
    """Type this command and get the answer of how gay you or the person you tagged is, based on a percentage."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = "Gay Rating",
        description = f"{taggedUser.name if taggedUser else ctx.author.name} is {random.randint(0, 100)}% gay",
        color = kiwiGreen
    ))

# howsimp command
@client.command(brief = "Oh look! A simp!")
async def howsimp(ctx, taggedUser: discord.Member = None):
    """Type this command and get the answer of how simp you or the person you tagged is, based on a percentage."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = "Simp Rating",
        description = f"{taggedUser.name if taggedUser else ctx.author.name} is {random.randint(0, 100)}% simp",
        color = kiwiGreen
    ))

# imagine command
@client.command(brief = "Imagine writing an imagine command. Oh wait...")
async def imagine(ctx, *args):
    """Type this command and Kiwi will repeat it, with just an "imagine" and the beginning."""
    await ctx.message.delete()
    if args: await ctx.send(embed = discord.Embed(
            title = f"Imagine {' '.join(args)}...",
            description = f"{ctx.author.name} is trying really hard to imagine...",
            color = kiwiGreen
        ))

# magic command
@client.command(brief = "Your good old Magic 8 Ball. It can tell you your luck.")
async def magic(ctx, *args):
    """Type this command and the Magic 8 Ball will try to tell your luck. Hopefully nothing bad happens..."""
    if args: await ctx.send(random.choice([
            # good responses
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            # neutral responses
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            # bad responses
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
    ]))

# pp command
@client.command(brief = "Do you really want to so show everyone your pp size? etto...")
async def pp(ctx, tag: discord.Member = None):
    """It's a ppsize machine. Type the command and you will get the size of your peepee. Note that your ppsize might magically change, so be careful on using this command."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = f"{tag.name if tag else ctx.author.name}'s pp size",
        description = "Too big to measure!!!" if not tag and ctx.author.id == 578280441245597708 or tag and tag.id == 578280441245597708 else f"8{'=' * random.randint(2, 20)}D",
        color = kiwiGreen
    ))

# ----- Fun Commands end here ----- #

# ----- Reaction Commands start here ----- #

# blush command
@client.command(brief = "¡You're blushing!")
async def blush(ctx):
    """Type this command and Kiwi will show a GIF saying you're blushing."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + random.choice([" is blushing!", "'s face turns red'!", " blushes! >///<"]),
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["blush"].values()))))

# cry command
@client.command(brief = "You're crying!")
async def cry(ctx):
    """Type this command and Kiwi will show a GIF saying you're crying."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + random.choice([" is crying...", " needs a hug...", " feels sad...", " TTwTT", " cries..."]),
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["cry"].values()))))

# dance command
@client.command(brief = "Time to dance!")
async def dance(ctx):
    """Type this command and Kiwi will show a GIF saying you're dancing."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + random.choice([" is dancing!", " moves some booty!", " got them moves!"]),
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["dance"].values()))))

# happy command
@client.command(brief = "If you're happy and you know it clap your hands!")
async def happy(ctx):
    """Type this command and Kiwi will show a GIF saying you're dancing."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + random.choice([" is happy!", " feels happy!"]),
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["happy"].values()))))

# teehee command
@client.command(brief = "ehe, te nandayo?")
async def teehee(ctx):
    """Type this command and Kiwi will show a GIF with a grin."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + " c;",
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["teehee"].values()))))

# thinking command
@client.command(brief = "Your dumb*** does not understand.")
async def thinking(ctx):
    """Type this command and Kiwi will show a GIF saying you're thinking."""
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(
        title = str(ctx.author.name) + random.choice([" is thinking...", " can't process that...", " is trying to understand...", " is processing..."]),
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["thinking"].values()))))

# hug command
@client.command(brief = "Your only chance to hug her, she won't let you irl...")
async def hug(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're hugging someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send(random.choice("I'll hug you...", "Do you need a hug?"))
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" hugs ", " gives a hug to "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["hug"].values()))))

# kill command
@client.command(brief = "Omae wa mou, shindeirou. Nani?")
async def kill(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're killing someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send(random.choice("Don't do it TTwTT", "Don't kill yourself TTwTT", "Umm...", "Are you sure?"))
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" killed ", " has killed ", " kills "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["kill"].values()))))

# punch command
@client.command(brief = "ONE PUUUUUUUUUUUUUUUNCH!!!")
async def punch(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're punching someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send(random.choice("Don't do it!", "Don't punch yourself!", "Umm...", "Are you sure?"))
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" punches ", " wacks ", " punched "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["punch"].values()))))

# slap command
@client.command(brief = "Just don't you dare slap a Karen, ok?")
async def slap(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're slapping someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send(random.choice("Don't do it!", "Don't slap yourself!", "Umm...", "Are you sure?"))
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" slaps ", " slapped "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["slap"].values()))))

# stare command
@client.command(brief = "What ya lookin' at?")
async def stare(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're staring at someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send("Are you... looking at a mirror?")
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" stares at ", " looks directly to "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["stare"].values()))))

# wave command
@client.command(brief = "OwO hewwo my fwiend!! (cringe but this command just says hi)")
async def wave(ctx, tag: discord.Member):
    """Type this command and Kiwi will show a GIF saying you're waving at someone."""
    await ctx.message.delete()
    if tag == ctx.author: await ctx.send("Are you... looking at a mirror?")
    elif tag: await ctx.send(embed = discord.Embed(
            title = str(ctx.author.name) + random.choice([" waves at ", " says hi to "]) + str(tag.name) + "!",
            color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["wave"].values()))))

# ----- Reaction Commands end here ----- #

# ----- Play Commands start here ----- #

@client.command(brief = "Play a game with Kiwi!")
async def rps(ctx):
    """Play rock paper scissors with Kiwi!"""
    await ctx.message.delete()
    await ctx.send("Rock, paper, scissors! Choose one!")
    try: msg = await client.wait_for('message', timeout = 10.0)
    except asyncio.TimeoutError: await ctx.send("You took too long to respond. Try again!")
    else:
        if msg.content.lower() == "rock" or "paper" or "scissors":
            await ctx.send(random.choice(["You won!", "You lost!", "It's a tie!"]))
        else:
            await ctx.send("That's not a valid option! Try again!")

@client.command(brief = "Play a game with Kiwi!")
async def get21(ctx):
    await ctx.send(embed = discord.Embed(
        title = "Title",
        color = kiwiGreen
    ).set_image(url = random.choice(list(json.load(open("assets/reactions.json"))["blush"].values()))))

# ----- Play Commands end here ----- #

# will fail if answer is not "kiwi" or "beta"
# client.run(json.load(open("tokens.json"))[str(input("Select a client: ").lower())])
client.run(json.load(open("tokens.json"))["kiwi"])

"""
TODO: Future tasks
* Change status periodically
* React when kiwi is sent
"""