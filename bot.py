import discord
from discord.ext import commands
import datetime
import os

class MyClient(discord.Client):
    async def on_ready(self):
        ID = os.getenv("ID")

        canal = self.get_channel(ID)
        
        if canal:
            await canal.send(f"# 🟢 MOD ATUALIZADO \n [{datetime.datetime.now()}] Favor rodar o script para atualizar o modpack")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
