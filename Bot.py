import discord
import respuestas

async def send_message(message, user_message, is_private):
    response = respuestas.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)

def run_discord_bot():
    TOKEN = 'MTIwNjU5ODg4NzM3NzMzODM4OA.GEuURy.ZCLWV01wyIV4L454jqVJk0LO57X4yNw2SZBz7s' ##Lo puedes encontrar en el portal de Discord Developer => Bot => Reset Token
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} se ha conectado al servidor\n')
        for servidor in client.guilds:
            print(f'{servidor.name}(id: {servidor.id})')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        ##Información útil, usuario del mensaje, mensaje, y canal.
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} mandó: "{user_message}" ({channel})')

        ##Para conversación en privado
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
