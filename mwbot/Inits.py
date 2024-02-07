
def init(client, discord):
    @client.event
    async def on_ready():
        print(f'로그인 : {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

    @client.hybrid_command(name="ping", with_app_command=True, description="testing~")
    async def ping(ctx):
        await ctx.send("123")