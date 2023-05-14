import discord
import classification as cl
import time
file_name = None # Use this variable to store the channel where the bot should receive photos

class MyClient(discord.Client):
  async def on_ready(self):
    print("logged on as {0}!" .format(self.user))

  async def on_message(self, message):
    print("Message from {0.author}: {0.content}" .format(message))
    if message.content == "!PWPola":
      await message.channel.send(f"Olá {message.author.name}! Prazer em conhece-lo. Sou um bot que tenta se passar por um especialista em personagens de animes, eu não tenho certeza de nada, mas há sempre uma grande probabilidade de o que eu estar falando estar certo.")
    if message.attachments:
      for attachment in message.attachments:
        if attachment.filename.lower().endswith(('.jpg')):
          file_name = attachment.filename
          await attachment.save("botPWP/Images_test/" + attachment.filename)
          await message.channel.send(f'Recebi sua imagem :), vou analisar qual personagem de anime é! Já te retorno com os resultados das análises.')
          time.sleep(1)
          await message.channel.send('.')
          time.sleep(1)
          await message.channel.send('.')
          time.sleep(1)
          await message.channel.send('.')
          await message.channel.send(cl.predicted_image(file_name))

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run("MTA5OTgwOTU3MjkxMjM4MjA2Mg.GNAas3.gdZaLvJepUPqrnzJUpeCZGokFSo8TX9xqYFQFg")
