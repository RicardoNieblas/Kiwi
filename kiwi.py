import discord, json, random
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
    if "owo" in message.content.lower() and message.author.id != 894472594118557777: await message.channel.send("OwO")

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

# will fail if answer is not "kiwi" or "beta"
# client.run(json.load(open("tokens.json"))[str(input("Select a client: ").lower())])
client.run(json.load(open("tokens.json"))["kiwi"])

"""
TODO: Future tasks
* Change status periodically
* React when kiwi is sent
"""