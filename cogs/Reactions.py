import discord, random
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)

"""
TODO: Simplify the embed on the reactions. Try to make the bot show the GIF directly by using the directory, instead of the link of where it is stored from the GitHub repository.
TODO: Add a few more emotions or reactions.
? Possibly start looking into integrating something like a GIF library, only if such exists with anime GIFs exclusively.
"""
    
class reactions(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief = "¡You're blushing!")
    async def blush(self, ctx):
        """Type this command and Kiwi will show a GIF saying you're blushing."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + random.choice([" is blushing!", "'s face turns red'!", " blushes! >///<"]),
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/blush.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "You're crying!")
    async def cry(self, ctx):
        """Type this command and Kiwi will show a GIF saying you're crying."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + random.choice([" is crying...", " needs a hug...", " feels sad...", " TTwTT", " cries..."]),
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/cry.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "Time to dance!")
    async def dance(self, ctx):
        """Type this command and Kiwi will show a GIF saying you're dancing."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + random.choice([" is dancing!", " moves some booty!", " got them moves!"]),
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/dance.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "If you're happy and you know it clap your hands!")
    async def happy(self, ctx):
        """Type this command and Kiwi will show a GIF saying you're dancing."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + random.choice([" is happy!", " feels happy!",]),
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/happy.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "ehe, te nandayo?")
    async def teehee(self, ctx):
        """Type this command and Kiwi will show a GIF with a grin."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + " c;",
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/teehee.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "Your dumb*** does not understand.")
    async def thinking(self, ctx):
        """Type this command and Kiwi will show a GIF saying you're thinking."""
        embed = discord.Embed(
            title = f"{ctx.author.name}" + random.choice([" is thinking...", " can't process that...", " is trying to understand...", " is processing..."]),
            color = kiwi
        )
        embed.set_image(url = random.choice(open("../reactions/thinking.txt").readlines()))
        await ctx.send(embed = embed)

    @commands.command(brief = "Your only chance to hug her, she won't let you irl...")
    async def hug(self, ctx, tag: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're hugging someone."""
        if tag != ():
            if tag == ctx.author:
                await ctx.send(random.choice("I'll hug you...", "Do you need a hug?"))
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" hugs ", " gives a hug to "]) + str(tag.name) + "!",
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/hug.txt").readlines()))
                await ctx.send(embed = embed)

    @commands.command(brief = "Omae wa mou, shindeirou. Nani?")
    async def kill(self, ctx, taggedUser: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're killing someone."""
        if taggedUser != ():
            if taggedUser == ctx.author:
                await ctx.send(random.choice(["Don't do it TTwTT", "Don't kill yourself TTwTT", "Umm...", "Are you sure?"]))
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" killed ", " has killed "]) + str(taggedUser.name) + "!",
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/kill.txt").readlines()))
                await ctx.send(embed = embed)

    @commands.command(brief = "ONE PUUUUUUUUUUUUUUUNCH!!!")
    async def punch(self, ctx, taggedUser: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're punching someone."""
        if taggedUser != ():
            if taggedUser == ctx.author:
                await ctx.send(random.choice(["Don't do it!", "Don't punch yourself!", "Umm...", "Are you sure?"]))
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" punches ", " wacks "]) + str(taggedUser.name) + "!",
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/punch.txt").readlines()))
                await ctx.send(embed = embed)

    @commands.command(brief = "Just don't you dare slap a Karen, ok?")
    async def slap(self, ctx, taggedUser: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're slapping someone."""
        if taggedUser != ():
            if taggedUser == ctx.author:
                await ctx.send(random.choice(["Don't do it!", "Don't slap yourself!", "Umm...", "Are you sure?"]))
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" slaps ", " slapped "]) + str(taggedUser.name) + "!",
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/slap.txt").readlines()))
                await ctx.send(embed = embed)

    @commands.command(brief = "What ya lookin' at?")
    async def stare(self, ctx, taggedUser: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're staring at someone."""
        if taggedUser != ():
            if taggedUser == ctx.author:
                await ctx.send("Are you... looking at a mirror?")
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" stares at ", " looks directly to "]) + str(taggedUser.name) + random.choice(["...", ". What did you do?"]),
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/stare.txt").readlines()))
                await ctx.send(embed = embed)

    @commands.command(brief = "OwO hewwo my fwiend!! (cringe but this command just says hi)")
    async def wave(self, ctx, taggedUser: discord.Member):
        """Type this command and Kiwi will show a GIF saying you're waving at someone."""
        if taggedUser != ():
            if taggedUser == ctx.author:
                await ctx.send("Are you... looking at a mirror?")
            else:
                embed = discord.Embed(
                    title = f"{ctx.author.name}" + random.choice([" waves at ", " says hi to "]) + str(taggedUser.name) + "!",
                    color = kiwi
                )
                embed.set_image(url = random.choice(open("../reactions/wave.txt").readlines()))
                await ctx.send(embed = embed)

def setup(client):
    client.add_cog(reactions(client))