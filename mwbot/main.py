import DF_Command
import discord
import MyToken
import Inits
import DF
import Web
from discord.ext import commands


class CMain:
    def __init__(self): # init
        # token
        self.tokens = MyToken.CToken()
        # init
        intents = discord.Intents.default()
        intents.message_content = True
        self._client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

        Inits.init(client=self._client, commands=commands)

        # DF
        self._DF = DF.CDF(token=self.tokens.m_DFToken)

    def start(self): # start components
        Web.start(client=self._client, commands=commands)
        DF_Command.start(client=self._client, DF=self._DF, commands=commands, discord=discord)

    def run(self): # run
        self._client.run(self.tokens.m_DiscordToken)


main = CMain()
main.start()
main.run()
