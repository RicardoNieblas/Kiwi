import discord, random
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief = "Just OwO")
    async def owo(self, ctx):
        """Really? What do you want me to say here? Kiwi just says OwO!!!"""
        await ctx.send("OwO")

    @commands.command(brief = "Type a message and Kiwi repeats it.")
    async def say(self, ctx, *args):
        """Type a message. Kiwi deletes your message and repeats it, so that way your message is now anonymous."""
        if args != ():
            await ctx.message.delete()
            await ctx.send(" ".join(args))
    
    @commands.command(brief = "Ok, but can your chair do this?")
    async def howgamer(self, ctx, taggedUser: discord.Member = None):
        """Type this command and get the answer of how gamer you or the person you tagged is, based on a percentage."""
        user = str(ctx.author.name)
        if taggedUser != None:
            user = str(taggedUser.name)
        embed = discord.Embed(
            title = "Gamer Rating",
            description = user + " is " + str(random.randint(0, 100)) + "% gamer.",
            color = kiwi
        )
        await ctx.send(embed = embed)

    @commands.command(brief = "Should have said no homo...")
    async def howgay(self, ctx, taggedUser: discord.Member = None):
        """Type this command and get the answer of how gay you or the person you tagged is, based on a percentage."""
        user = str(ctx.author.name)
        if taggedUser != None:
            user = str(taggedUser.name)
        embed = discord.Embed(
            title = "Gay Rating",
            description = user + " is " + str(random.randint(0, 100)) + "% gay.",
            color = kiwi
        )
        await ctx.send(embed = embed)

    @commands.command(brief = "Oh look! A simp!")
    async def howsimp(self, ctx, taggedUser: discord.Member = None):
        """Type this command and get the answer of how simp you or the person you tagged is, based on a percentage."""
        user = str(ctx.author.name)
        if taggedUser != None:
            user = str(taggedUser.name)
        embed = discord.Embed(
            title = "Simp Rating",
            description = user + " is " + str(random.randint(0, 100)) + "% simp.",
            color = kiwi
        )
        await ctx.send(embed = embed)

    @commands.command(brief = "Imagine writing a imagine command. Oh wait...")
    async def imagine(self, ctx, *args):
        """Type this command and Kiwi will repeat it, with just an 'Imagine' and the beginning."""
        if args != ():
            embed = discord.Embed(
                title = "Imagine " + " ".join(args) + "...",
                description = ctx.author.name + " is trying really hard to imagine...",
                color = kiwi
            )
            await ctx.send(embed = embed)

    @commands.command(brief = "Your good old Magic 8 Ball. It can tell you your luck.")
    async def magic(ctx, *args):
        """Type this command and the Magic 8 Ball will try to tell your luck. Hopefully nothing bad happens..."""
        if args != ():
            await ctx.send(random.choice([
            "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
            "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."
        ]))

    @commands.command(brief = "Do you really want to so show everyone your pp size? etto...")
    async def pp(self, ctx, tag: discord.Member = None):
        """It's a ppsize machine. Type the command and you will get the size of your peepee. Note that your ppsize might magically change, so be careful on using this command."""
        ppsize = "8" + random.choice(["==", "===", "====", "=====", "======", "=======", "========", "=========", "==========", "===========", "============", "=============", "==============", "==============="]) + "D"
        if tag == None:
            user = ctx.author.name
            if ctx.author.id == 578280441245597708 or ctx.author.id == 602244935797702717:
                ppsize = "Too big to measure!!!"
        elif tag != None: 
            user = tag.name
            if tag.id == 578280441245597708 or ctx.author.id == 602244935797702717:
                ppsize = "Too big to measure!!!"
        embed = discord.Embed(
            title = user + "'s pp size",
            description = ppsize,
            color = kiwi
        )
        await ctx.send(embed = embed)
    
def setup(client):
    client.add_cog(fun(client))