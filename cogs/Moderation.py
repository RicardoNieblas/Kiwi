import discord
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)
    
class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

   # future revision

def setup(client):
    client.add_cog(moderation(client))