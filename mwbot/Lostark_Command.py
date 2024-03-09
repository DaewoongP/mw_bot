
def start(client, lostark, commands):
    @client.hybrid_command(name="로아공지", with_app_command=True, description="로아 공지")
    async def command_notice(ctx: commands.Context):
        print(f"[{ctx.author.display_name}({ctx.author})] : {ctx.message.content}")
        await ctx.send(f"가장 최근 공지 : [{lostark.get_notice_title()[0]}]({lostark.get_notice_link()[0]})")