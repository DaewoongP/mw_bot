def init(client):
    @client.event
    async def on_ready():
        print(f'로그인 : {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
