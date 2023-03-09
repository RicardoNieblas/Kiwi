import discord
from discord.ext import commands

"""
TODO: Create a custom help section.
TODO: Fun commands from Dank Memer (mock)
TODO: Create a music section to replace MEE6's commands.
TODO: Info section where it shows you general info about the bot.
TODO: Create the ability to turn on and off different sections from the bot.
"""

kiwi = discord.Colour.from_rgb(0, 200, 118)
    
class help(commands.Cog):
    def __init__(self, client):
        self.client = client

   # future revision

def setup(client):
    client.add_cog(help(client))