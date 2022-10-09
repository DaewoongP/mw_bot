import asyncio
import discord
import random
import numpy as np
import re
# from discord.ui import Button, View
from discord.ext import commands
from discord_buttons_plugin import *

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains



event = []
event_id = []
event_shuffle = []
event_team = [] ##
lol = []
lol_id = []
score = []
score_list = []
team_score_list = [] ##
score_person = 0

answer = []
colors = [0xFFEEEE, 0xFFF2EE, 0xFFF7EE, 0xFFFBEE, 0xFFFFEE, 0xFBFFEE, 0xF7FFEE, 0xF2FFEE, 0xEEFFEE, 0xEEFFF2,
          0xEEFFF7, 0xEEFFFB, 0xEEFFFF, 0xEEFBFF, 0xEEF2FF, 0xEEEEFF, 0xF2EEFF, 0xF7EEFF, 0xFBEEFF, 0xFFEEFF,
          0xFFEEFB, 0xFFEEF7, 0xFFEEF2, 0xFFD9D9, 0xFFE2D9, 0xFFECD9, 0xFFF5D9, 0xFFFFD9, 0xF5FFD9, 0xECFFD9,
          0xE2FFD9, 0xD9FFD9, 0xD9FFE2, 0xD9FFEC, 0xD9FFF5, 0xD9FFFF, 0xD9F5FF, 0xD9ECFF, 0xD9E2FF, 0xD9D9FF,
          0xE2D9FF, 0xECD9FF, 0xF5D9FF, 0xFFD9FF, 0xFFD9F5, 0xFFD9EC, 0xFFC4C4, 0xFFD2C4, 0xFFE1C4, 0xFFF0C4,
          0xFFFFC4, 0xF0FFC4, 0xE1FFC4, 0xD2FFC4, 0xC4FFC4, 0xC4FFD2, 0xC4FFE1, 0xC4FFF0, 0xC4FFFF, 0xC4F0FF,
          0xC4E1FF, 0xC4D2FF, 0xC4C4FF, 0xD2C4FF, 0xE1C4FF, 0xF0C4FF, 0xFFC4FF, 0xFFC4F0, 0xFFC4E1]

#bot = discord.Client()

token_text = open("C:\\Users\\qsc14\\Desktop\\discord\\token\\mw_token.txt", 'r')
token = token_text.readline() #토큰을 로컬 텍스트에서 가져옴

# discord bot developer portal 에서 message content intent (ON) 설정 이후 True 까지 해줘야 command가 돌아감
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None) # 전처리 기호
buttons = ButtonsClient(bot)


@bot.event
async def on_ready():
    print('We have loggedd in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online,#online, idle, dnd, offline
                              activity=discord.Game(name='!도움 / 패치노트 읽으세요 ㅎ'))


# -------------------------------------------------------------------------------------- 이벤트처리
@bot.event
async def on_message(message):
    # ---------------------------------- 정답맞추기
    if message.content.startswith('정답') and message.content.endswith('정답'):
        channel = message.channel
        user = message.author.nick
        await channel.send(f'> 💬 > {message.author.mention} ')

    # ---------------------------------- 야리돌림
    if message.content.startswith('연규야..') and message.content.endswith('연규야..'):
        await message.channel.send('**형이야..**')

    if message.content.startswith('머웅아') and message.content.startswith('머웅아'):
        await message.channel.send('왜')

    # ---------------------------------- 쌀묵
    if message.content.startswith('쌀') and message.content.endswith('쌀'):
        await message.channel.send('묵')
        await message.channel.send('자')

    # ---------------------------------- 엄
    if message.content.startswith('엄') and message.content.endswith('엄'):
        await message.channel.send('준')
        await message.channel.send('식')

    if message.content.startswith('어서빨리') and message.content.endswith('어서빨리'):
        await message.channel.send('로아.. 하고싶다')

    if message.content.startswith('굿') and message.content.endswith('굿'):
        await message.channel.send('**굿**')

    # ---------------------------------- 이모티콘
    if message.content.startswith('놀자에요') and message.content.endswith('놀자에요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958401283327406140/i15155283135.png')
    if message.content.startswith('머쓱해요') and message.content.endswith('머쓱해요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958401283734245376/i15185318509.png')
    if message.content.startswith('뭐라구요') and message.content.endswith('뭐라구요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958401282786357318/i15117433596.png')
    if message.content.startswith('웃프네요') and message.content.endswith('웃프네요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958401283012837507/i15148925192.png')
    if message.content.startswith('추천이요') and message.content.endswith('추천이요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958401283524534332/i15179338842.png')
    if message.content.startswith('엄지') and message.content.endswith('엄지'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399737529237574/01_1_01_.png')
    if message.content.startswith('야호') and message.content.endswith('야호'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399737852207124/01_1_03_.png')
    if message.content.startswith('크크') and message.content.endswith('크크'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399738120638504/01_1_06_.png')
    if message.content.startswith('방긋') and message.content.endswith('방긋'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399738326167592/01_1_09_.png')
    if message.content.startswith('해줘') and message.content.endswith('해줘'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399738514927657/01_1_13_.png')
    if message.content.startswith('안줘') and message.content.endswith('안줘'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399738695262268/01_1_14__.png')
    if message.content.startswith('빠직') and message.content.endswith('빠직'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399739064373318/01_1_17_.png')
    if message.content.startswith('슬퍼') and message.content.endswith('슬퍼'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399739286667314/01_1_18_.png')
    if message.content.startswith('향기') and message.content.endswith('향기'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399739513155725/01_1_23_.png')
    if message.content.startswith('털썩') and message.content.endswith('털썩'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958399739999686737/01_1_24_.png')
    if message.content.startswith('머쓱환에요') and message.content.endswith('머쓱환에요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958418096899649566/ezgif-2-ee1167fb00.png')
    if message.content.startswith('놀자에몽') and message.content.endswith('놀자에몽'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958418815132254208/ezgif-2-22c1384f51.png')
    if message.content.startswith('뀨잉') and message.content.endswith('뀨잉'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536457747017748/unknown.png')
    if message.content.startswith('두렵다') and message.content.endswith('두렵다'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536458099331102/unknown.png')
    if message.content.startswith('못참지') and message.content.endswith('못참지'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536458409705512/unknown.png') 
    if message.content.startswith('영차') and message.content.endswith('영차'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536458799788042/unknown.png')
    if message.content.startswith('이이잉') and message.content.endswith('이이잉'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536459152101386/unknown.png')    
    if message.content.startswith('좋아요') and message.content.endswith('좋아요'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536459563139072/unknown.png')
    if message.content.startswith('핥짝') and message.content.endswith('핥짝'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536459911278614/unknown.png')
    if message.content.startswith('호에엥') and message.content.endswith('호에엥'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007536460326522932/unknown.png')       
    if message.content.startswith('몰?루') and message.content.endswith('몰?루'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958413802477584404/molru.gif')
    if message.content.startswith('팝콘각') and message.content.endswith('팝콘각'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958414394734297188/popcorn.gif')
    if message.content.startswith('녹턴') and message.content.endswith('녹턴'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/958364159983112282/e5d5403296a70ad3b6973ef1794898e7dd204479af5cd837a6baa7d8c4de365c789d23061f176d8e91cfc9efebc3792f73068ad86b8dcec55679b0e195c001198b5b2fabc05ae2350c9a91a9455ef75d788e7a6368f7b630be893f02e9e7fd37.png')
    if message.content.startswith('아하!') and message.content.endswith('아하!'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/967397648652992582/unknown.png')
    if message.content.startswith('흐음...') and message.content.endswith('흐음...'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/967757392592904243/unknown.png')
    if message.content.startswith('감사합니다~') and message.content.endswith('감사합니다~'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/969275402038173776/jerry.gif')
    if message.content.startswith('엄격') and message.content.endswith('엄격'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/972541350010552330/unknown.png')
    if message.content.startswith('나락') and message.content.endswith('나락'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/323766857708470272/972789822462771250/bb352af89e389066.gif')
    if message.content.startswith('오케이~') and message.content.endswith('오케이~'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/980028328683634688/emma-removebg-preview.png')
    if message.content.startswith('왜!!') and message.content.endswith('왜!!'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/323766857708470272/985188355560075345/7ed06c892a3d0baa.gif')
    if message.content.startswith('개추') or message.content.endswith('개추'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/957612748978683914/1007181232720851024/unknown.png')
    
    await bot.process_commands(message)


# -------------------------------------------------------------------------------------- 기본

@bot.command()
async def 이모티콘(ctx):
    await ctx.send('**이모티콘 목록 클릭하면 잘보입니다.**')
    await ctx.send('https://cdn.discordapp.com/attachments/957612748978683914/958425378517553222/unknown.png')


@bot.command()
async def 패치노트(ctx):
    embed = discord.Embed(title='📖 머웅 봇 v3.0 패치노트', color=random.choice(colors))
    # 📕📘📙📗
    embed.add_field(name='📕 1. `!프로필` 베타버전', value='`추가 작업 중`', inline=False)
    embed.add_field(name='📘 2. `!강화`', value='`에스더 강화 패치 추가 하락확률 = 강화확률`', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 도움(ctx):
    # 메인 페이지
    page0 = discord.Embed(title='💡 도움!', color=random.choice(colors))
    page0.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/957612748978683914/957631143493111808/quest_adventure.png')
    page0.add_field(name='📖 머웅 봇 패치노트', value='`!패치노트`', inline=False)
    page0.add_field(name='✏️ 닉네임 변경(공백X)', value='`!닉변 (원래닉) (변경닉)`', inline=False)  # inline True = 2줄 False = 1줄
    page0.add_field(name='🖼️ 이모티콘', value='`!이모티콘`', inline=False)
    page0.add_field(name='⚔️ 강화', value='`!강화` `!강화확률 (강화수치)` `!강화확인`', inline=False)
    page0.add_field(name='🪙 코인', value='`!코인`', inline=False)
    page0.add_field(name='🍀 운세', value='`!운세 (자신의 생년월일)`', inline=False)
    page0.add_field(name='🎉 이벤트', value='`!이벤트` `!이벤트탈주` `!이벤트멤버` `!팀나누기 (팀 수)`', inline=False)
    page0.add_field(name='🎉 이벤트 점수', value='`!점수현황` `!점수추가` `!점수감소` `!점수초기화`', inline=False)
    page0.add_field(name='🎉 이벤트 팀', value='`!팀점수현황` `!팀점수추가` `!팀점수감소` `!팀점수초기화`', inline=False)
    page0.add_field(name='🎮 롤', value='`!롤` `!롤팟탈주` `!롤멤버` `!롤멤버초기화`', inline=False)
    page0.add_field(name='💰 레이드 경매', value='`!경매 (인원수) (경매장가)`', inline=False)
    page0.add_field(name='📺 자투리', value='`!자투리`', inline=False)
    page0.add_field(name='🏷️ 이동', value='`아래 도움에 맞는 버튼을 클릭하면 이동합니당`',inline=False)
    page0.set_footer(text='by 머웅',
                     icon_url='https://cdn.discordapp.com/attachments/957612748978683914/958399739999686737/01_1_24_.png')

    # 패치노트 페이지
    page1 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page1.add_field(name='📖 머웅 봇 패치노트', value='`!패치노트` 명령어를 사용하여 봇의 현재 버전 패치내역을 확인합니다.',inline=False)
    page1.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975984070850932806/unknown.png')

    # 닉네임 변경 페이지
    page2 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page2.add_field(name='✏️ 닉네임 변경', value='`!닉변 (원래닉) (변경닉)` 명령어를 사용하여 닉네임 변경이 가능, ', inline=False)
    page2.add_field(name='⚠️ 주의사항', value='닉네임 사이에 공백 있을경우 변경 불가, 봇보다 권한이 높을경우 불가', inline=False)
    page2.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975984973607751700/unknown.png')

    # 이모티콘 페이지
    page3 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page3.add_field(name='🖼️ 이모티콘', value='`!이모티콘` 을 입력하면 사용할 수 있는 이모티콘 목록이 나옵니다., ', inline=False)
    page3.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975985936670277662/unknown.png')

    # 강화 페이지
    page4 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page4.add_field(name='⚔️ 강화', value='옆 채널 머웅투르의 공방에서 `!강화` 명령어를 사용하여 강화 시뮬레이터 사용가능합니다.', inline=False)
    page4.add_field(name='⚔️ 강화확인', value='`!강화확인` 입력하면 자신의 강화 상태가 나옵니다.', inline=False)
    page4.add_field(name='⚔️ 강화확률', value='`!강화확률 (강화수치)` 입력하면 강화수치에 맞는 확률이 나옵니다.', inline=False)
    page4.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975988346813833266/unknown.png')

    # 코인 페이지
    page5 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page5.add_field(name='🪙 코인', value='`!코인` 도지코인 ON, ', inline=False)
    page5.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975989123611521054/unknown.png')

    # 코인 페이지
    page6 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page6.add_field(name='🍀 운세', value='`!운세 (자신의 생년월일)` 네이버 오늘의 운세 확인 가능! ', inline=False)
    page6.add_field(name='🍀 운세', value='ex) `!운세 19970101`', inline=False)
    page6.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/977149265191252008/unknown.png')

    # 이벤트 페이지
    page7 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page7.add_field(name='🎉 이벤트', value='`!이벤트` `!이벤트탈주` `!이벤트멤버`이벤트 참여, 탈주, 멤버확인이 가능합니다', inline=False)
    page7.add_field(name='🎉 이벤트', value='`!팀나누기 (팀 수)` 이벤트멤버에서 팀을 나눕니다', inline=False)
    page7.add_field(name='🎉 이벤트', value='`!점수현황` `!점수추가` `!점수감소` `!점수초기화` \n `!팀점수현황` `!팀점수추가` `!팀점수감소` `!팀점수초기화`\n위 명령어를 사용하여 이벤트에서 점수 추가, 확인, 초기화가 가능합니다', inline=False)
    page7.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975994244168843264/unknown.png')

    # 롤 페이지
    page8 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page8.add_field(name='🎮 롤', value='`!롤` `!롤팟탈주` `!롤멤버` 명령어 입력해서 파티를 구하거나, 탈주, 멤버 확인 가능합니다', inline=False)
    page8.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975995016835112990/unknown.png')

    # 레이드 경매 페이지
    page9 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page9.add_field(name='💰 레이드 경매', value='`!경매 (공대인원) (경매장 가격)` 명령어 입력해서 쌀먹골드와 손해 분기점을 확인 가능합니다.', inline=False)
    page9.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975995666700599326/unknown.png')

    # 자투리 페이지
    page10 = discord.Embed(title='💡 **도움!**', color=random.choice(colors))
    page10.add_field(name='📺 자투리', value='`!자투리` 자.. 드가자! 링크 누르면 유튜브로 이동', inline=False)
    page10.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975995898184228884/unknown.png')


    pages = [page0, page1, page2, page3, page4,
             page5, page6, page7, page8, page9, page10]

    message = await ctx.send(embed=page0)

    # 아래 리액션 버튼 추가
    await message.add_reaction('💡')
    await message.add_reaction('📖')
    await message.add_reaction('✏️')
    await message.add_reaction('🖼️')
    await message.add_reaction('⚔️')
    await message.add_reaction('🪙')
    await message.add_reaction('🍀')
    await message.add_reaction('🎉')
    await message.add_reaction('🎮')
    await message.add_reaction('💰')
    await message.add_reaction('📺')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True: # 리액션에 따른 임베드 출력
        if str(reaction) == '💡':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '📖':
            i = 1
            await message.edit(embed=pages[i])
        elif str(reaction) == '✏️':
            i = 2
            await message.edit(embed=pages[i])
        elif str(reaction) == '🖼️':
            i = 3
            await message.edit(embed=pages[i])
        elif str(reaction) == '⚔️':
            i = 4
            await message.edit(embed=pages[i])
        elif str(reaction) == '🪙':
            i = 5
            await message.edit(embed=pages[i])
        elif str(reaction) == '🍀':
            i = 6
            await message.edit(embed=pages[i])
        elif str(reaction) == '🎉':
            i = 7
            await message.edit(embed=pages[i])
        elif str(reaction) == '🎮':
            i = 8
            await message.edit(embed=pages[i])
        elif str(reaction) == '💰':
            i = 9
            await message.edit(embed=pages[i])
        elif str(reaction) == '📺':
            i = 10
            await message.edit(embed=pages[i])
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=600, check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


@bot.command()
async def 닉변(ctx, member: discord.Member,*, nick):  # !닉변 머웅2 123 # 닉변 명령어
    if member.nick == None:
        before_nick = str(member.name)
    else:
        before_nick = str(member.nick)
    await member.edit(nick=nick)

    embed = discord.Embed(title='**닉네임 변경**', color=random.choice(colors))  # 임베드 타이틀 - 섬네일 - 필드 - 푸터 순서 잘지키기
    embed.add_field(name='✏️ 변경 완료!', value=f'**{str(before_nick)}** ➡️ {member.mention}', inline=False)
    await ctx.send(embed=embed)
    

# -------------------------------------------------------------------------------------- 강화
@bot.command()
#@commands.cooldown(1, 600, commands.BucketType.user) #서버 자체에 쿨타임 생성
async def 강화(ctx):
    # 명령어 입력한 사람 id, 강화 수치 가져오기
    id = ctx.message.author.id  # id 가져오기
    f = open('C:\\Users\\qsc14\\Desktop\\discord\\rf.txt', 'r')
    text_file = f.readlines()
    if f'{id}\n' not in text_file:
        text_file.append(f'{id}\n')
        text_file.append('0\n')
        text_file.append('0\n')
    rf_id = text_file.index(f'{id}\n')  # 텍스트파일 id의 위치
    rf = int(text_file[rf_id + 1])  # id에 따른 강화수치 => str
    rf_try = int(text_file[rf_id + 2])  # 누른 횟수
    f.close()  # 파일 읽기 종료

    # 강화 상태에 따른 확률 설정값
    rf_effect = 0x000000
    if rf == 0:
        success = 0.05
        rf_effect = 0x000000
    elif rf == 1:
        success = 0.01
        rf_effect = 0x000000
    elif rf == 2:
        success = 0.005
        rf_effect = 0xff0000
    elif rf == 3:
        success = 0.0025
        rf_effect = 0xff8c00
    elif rf == 4:
        success = 0.001
        rf_effect = 0xffff00
    elif rf == 5:
        success = 0.0005
        rf_effect = 0x008000
    elif rf == 6:
        success = 0.00025
        rf_effect = 0x0033ff
    elif rf == 7:
        success = 0.0001
        rf_effect = 0x4b0082
    elif rf == 8:
        await ctx.send('이걸 8강을 성공하셨네 ㄷㄷ')


    rf_try += 1

    # 강화 상태 메세지
    rf_name = ['강화 성공', '강화 실패', '강화 하락']
    level = np.random.choice(rf_name, p=[success, 1 - (success*2), success])  # 강화 상태

    # 강화 성공?
    if level == rf_name[0]:
        embed = discord.Embed(title='```강화 성공 !!```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf + 1}', inline=False)
        embed.add_field(name='누른 횟수', value=f'{rf_try}번 만에 성공', inline=True)
        await ctx.send(embed=embed)
        

        channel = bot.get_channel(323766857708470272)
        embed = discord.Embed(title='```강화 성공 !!```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf + 1}', inline=False)
        embed.add_field(name='누른 횟수', value=f'{rf_try}번 만에 성공', inline=True)
        await channel.send(embed=embed)

        rf += 1  # 강화 수치 증가 (성공)

    # 강화 하락
    elif level == rf_name[2]:
        if rf == 0:
            await ctx.send('와 1강도 안붙었는데 하락 확률을 뚫으셨네요 ㅋㅋ')
        else:
            embed = discord.Embed(title='```강화 하락 ㄷㄷ```', color=rf_effect)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
            embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
            embed.add_field(name='하락 확률', value=f'{success * 100}%', inline=True)
            embed.add_field(name='강화 상태', value=f'{rf} => {rf - 1}', inline=False)
            embed.add_field(name='누른 횟수', value=f'{rf_try}번이나 눌렀는데 떨어짐 ㅠ', inline=True)
            await ctx.send(embed=embed)
            
            channel = bot.get_channel(323766857708470272)
            embed = discord.Embed(title='```강화 하락 ㄷㄷ```', color=rf_effect)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
            embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
            embed.add_field(name='하락 확률', value=f'{success * 100}%', inline=True)
            embed.add_field(name='강화 상태', value=f'{rf} => {rf - 1}', inline=False)
            embed.add_field(name='누른 횟수', value=f'{rf_try}번이나 눌렀는데 떨어짐 ㅠ', inline=True)
            await channel.send(embed=embed)

            rf -= 1 # 강화 수치 하락 (실패)



    # 강화 실패?
    else:
        embed = discord.Embed(title='```강화 실패 ㅠㅠ```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='현재 강화 수치', value=f'{rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf}', inline=False)
        embed.add_field(name='누른 횟수', value=f'{rf_try}번 누름', inline=True)
        await ctx.send(embed=embed)

    text_file[rf_id + 1] = str(f'{rf}\n')  # str \n 형태로 강화 수치값 넣어주기
    text_file[rf_id + 2] = str(f'{rf_try}\n')  # 마찬가지로 장기백값 넣어주기
    f = open('C:\\Users\\qsc14\\Desktop\\discord\\rf.txt', 'w')
    f.writelines(text_file)
    f.close()

@bot.command()
async def 강화확률(ctx, k):
    n = int(k)
    if n == 1:
        await ctx.send('`5%`')
    elif n == 2:
        await ctx.send('`1%`')
    elif n == 3:
        await ctx.send('`0.5%`')
    elif n == 4:
        await ctx.send('`0.25%`')
    elif n == 5:
        await ctx.send('`0.1%`')
    elif n == 6:
        await ctx.send('`0.05%`')
    elif n == 7:
        await ctx.send('`0.025%`')
    elif n == 8:
        await ctx.send('`0.01%`')
    else:
        await ctx.send('강화 수치 제대로 입력 해줘')

# -------------------------------------------------------------------------------------- 이벤트
@bot.command()
async def 이벤트(ctx):  # 이벤트 리스트에 멤버 입력
    user = ctx.message.author.nick  # 닉네임 가져오기
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name  # 디코 이름 일경우 닉네임 말고 이름으로 가져옴
    if id in event_id:  # 리스트에 id 있을경우 출력
        await ctx.send('한번만 누르셈 ㅡㅡ')
    else:  # 리스트에 id 없으면 닉네임 / 이름 , id 리스트에 저장, 출력
        embed = discord.Embed(title='🎉 ```딩식당 이벤트```', color=random.choice(colors))
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960483064197296168/unknown_2.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='이벤트 등록완료!', value=f'<@{id}>', inline=False)
        await ctx.send(embed=embed)
        event.append(user)
        event_id.append(id)
        score.append(user)
        score.append(0)
        # score_list에 미리 값 던지기
        i = score.index(user)
        score_list.append([score[i], score[i + 1]])
        

@bot.command()
async def 점수추가(ctx):  # 자신의 점수 추가
    if event:
        user = ctx.message.author.nick  # 닉네임 가져오기
        id = ctx.message.author.id  # id 가져오기
        if user == None:
            user = ctx.message.author.name  # 디코 이름 일경우 닉네임 말고 이름으로 가져옴
        event_index = event_id.index(id)  # event 리스트의 아이디 위치

        score_list[event_index][1] = int(score_list[event_index][1]) + 1  # 점수 추가

        embed = discord.Embed(title=f'🔺 {user} 점수 추가', color=random.choice(colors))
        embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
        embed.add_field(name=f'1점 추가!', value=f'<@{id}>', inline=False) # name, title에는 멘션이 안되네 시ㅡ발
        #for i in range(0, len(event)):  # 전체 인원 현재 점수 출력  
        #    embed.add_field(name=f'{score_list[i][0]}', value=f'> {score_list[i][1]}점', inline=False)
        embed.add_field(name=f'{score_list[event_index][0]}', value=f'> {score_list[event_index][1]}점', inline=False)
        await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


@bot.command()
async def 점수감소(ctx):  # 자신의 점수 감소
    if event:
        user = ctx.message.author.nick  # 닉네임 가져오기
        id = ctx.message.author.id  # id 가져오기
        if user == None:
            user = ctx.message.author.name  # 디코 이름 일경우 닉네임 말고 이름으로 가져옴
        event_index = event_id.index(id)  # event 리스트의 아이디 위치

        score_list[event_index][1] = int(score_list[event_index][1]) - 1  # 점수 추가
        if score_list[event_index][1] < 0: # 0 이하일 경우 0으로 고정
            score_list[event_index][1] = 0
     
        embed = discord.Embed(title=f'🔻 {user} 점수 감소', color=random.choice(colors))
        embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
        embed.add_field(name=f'1점 감소 ㅠㅠ', value=f'<@{id}>', inline=False) # name, title에는 멘션이 안되네 시ㅡ발
        #for i in range(0, len(event)):  # 전체 인원 현재 점수 출력  
        #    embed.add_field(name=f'{score_list[i][0]}', value=f'> {score_list[i][1]}점', inline=False)
        embed.add_field(name=f'{score_list[event_index][0]}', value=f'> {score_list[event_index][1]}점', inline=False)
        await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


@bot.command()
async def 점수현황(ctx):
    if event:
        embed = discord.Embed(title=' **🎉 현재 점수 현황**', color=random.choice(colors))
        embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
        for i in range(0, len(event)):  # 현재 점수 출력  
            embed.add_field(name=f'{score_list[i][0]}', value=f'> {score_list[i][1]}점', inline=True)
        await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


@bot.command()
async def 점수초기화(ctx):
    if event:
        embed = discord.Embed(title='🗑️ **점수 초기화**', color=random.choice(colors))
        embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/975561969321009202/baseline_delete_white_24dp.png')
        for i in range(0, len(event)):  # 현재 점수 출력  
            score_list[i][1] = 0
            embed.add_field(name=f'{score_list[i][0]}', value=f'> {score_list[i][1]}점', inline=True)
        await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


#------------------------------------------------------------------ 팀 점수        
@bot.command()
async def 팀점수추가(ctx, n):# !팀점수추가 (x팀) > 몇점추가할래? > 대답(int) > 적용
    t = int(n) # 자꾸 str값으로 들어옴
    if team_score_list == []: # 팀나누기 없이 팀점수추가?
        await ctx.send('먼저 팀나누기를 해서 팀을 나눠줘')
    else: # 주요 코드
        await ctx.send('추가할 점수를 숫자만 적어줘')
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try:
            team_score_msg = await bot.wait_for('message', check = check, timeout=10.0)

        except asyncio.TimeoutError:
            await ctx.send('10초 지나서 다시 처음부터 입력해줘')
        else:
            if int(team_score_msg.content) > 0:
                team_score_list[t-1][1] = team_score_list[t-1][1] + int(team_score_msg.content)

                embed = discord.Embed(title=f'🔺 {t}팀 점수 추가', color=random.choice(colors))
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
                embed.add_field(name=f'{team_score_msg.content}점 추가!', value='** **', inline=False) # name, title에는 멘션이 안되네 시ㅡ발
                embed.add_field(name=f'{team_score_list[t-1][0]}팀', value=f'> {team_score_list[t-1][1]}점', inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send('숫자값만 딱 입력해줘!')


@bot.command()
async def 팀점수감소(ctx, n):
    t = int(n) # 자꾸 str값으로 들어옴
    if team_score_list == []: # 팀나누기 없이 팀점수추가?
        await ctx.send('먼저 팀나누기를 해서 팀을 나눠줘')
    else: # 주요 코드
        await ctx.send('감소시킬 점수를 숫자만 적어줘')
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try:
            team_score_msg = await bot.wait_for('message', check = check, timeout=10.0)

        except asyncio.TimeoutError:
            await ctx.send('10초 지나서 다시 처음부터 입력해줘')
        else:
            if int(team_score_msg.content) > 0:
                min_chk = team_score_list[t-1][1] - int(team_score_msg.content)
                if min_chk < 0:
                    await ctx.send(f'현재 {t}팀의 점수는 {team_score_list[t-1][1]}점이야. 음수가 되지 않도록 다시 입력해줘')
                else:
                    team_score_list[t-1][1] = team_score_list[t-1][1] - int(team_score_msg.content)
                    embed = discord.Embed(title=f'🔻 {t}팀 점수 감소', color=random.choice(colors))
                    embed.set_thumbnail(
                        url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
                    embed.add_field(name=f'{team_score_msg.content}점 감소', value='** **', inline=False) # name, title에는 멘션이 안되네 시ㅡ발
                    embed.add_field(name=f'{team_score_list[t-1][0]}팀', value=f'> {team_score_list[t-1][1]}점', inline=False)
                    await ctx.send(embed=embed)
            else:
                await ctx.send('숫자값만 딱 입력해줘!')


@bot.command()
async def 팀점수현황(ctx):
    #점수 => 점수 현황, 팀점수, 팀점수 관련 제작
    if event:
        if event_team == []:
            await ctx.send('먼저 팀나누기를 해서 팀을 나눠줘')
        else:
            team_len = len(event_team) / 2 # float
            embed = discord.Embed(title=' **🎉 현재 팀 점수 현황**', color=random.choice(colors))
            embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/957612748978683914/975554586272215040/baseline_sports_score_white_24dp.png')
            for i in range(0, int(team_len)):  # 현재 점수 출력  
                embed.add_field(name=f'{team_score_list[i][0]}팀', value=f'> {team_score_list[i][1]}점', inline=False)
            await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


@bot.command()
async def 팀점수초기화(ctx):
    if event:
        if event_team == []:
            await ctx.send('먼저 팀나누기를 해서 팀을 나눠줘')
        else:
            team_len = len(event_team) / 2 # float
            embed = discord.Embed(title='🗑️ **팀 점수 초기화**', color=random.choice(colors))
            embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/957612748978683914/975561969321009202/baseline_delete_white_24dp.png')
            for i in range(0, int(team_len)):  # 현재 점수 출력  
                team_score_list[i][1] = 0
                embed.add_field(name=f'{team_score_list[i][0]}팀', value=f'> {team_score_list[i][1]}점', inline=True)
            await ctx.send(embed=embed)

    else:
        await ctx.send('이벤트에 아무도 없넹')


@bot.command()
async def 이벤트멤버(ctx):  # 이벤트 멤버 리스트 출력
    member_ev = "` `".join(event) # 리스트 특수문자 없애고 값 사이에 ` ` 출력

    embed = discord.Embed(title='🎉 **이벤트 멤버 현황**', color=random.choice(colors))
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/957612748978683914/960483064197296168/unknown_2.png')
    embed.add_field(name=f'총 {str(len(event))} 명', value=f'`{member_ev}`', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 이벤트탈주(ctx):  # 이벤트 리스트에 멤버 입력
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name
    if id in event_id:
        await ctx.send('이벤트를 버리네 ㅋㅋ')
        id_off = event_id.index(id)  # 탈주범 아이디로 리스트상 위치확인
        event.pop(id_off)  # 탈주범 아이디 위치 에있는 닉네임 / 이름 삭제
        event_id.remove(id)  # 탈주범 아이디 삭제
        id_off_score = id_off * 2
        score.pop(id_off_score)  # score 위치 이름 삭제
        score.pop(id_off_score)  # score 위치 이름이 삭제되었으므로 앞으로 땡겨진 점수 삭제
    else:
        await ctx.send('**!이벤트가입** 부터 좀;')


@bot.command()
async def 팀나누기(ctx, div):  # !팀나누기 n  #n개의 팀으로 나누어짐
    n = int(div)
    if n == 0:
        await ctx.send('0으로 나눈다니 빠가군요')
    n = len(event) // n
    if n == 0:
        await ctx.send('이벤트에 사람이 없거나 사람보다 팀 수가 더 많아')
    else:
        event_shuffle = list(event)  # 리스트 복사할때는 꼭 list 연산자 붙여주자!!!!!
        random.shuffle(event_shuffle)

        # 각각의 팀을 이중리스트 형태로 저장
        result = [event_shuffle[i * n:(i + 1) * n] for i in
                  range((len(event_shuffle) + n - 1) // n)]  # list comprehension

        # list = [] 이런식으로 쓰면 전역변수가 아닌 로컬변수로 처리됨
        event_team.clear()
        team_score_list.clear()

        t = 0

        for i in range(len(result)):
            if ((len(result[i]) % n) != 0):
                member_team = "` `".join(result[i]) # 리스트 특수문자 없애고 값 사이에 ` ` 출력
                embed = discord.Embed(title='💣 깍두기', color=random.choice(colors))  # result의 팀을 각각 embed로 출력
                embed.add_field(name='남는 사람', value=f'`{member_team}`', inline=False)
                await ctx.send(embed=embed)

            else:
                event_team.append(i+1)
                event_team.append(0)
                member_team = "` `".join(result[i]) # 리스트 특수문자 없애고 값 사이에 ` ` 출력
                embed = discord.Embed(title=f'🎉 {i + 1}팀', color=random.choice(colors))  # result의 팀을 각각 embed로 출력
                embed.add_field(name=f'{i + 1}팀 멤버', value=f'`{member_team}`', inline=False)
                await ctx.send(embed=embed)
                team_score_list.append([event_team[t],event_team[t+1]]) # 팀스코어리스트 이중리스트에 [[팀숫자, 점수]] 형태
                t = t + 2


@bot.command()
async def 코인(ctx):
    coin = random.randrange(1, 3)
    if (coin == 1):
        embed = discord.Embed(title='🤭 앞면!', color=0xffffff)  # result의 팀을 각각 embed로 출력
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/963299860923183144/doge.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='🤔 뒷면!', color=0x000000)  # result의 팀을 각각 embed로 출력
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/963302395062931486/doge_black.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)


# -------------------------------------------------------------------------------------- 롤
@bot.command()
async def 롤(ctx):  # ㅋㅋ
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name
    if id in lol_id:  # 리스트에 id 있을경우 출력
        await ctx.send('한번만 누르셈 ㅡㅡ')
    else:
        if len(lol) >= 5:
            await ctx.send('풀파티네요 ㄲㅂ')
        else:
            lol.append(user)
            lol_id.append(id)
        member_l = "` `".join(lol) # 리스트 특수문자 없애고 값 사이에 ` ` 출력
        embed = discord.Embed(title='🎮 롤 멤버', color=0x067EDB)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960737976365744198/lol.png')
        embed.add_field(name='롤 멤버 추가 완료!', value=f'`{member_l}`', inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def 롤팟탈주(ctx):  # 롤 리스트에 멤버 삭제
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name
    if id in lol_id:
        await ctx.send('너없으면 롤망해 ㅠㅠ')
        id_off = lol_id.index(id)  # 탈주범 아이디로 리스트상 위치확인
        lol.pop(id_off)  # 탈주범 아이디 위치 에있는 닉네임 / 이름 삭제
        lol_id.remove(id)  # 탈주범 아이디 삭제
    else:
        await ctx.send('롤팟에 있지도 않으신데요 선생님')


@bot.command()
async def 롤멤버(ctx):  # 롤 멤버 리스트 출력
    if len(lol) >= 1:
        member_l = "` `".join(lol) # 리스트 특수문자 없애고 값 사이에 ` ` 출력
        embed = discord.Embed(title='🎮 롤 멤버', color=0x067EDB)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960737976365744198/lol.png')
        embed.add_field(name='현재 인원', value=f'{member_l}', inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send('롤팟이 없넹')


@bot.command()
async def 롤멤버초기화(ctx):
    if lol:
        lol.clear()
        lol_id.clear()
        await ctx.send('롤 멤버 초기화 완료!')
    else:
        await ctx.send('롤팟이 없넹')


# -------------------------------------------------------------------------------------- 로아
@bot.command()
async def 경매(ctx, person, gold):  # 레이드 경매 시스템
    if person == '4':
        buf = 0.7125
    elif person == '8':
        buf = 0.83125
    buf = int(gold) * buf  # 손익분기점
    ssal = buf / 1.1  # 입찰 골드
    if person == '4' or person == '8':
        if ssal < 50:
            if 0 < int(gold) < 50:
                await ctx.send('오.. 님은 **50골**도 안쓰고 입찰하나봐요?')
            elif int(gold) <= 0:
                await ctx.send('ㅋㅋ 생각 조금만 하고 적죠')
            else:
                await ctx.send('**50골**에 입찰하면 될거같은데?')
        else:
            embed = discord.Embed(title='경매 입찰', description=person + '인 레이드', color=0xff0000)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957373143901691987/957612301194756166/gold_coin.png')  # 썸네일
            embed.add_field(name='쌀먹 골드  | ', value=int(ssal), inline=True)  # inline True = 2줄 False = 1줄
            embed.add_field(name='손해 분기점', value=int(buf), inline=True)
            ssal = 0
            person = 0
            buf = 0
            await ctx.send(embed=embed)
    else:
        await ctx.send('**!경매 인원수 경매장가** 순으로 제대로 입력좀')


@bot.command()
async def 빨파초(ctx):
    embed = discord.Embed(title='**📗<📕**', color=0xff0000)
    embed.add_field(name='초록장판', value='빨간구슬',inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975656018921013278/20220516_160353.png')
    await ctx.send(embed=embed)
    embed = discord.Embed(title='**📕<📘**', color=0x0000ff)
    embed.add_field(name='빨강장판', value='파랑구슬',inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975656019193638932/20220516_160414.png')
    await ctx.send(embed=embed)
    embed = discord.Embed(title='**📘<📗**', color=0x00ff00)
    embed.add_field(name='파랑장판', value='초록구슬',inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/957612748978683914/975656019470483506/20220516_160429.png')
    await ctx.send(embed=embed)

@bot.command()
async def 자투리(ctx):  # 자투리 링크버튼
    await buttons.send(
        content="> **자투리 모음**",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label='1. 너도 역겹고, 너도 역겹고, 다 역겨워!',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://youtu.be/NVbJkweLlkw'
                ),
                Button(
                    label='2. 병신짓도 같이하면 괜찮다! 자 드가자~',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://youtu.be/37cpuuzEEcQ'
                )
            ]),
            ActionRow([
                Button(
                    label='3. 화성 갈끄니까~~~ < 짤림 ㅠㅠ',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://youtu.be/2EM_c9HfBWw'
                ),
                Button(
                    label='4. 발탄의 왕',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://www.youtube.com/watch?v=HrQVeFUDA1E'
                )
            ]),
            ActionRow([
                Button(
                    label='5. 오레하만 가면 이상한 사람들',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://www.youtube.com/watch?v=Ul-MsgA_sdM'
                ),
                Button(
                    label='6. 두 줄 깎는 빙수',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://www.youtube.com/watch?v=B_WNJzW7sTM'
                )
            ]),
            ActionRow([
                Button(
                    label='7. 끝도 없이 나오는 영상각',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://youtu.be/10iFkjompu8'
                )
            ]),
            ActionRow([
                Button(
                    label='11. 뭉치면 죽고 떨어지면 산다',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://youtu.be/Oa7anGhvH94'
                )
            ])
        ]
    )


# 자투리 1 => https://youtu.be/NVbJkweLlkw  
# 자투리 2 => https://youtu.be/37cpuuzEEcQ
# 자투리 3 => https://youtu.be/2EM_c9HfBWw
# 자투리 4 => https://www.youtube.com/watch?v=HrQVeFUDA1E
# 자투리 5 => https://www.youtube.com/watch?v=Ul-MsgA_sdM
# 자투리 6 => https://www.youtube.com/watch?v=B_WNJzW7sTM
# 자투리 7 => https://youtu.be/10iFkjompu8
# 자투리 11 => https://youtu.be/Oa7anGhvH94

# ----------------------------------------------------------------------------------------- 프로필
@bot.command()
async def 프로필(ctx, name):
    await ctx.send('프로필 검색중 입니다... 10초정도 소요됩니다')
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name

    char_name = str(name)

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    options.add_argument("window-size=2560x9999") # 세로를 9999로 설정 (headless 모드에서만 작동함)
    url = 'https://lostark.game.onstove.com/Profile/Character/' + char_name

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(url)

    # xpath 값 대입 char_name값은 이미 적고들어옴
    
    char_server = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[1]/span[3]')
    char_attack = driver.find_element("xpath",'//*[@id="profile-ability"]/div[2]/ul/li[1]/span[2]')
    char_atk = char_attack.text
    char_health = driver.find_element("xpath",'//*[@id="profile-ability"]/div[2]/ul/li[2]/span[2]')
    char_hp = char_health.text

    char_stat_crit = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[1]/span[2]') #치명
    char_crit = char_stat_crit.text

    char_stat_special = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[2]/span[2]') #특화
    char_special = char_stat_special.text

    char_stat_dominate = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[3]/span[2]') #제압
    char_dominate = char_stat_dominate.text

    char_stat_swift = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[4]/span[2]') #신속
    char_swift = char_stat_swift.text

    char_stat_endure = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[5]/span[2]') #인내
    char_endure = char_stat_endure.text

    char_stat_expertise = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[6]/span[2]') #숙련
    char_expertise = char_stat_expertise.text
    
    char_total_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[1]/div[1]/span[2]')
    char_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[1]/div[2]/span[2]')
    char_item_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[2]/div[2]/span[2]')
    char_title = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[1]/span[2]')
    char_guild = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[2]/span[2]')
    char_territory = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[4]/span[2]')
    char_territory_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[4]/span[3]')
    char_equip_compass = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[1]/div')
    char_equip_charm = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[2]/div')
    char_equip_emblem = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[3]/div')
    
    char_set = []
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[6]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_weapon = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_weapon_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[1]')
    char_set.append(char_set_1.text) # 무기 세트효과까지 뽑아냄
    equip_weapon = char_equip_weapon.text
    equip_weapon_qual = char_equip_weapon_qual.text

    
    # 무기 정보에서 직업 가져옴
    char_class = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[3]/font')
    class_text_len = len(char_class.text) - 3
    char_class = char_class.text[:class_text_len]

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[1]')
    ActionChains(driver).move_to_element(target).perform() #ActionChains를 통해 movetoelement 구현
    # 마우스 등 특수한 동작 시행시에 액션체인 사용해보는거 나쁘지않을듯
    char_equip_head = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_head_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[2]')
    char_set.append(char_set_2.text) # 머리
    equip_head = char_equip_head.text
    equip_head_qual = char_equip_head_qual.text

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[2]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_shoulder = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_shoulder_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_3 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[6]')
    char_set.append(char_set_3.text) # 어깨
    equip_shoulder = char_equip_shoulder.text
    equip_shoulder_qual = char_equip_shoulder_qual.text

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[3]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_chestpiece = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_chestpiece_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_4 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[3]')
    char_set.append(char_set_4.text) # 상의
    equip_chestpiece = char_equip_chestpiece.text
    equip_chestpiece_qual = char_equip_chestpiece_qual.text

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[4]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_pants = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_pants_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_5 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[4]')
    char_set.append(char_set_5.text) # 하의
    equip_pants = char_equip_pants.text
    equip_pants_qual = char_equip_pants_qual.text

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[5]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_gloves = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_gloves_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_set_6 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[5]')
    char_set.append(char_set_6.text) # 장갑
    equip_gloves = char_equip_gloves.text
    equip_gloves_qual = char_equip_gloves_qual.text
    
    # char_set list에 세트효과가 각각 들어가있음
    # 세트효과 초기화
    set_ji = 0
    set_be = 0
    set_gal = 0
    set_pa = 0
    set_me = 0
    set_sa = 0
    set_ak = 0
    set_han = 0
    set_gu = 0
    char_set_t_1 = ""
    char_set_t_2 = ""
    char_set_t_3 = ""
    char_set_t_4 = ""
    char_set_t_5 = ""
    char_set_t_6 = ""
    char_set_t_7 = ""
    char_set_t_8 = ""
    char_set_t_9 = ""

    for i in char_set:
        if "지배" in i:
            set_ji += 1
            char_set_t_1 = str(set_ji) + "지배"
        elif "배신" in i:
            set_be += 1
            char_set_t_2 = str(set_be) + "배신"
        elif "갈망" in i:
            set_gal += 1
            char_set_t_3 = str(set_gal) + "갈망"
        elif "파괴" in i:
            set_pa += 1
            char_set_t_4 = str(set_pa) + "파괴"
        elif "매혹" in i:
            set_me += 1
            char_set_t_5 = str(set_me) + "매혹"
        elif "사멸" in i:
            set_sa += 1
            char_set_t_6 = str(set_sa) + "사멸"
        elif "악몽" in i:
            set_ak += 1
            char_set_t_7 = str(set_ak) + "악몽"
        elif "환각" in i:
            set_han += 1
            char_set_t_8 = str(set_han) + "환각"
        elif "구원" in i:
            set_gu += 1
            char_set_t_9 = str(set_gu) + "구원"
        else:
            pass
    # x지배 x악몽 출력
    #await ctx.send(char_set_t_1 + char_set_t_2 + char_set_t_3 
    #             + char_set_t_4 + char_set_t_5 + char_set_t_6 
    #             + char_set_t_7 + char_set_t_8 + char_set_t_9)
    char_set_name = char_set_t_1 + char_set_t_2 + char_set_t_3 + char_set_t_4 + char_set_t_5 + char_set_t_6 + char_set_t_7 + char_set_t_8 + char_set_t_9

    #각인 효과
    #char_active_1 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[1]/span')
    #char_active_2 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[2]/span')
    #char_active_3 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[3]/span')
    #char_active_4 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[4]/span')
    #char_active_5 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[5]/span')
    #char_active_6 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]/li[6]/span')
    target = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[2]/div[3]')
    active_1 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[1]')
    #await ctx.send(active_1.text)
    char_active_1 = active_1.text #문제
    target = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[2]/div[3]').click()
    active_2 = driver.find_element("xpath",'//*[@id="profile-ability"]/div[4]/div/div[1]/ul[2]')
    #await ctx.send(char_active.text)
    char_active_2 = active_2.text

    '''# 악세는 안하는게 나을듯?
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[7]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_neck = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_acc_neck_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_neck_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_neck_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_neck_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[8]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ear_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_acc_ear_1_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ear_1_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ear_1_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ear_1_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[9]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ear_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_acc_ear_2_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ear_2_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ear_2_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ear_2_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[10]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ring_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_acc_ring_1_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ring_1_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ring_1_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ring_1_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[11]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ring_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_acc_ring_2_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ring_2_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ring_2_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ring_2_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[14]') 
    ActionChains(driver).move_to_element(target).perform() # 장착 각인
    char_active_1_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[1]')
    char_active_1_value = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[2]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[15]') 
    ActionChains(driver).move_to_element(target).perform() # 장착 각인
    char_active_1_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[1]')
    char_active_1_value = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[2]')

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[13]') 
    ActionChains(driver).move_to_element(target).perform() # 돌
    char_stone_rate = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font') # 돌 등급
    char_stone_active = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[7]') # 돌 효과

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[12]') 
    ActionChains(driver).move_to_element(target).perform() # 팔찌
    char_brace_rate = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font') # 팔찌 등급
    char_brace_active = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[5]') # 팔찌 효과
    '''

    '''
    # 아바타 탭으로 변경
    # 아바타 귀걸이 눈장식등 개수마다 번호가 계속 달라져서 한가지로 못할듯, 전체를 보고 판단하던가, 아바타 탭자체를 없애던가 하는게 편할거같음.
    driver.find_element("xpath",'//*[@id="profile-ability"]/div[1]/div[1]/a[2]').click() 

    char_avartar_islegend = []
    
    target = driver.find_element("xpath",'//*[@id="profile-avatar"]/div[2]/div[1]') 
    ActionChains(driver).move_to_element(target).perform() # 전압 - 무기
    char_avartar_1_grade = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')    
    char_avartar_islegend.append(char_avartar_1_grade.text)
    await ctx.send(char_avartar_islegend[0])

    target = driver.find_element("xpath",'//*[@id="profile-avatar"]/div[2]/div[3]') 
    ActionChains(driver).move_to_element(target).perform() # 전압 - 머리
    char_avartar_2_grade = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_avartar_islegend.append(char_avartar_2_grade.text)
    await ctx.send(char_avartar_islegend[1])
    
    target = driver.find_element("xpath",'//*[@id="profile-avatar"]/div[2]/div[6]') 
    ActionChains(driver).move_to_element(target).perform() # 전압 - 상의
    char_avartar_3_grade = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_avartar_islegend.append(char_avartar_3_grade.text)
    await ctx.send(char_avartar_islegend[2])

    target = driver.find_element("xpath",'//*[@id="profile-avatar"]/div[2]/div[7]') 
    ActionChains(driver).move_to_element(target).perform() # 전압 - 하의
    char_avartar_4_grade = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_avartar_islegend.append(char_avartar_4_grade.text)
    await ctx.send(char_avartar_islegend[3])

    cnt_legend = 0
    cnt_hero = 0
    for i in char_avartar_islegend:
        if "전설" in i:
            cnt_legend += 1
        elif "영웅" in i:
            cnt_hero += 1
        else:
            pass
    await ctx.send(str(cnt_legend) + "전설아바타" + str(cnt_hero) + "영웅아바타")
    '''
    # 카드탭 이동
    driver.find_element("xpath",'//*[@id="profile-ability"]/div[1]/div[1]/a[4]').click()

    # 카드탭은 메모장에 적어놓고 메모장이랑 같으면 효과 나오고 그런식으로 하는게 편할거같음 문자열 안에 세구빛12, 18,30 체크, 암구빛12,18,30 체크, 암바절12,30 체크, 남바절12,30 체크, 세우라제 체크 등 
    char_card = driver.find_element("xpath",'//*[@id="profile-card"]/div[2]/div')
    card_check = char_card.text
    # 세구빛
    if "세상을 구하는 빛" in card_check:
        if "성속성 피해 +8.00%" in card_check:
            char_card = "세구30"
        elif "성속성 피해 +7.00%" in card_check:
            char_card = "세구18"
        elif "공격 속성을 성속성으로 변환" in card_check:
            char_card = "세구12"
        else:
            char_card = "세구N개"
    # 남바절
    elif "남겨진 바람의 절벽" in card_check:
        if "성속성 피해량이 3.5% 증가" in card_check:
            char_card = "남바30"
        elif "치명타 적중률 +7.00%" in card_check:
            char_card = "남바12"
        else:
            char_card = "남바N개"
    # 암구빛
    elif "카제로스의 군단장" in card_check:
        if "암속성 피해 +8.00%" in card_check:
            char_card = "암구30"
        elif "암속성 피해 +7.00%" in card_check:
            char_card = "암구18"
        elif "공격 속성을 암속성으로 변환" in card_check:
            char_card = "암구12"
        else:
            char_card = "암구N개"
    # 암바절 (창달)
    elif "창의 달인" in card_check:
        if "암속성 피해량이 2.5% 증가" in card_check:
            char_card = "창달30"
        else:
            char_card = "창달N개"

    else:
        char_card = "X"

    def gem_check(gem_text):
        if "감소" in gem_text: # 홍염 2~20 1~10레벨
            value = re.sub(r'[^0-9]','',gem_text)
            value = int(value) // 200
            value = str(value) + "홍"

        elif "증가" in gem_text: # 멸화 3~24 1~8레벨 9레벨=30%, 10레벨=40%
            value = re.sub(r'[^0-9]','',gem_text)
            if int(value) < 2500:
                value = int(value) // 300
                value = str(value) + "멸"
            elif int(value) == 3000:
                value = "9멸"
            elif int(value) == 4000:
                value = "10멸"
            else:
                pass
        else:
            pass
        return value

    # 보석 탭 클릭
    driver.find_element("xpath",'//*[@id="profile-ability"]/div[1]/div[1]/a[3]').click()
    
    char_gem_1 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[1]/p') # 1~11번 보석
    char_gem_1_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[1]/p/font')
    char_gem_2 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[2]/p')
    char_gem_2_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[2]/p/font')
    char_gem_3 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[3]/p')
    char_gem_3_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[3]/p/font')
    char_gem_4 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[4]/p')
    char_gem_4_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[4]/p/font')
    char_gem_5 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[5]/p')
    char_gem_5_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[5]/p/font')
    char_gem_6 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[6]/p')
    char_gem_6_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[6]/p/font')
    char_gem_7 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[7]/p')
    char_gem_7_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[7]/p/font')
    char_gem_8 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[8]/p')
    char_gem_8_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[8]/p/font')
    char_gem_9 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[9]/p')
    char_gem_9_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[9]/p/font')
    char_gem_10 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[10]/p')
    char_gem_10_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[10]/p/font')
    char_gem_11 = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[11]/p')
    char_gem_11_name = driver.find_element("xpath",'//*[@id="profile-jewel"]/div/div[2]/div/ul/li[11]/p/font')
    #await ctx.send(gem_check(char_gem.text))
    
    # 왠진 모르지만 selenium으로 가져온 순수 숫자 파일이 카드탭으로 넘어오면서 증발하는 버그 같은게 있음. 다시 다른 변수에 넣어주면서 해결
    page0 = discord.Embed(title='프로필 검색', color=random.choice(colors))
    page0.add_field(name=f'`[닉네임]` : {char_name}\n' + f'`[서버]` : {char_server.text}\n'
                    +f'`[영지이름]` : {char_territory_name.text}\n' + f'`[영지레벨]` : {char_territory.text}\n\n'
                    +f'`[특성]`\n' + f'`[치명]` : {char_crit}\n'
                    +f'`[특화]` : {char_special}\n' + f'`[제압]` : {char_dominate}\n'
                    +f'`[신속]` : {char_swift}\n' + f'`[인내]` : {char_endure}\n'
                    +f'`[숙련]` : {char_expertise}\n'
                    ,value=f'ㅤ', inline=True)
    page0.add_field(name=f'`[직업]` : {char_class}\n' + f'`[칭호]` : {char_title.text}\n'
                    +f'`[공격력]` : {char_atk}\n' + f'`[체력]` : {char_hp}\n\n'
                    +f'`[원정대레벨]` : {char_total_LV.text}\n' + f'`[아이템레벨]` : {char_item_LV.text}\n'
                    +f'`[전투레벨]` : {char_LV.text}\n'
                    ,value=f'ㅤ', inline=True)

    page1 = discord.Embed(title='장비', color=random.choice(colors))
    page1.add_field(name=f'`[머리]` : {equip_head}\n'
                    + f'`[어깨]` : {equip_shoulder}\n'
                    + f'`[상의]` : {equip_chestpiece}\n'
                    + f'`[하의]` : {equip_pants}\n'
                    + f'`[장갑]` : {equip_gloves}\n'
                    + f'`[무기]` : {equip_weapon}\n'
                    ,value=f'ㅤ', inline=True)
    page1.add_field(name=f'`[품질]` : {equip_head_qual}\n'
                    + f'`[품질]` : {equip_shoulder_qual}\n'
                    + f'`[품질]` : {equip_chestpiece_qual}\n'
                    + f'`[품질]` : {equip_pants_qual}\n'
                    + f'`[품질]` : {equip_gloves_qual}\n'
                    + f'`[품질]` : {equip_weapon_qual}\n'
                    + f'`[세트효과]` : {char_set_name}\n'
                    ,value=f'ㅤ', inline=True)
    page2 = discord.Embed(title='카드 & 보석', color=random.choice(colors))
    page2.add_field(name=f'`[{gem_check(char_gem_1.text)}]` : {char_gem_1_name.text}\n'
                    + f'`[{gem_check(char_gem_2.text)}]` : {char_gem_2_name.text}\n'
                    + f'`[{gem_check(char_gem_3.text)}]` : {char_gem_3_name.text}\n'
                    + f'`[{gem_check(char_gem_4.text)}]` : {char_gem_4_name.text}\n'
                    + f'`[{gem_check(char_gem_5.text)}]` : {char_gem_5_name.text}\n'
                    + f'`[{gem_check(char_gem_6.text)}]` : {char_gem_6_name.text}\n'
                    + f'`[{gem_check(char_gem_7.text)}]` : {char_gem_7_name.text}\n'
                    + f'`[{gem_check(char_gem_8.text)}]` : {char_gem_8_name.text}\n'
                    + f'`[{gem_check(char_gem_9.text)}]` : {char_gem_9_name.text}\n'
                    + f'`[{gem_check(char_gem_10.text)}]` : {char_gem_10_name.text}\n'
                    + f'`[{gem_check(char_gem_11.text)}]` : {char_gem_11_name.text}\n'
                    ,value=f'ㅤ', inline=True)
    page2.add_field(name=f'`[장착 카드]` : {char_card}',value=f'ㅤ', inline=False)
    page3 = discord.Embed(title='장착 각인', color=random.choice(colors))
    page3.add_field(name=f'`{char_active_1}`\n`{char_active_2}`',value=f'ㅤ', inline=False)

    pages = [page0,page1,page2,page3]

    message = await ctx.send(embed=page0)

    await message.add_reaction('💡')
    await message.add_reaction('⚔️')
    await message.add_reaction('💎')
    await message.add_reaction('📖')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True: # 리액션에 따른 임베드 출력
        if str(reaction) == '💡':
            i = 0
            await message.edit(embed=pages[i])
        elif str(reaction) == '⚔️':
            i = 1
            await message.edit(embed=pages[i])
        elif str(reaction) == '💎':
            i = 2
            await message.edit(embed=pages[i])
        elif str(reaction) == '📖':
            i = 3
            await message.edit(embed=pages[i])

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=300, check=check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()

    driver.quit()

# -------------------------------------------------------------------------------------- 운세
@bot.command()
async def 운세(ctx,date):
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name
    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    options.add_argument('--window-size=2560x9999')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EC%9A%B4%EC%84%B8'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(url)
    birth = driver.find_element("xpath",'//*[@id="srch_txt"]') # x-path값 대입 (셀레늄 3버전, 4버전 코드다름)
    birth.click()
    birth.clear() # 텍스트창 클릭후 적혀있는 글 제거 후 입력 (크롬 버전에 따라 달랐던거로..)
    birth.send_keys(date)
    btn = driver.find_element("xpath",'//*[@id="fortune_birthCondition"]/div[1]/fieldset/input')
    btn.click()
    driver.implicitly_wait(2) # 버튼 입력 후 element가 나오는 시간 기다리기
    fortune_main = driver.find_element("xpath",'//*[@id="fortune_birthResult"]/dl[1]/dd/strong')
    fortune_sub = driver.find_element("xpath",'//*[@id="fortune_birthResult"]/dl[1]/dd/p')

    fortune_sub_list = fortune_sub.text.split('.')
    ft_sub = '\n'.join(fortune_sub_list)
    embed = discord.Embed(title='🍀 오늘의 운세', color=random.choice(colors))  # 임베드 타이틀 - 섬네일 - 필드 - 푸터 순서 잘지키기
    embed.add_field(name=f'✒️ {fortune_main.text}', value=f'`{ft_sub}`', inline=False)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)

# -------------------------------------------------------------------------------------- 에러처리
@bot.event
async def on_command_error(ctx, error):  # 커맨드 에러
    id = ctx.message.author.id
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'그런 명령어는 없어. 오타가 났는지 확인해봐')
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'<@{id}> 아저씨 쿨타임이야 ㅋㅋ {error.retry_after:.0f}초 남음')


bot.run(token)  # token