import discord
import MyToken
import Inits
import Web
import Lostark
import Lostark_Command
import FiveSecond
import Accessory
from discord.ext import commands


class CMain:
    def __init__(self):
        # token
        self.tokens = MyToken.CToken()
        # init
        intents = discord.Intents.default()
        intents.message_content = True
        self._client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

        Inits.init(client=self._client, commands=commands)

        self._lostark = Lostark.CLostark(token=self.tokens.m_LostarkToken)

    def start(self):
        Lostark_Command.start(client=self._client, lostark=self._lostark, commands=commands, discord=discord)
        # Web.start(client=self._client, commands=commands)
        FiveSecond.start(client=self._client, commands=commands, discord=discord)
        Accessory.start(client=self._client, commands=commands, discord=discord, channel_id=self.tokens.m_GongbangToken)

    def run(self):
        self._client.run(self.tokens.m_DiscordToken)


main = CMain()
main.start()
main.run()
