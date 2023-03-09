import discord, math
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)
    
class math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief = "Math, heck yeah, now homework should be easy. Right?")
    async def math(self, ctx, arg1, arg2 = None, arg3 = None):
        """Type this command and get the answer from one of five basic math operations: sum, subtraction, multiplication, division, and power."""
        if arg2 == None or arg3 == None:
            await ctx.send("Sorry, one of the numbers is incorrect. Make sure to not mix any letters, and to add spaces between the numbers and the operation sign.")
        else:
            a, b, c = float(arg1), str(arg2), float(arg3)
            if b == '+':
                result = a + c
            elif b == '-':
                result = a - c
            elif b == '*':
                result = a * c
            elif b == '/':
                result = a / c
            elif b == '^':
                result = math.pow(a, c)
            await ctx.send(result)
        
    @commands.command(brief = "More math, cause you know, it's never enough.")
    async def add(self, ctx, *args):
        """Type this command and as many numbers as you want, and Kiwi will tell you the result of adding all the numbers."""
        list = []
        try:
            for arg in args:
                if arg != "+":
                    x = float(arg)
                    list.append(x)
                else:
                    continue
            result = sum(list)
            await ctx.send(result)
        except ValueError:
            await ctx.send("Sorry, one of the numbers is incorrect. Make sure to not mix any letters, and to add spaces between the numbers.")

    @commands.command(brief = "Even more math. I was just bored and wanted something to do.")
    async def prod(self, ctx, *args):
        """Type this command and as many numbers as you want, and Kiwi will tell you the result of adding all the numbers."""
        list = []
        try:
            for arg in args:
                if arg != "*":
                    x = float(arg)
                    list.append(x)
                else:
                    continue
            result = math.prod(list)
            await ctx.send(result)
        except ValueError:
            await ctx.send("Sorry, one of the numbers is incorrect. Make sure to not mix any letters, and to add spaces between the numbers.")

def setup(client):
    client.add_cog(math(client))