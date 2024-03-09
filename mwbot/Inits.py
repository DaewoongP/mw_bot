# init... don't use return
def init(client, commands):
    @client.event
    async def on_ready():
        print(f'로그인 : {client.user}')

    @client.event
    async def on_message(message):
        await client.process_commands(message)

    @client.event
    async def on_command_error(ctx, error):
        print(f"[{ctx.author.display_name}({ctx.author})] -> 에러작성 : \'{error}\'")
        # await ctx.send(f"그런 명령어는 없어용 ㅋ")