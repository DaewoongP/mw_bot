import discord
import MyToken
import Inits
import Lostark
from discord.ext import commands


class CMain:
    def __init__(self):
        # token
        self.tokens = MyToken.CToken()
        # init
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self._client = commands.Bot(command_prefix="!", intents=self.intents)
        # discord.Client(command_prefix='!', intents=self.intents.all())

        Inits.init(self._client, discord)
        _lostark = Lostark.CLostark(self.tokens.m_LostarkToken)

        @self._client.hybrid_command(name="공지", with_app_command=True, description="로아 공지")
        async def command_notice(ctx):
            await ctx.send(_lostark.get_notice())

    def run(self):
        self._client.run(self.tokens.m_DiscordToken)


main = CMain()
main.run()
