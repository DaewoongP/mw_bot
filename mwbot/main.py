import discord
import MyToken
import Inits

#token
MyTokens = MyToken.CToken()
#init
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

Inits.init(client)


client.run(MyTokens.m_DiscordToken)
