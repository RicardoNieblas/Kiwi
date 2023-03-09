import discord, json, random
from discord.ext import commands

kiwi = discord.Colour.from_rgb(0, 200, 118)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

def clientSelection():
    clientSelected = input("Select a client: ")
    if clientSelected.lower() == "kiwi":
        return json.load(open("token.json"))["kiwi"]
    elif clientSelected.lower() == "beta":
        return json.load(open("token.json"))["beta"]

client.run(clientSelection())