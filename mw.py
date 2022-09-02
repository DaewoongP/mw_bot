import asyncio, discord
import random
import numpy as np
# from discord.ui import Button, View
from discord.ext import commands
from discord_buttons_plugin import *

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# opencv
import cv2

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

bot = discord.Client()

token_text = open("C:\\Users\\qsc14\\Desktop\\discord\\token\\mw_token.txt", 'r')
token = token_text.readline() #토큰을 로컬 텍스트에서 가져옴

bot = commands.Bot(command_prefix='!') # 전처리 기호
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

# ---------------------------- 메
@bot.command()
async def 메(ctx):
    await buttons.send(
        content="**-메-**",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label='GM 머의 패치노트',
                    style=ButtonType().Link,  # Primary , Success, Secondary, Danger, Link
                    url='https://languid-worm-c54.notion.site/1d0b72f5c57a44caa5344b96dad7e68b'
                )
            ])
        ]
    )



# -------------------------------------------------------------------------------------- 기본
# 역할 신 944955777968398407
# 역할 테스트서버 957815491299278849
# 역할 머웅투르 공방 960456596037705838
@bot.command()
@commands.has_role(957815491299278849)
async def qwerpoiu(ctx, n):
    f = open('C:\\Users\\qsc14\\Desktop\\discord\\test.txt', 'r')
    line = f.readlines()
    await ctx.send(line[int(n) - 1])  # 텍스트 라인 읽기
    f.close()


@bot.command()
async def 이모티콘(ctx):
    await ctx.send('**이모티콘 목록 클릭하면 잘보입니다.**')
    await ctx.send('https://cdn.discordapp.com/attachments/957612748978683914/958425378517553222/unknown.png')


@bot.command()
async def 패치노트(ctx):
    embed = discord.Embed(title='📖 머웅 봇 v2.2 패치노트', color=random.choice(colors))
    # 📕📘📙📗
    embed.add_field(name='📕 1. `!프로필` 기능 불가', value='`로아와 십새끼`', inline=False)
    embed.add_field(name='📘 2. `버그 개선`', value='`진짜 개선함`', inline=False)
    embed.add_field(name='📙 3. `이모티콘 개선`', value='괄호 삭제 및 `로아콘` 명칭 삭제', inline=False)
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
@commands.cooldown(1, 600, commands.BucketType.user)
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
    jangi = float(text_file[rf_id + 2])  # 장기 수치 => str
    f.close()  # 파일 읽기 종료

    # 강화 상태에 따른 확률 설정값
    rf_effect = 0x000000
    if rf < 3:
        success = 1
        rf_effect = 0x000000
    elif rf < 6:
        success = 0.9
        rf_effect = 0x000000
    elif rf < 9:
        success = 0.6
        rf_effect = 0xff0000
    elif rf < 11:
        success = 0.3
        rf_effect = 0xff8c00
    elif rf < 13:
        success = 0.2
        rf_effect = 0xffff00
    elif rf < 15:
        success = 0.1
        rf_effect = 0x008000
    elif rf < 17:
        success = 0.04
        rf_effect = 0x0033ff
    elif rf < 19:
        success = 0.03
        rf_effect = 0x4b0082
    elif rf < 21:
        success = 0.015
        rf_effect = 0x800080
    elif rf < 23:
        success = 0.01
        rf_effect = 0xff8c00
    elif rf < 25:
        success = 0.005
        rf_effect = 0x7d0328
    elif rf == 25:
        await ctx.send('25강에 이미 도착하셨네요! 에스더 강화 패치를 기대해주세요 ^^')
        await ctx.send('`!강화확인`을 통해서 자신의 강화상태를 확인 가능합니다')

    if jangi == 100:
        success = 1

    # 강화 상태 메세지
    rf_name = ['강화 성공', '강화 실패']
    level = np.random.choice(rf_name, p=[success, 1 - success])  # 강화 상태

    # 강화 성공?
    if level == rf_name[0]:
        embed = discord.Embed(title='```강화 성공 !!```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='이전 강화 수치', value=f'<@{id}> : {rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf + 1}', inline=False)
        embed.add_field(name='장인의 기운', value=f'{jangi:.2f}%에서 성공', inline=True)
        await ctx.send(embed=embed)
        jangi = 0
        rf += 1  # 강화 수치 증가 (성공)
        if rf >= 19: # 19강부터 강화성공시 비틱
            channel = bot.get_channel(323766857708470272)
            embed = discord.Embed(title='```강화 성공 !!```', color=rf_effect)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='이전 강화 수치', value=f'<@{id}> : {rf}강', inline=True)
            embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
            embed.add_field(name='강화 상태', value=f'{rf} => {rf}', inline=False)
            await channel.send(embed=embed)


    # 강화 실패?
    else:
        # ------------------ 장인의 기운 시스템
        jangi_percent = success * 100 * 0.465
        jangi += float(jangi_percent)
        # 장기백 확인
        if jangi >= 100:
            jangi = 100

        embed = discord.Embed(title='```강화 실패 ㅠㅠ```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='현재 강화 수치', value=f'{rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf}', inline=False)
        embed.add_field(name='장인의 기운', value=f'{jangi:.2f}%', inline=True)
        await ctx.send(embed=embed)

    text_file[rf_id + 1] = str(f'{rf}\n')  # str \n 형태로 강화 수치값 넣어주기
    text_file[rf_id + 2] = str(f'{jangi:.2f}\n')  # 마찬가지로 장기백값 넣어주기
    f = open('C:\\Users\\qsc14\\Desktop\\discord\\rf.txt', 'w')
    f.writelines(text_file)
    f.close()


@bot.command()
async def 강화확인(ctx):
    # 명령어 입력한 사람 id, 강화 수치 가져오기
    id = ctx.message.author.id  # id 가져오기
    f = open('C:\\Users\\qsc14\\Desktop\\discord\\rf.txt', 'r')
    text_file = f.readlines()
    if f'{id}\n' not in text_file:
        await ctx.send('```!강화 부터 하고 확인해줘```')
    rf_id = text_file.index(f'{id}\n')  # 텍스트파일 id의 위치
    rf = int(text_file[rf_id + 1])  # id에 따른 강화수치 => str
    jangi = float(text_file[rf_id + 2])  # 장기 수치 => str
    f.close()  # 파일 읽기 종료
    # -------------------------------------확률표
    rf_effect = 0x000000
    if rf < 3:
        success = 1
        rf_effect = 0x000000
    elif rf < 6:
        success = 0.9
        rf_effect = 0x000000
    elif rf < 9:
        success = 0.6
        rf_effect = 0xff0000
    elif rf < 11:
        success = 0.3
        rf_effect = 0xff8c00
    elif rf < 13:
        success = 0.2
        rf_effect = 0xffff00
    elif rf < 15:
        success = 0.1
        rf_effect = 0x008000
    elif rf < 17:
        success = 0.04
        rf_effect = 0x0033ff
    elif rf < 19:
        success = 0.03
        rf_effect = 0x4b0082
    elif rf < 21:
        success = 0.015
        rf_effect = 0x800080
    elif rf < 23:
        success = 0.01
        rf_effect = 0xff8c00
    elif rf < 25:
        success = 0.005
        rf_effect = 0x7d0328
    elif rf == 25:
        success = 0
        rf_effect = 0xffffff
    else:
        await ctx.send('잘못입력했어!')

    # ---------------------------------------
    embed = discord.Embed(title='```현재 강화 확인```', color = rf_effect)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name='현재 강화 수치', value=f'{rf}강', inline=True)
    embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
    embed.add_field(name='장인의 기운', value=f'{jangi:.2f}%', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 강화확률(ctx, k):
    n = int(k)
    if n < 3:
        await ctx.send('`100%`')
    elif n < 6:
        await ctx.send('`90%`')
    elif n < 9:
        await ctx.send('`60%`')
    elif n < 11:
        await ctx.send('`30%`')
    elif n < 13:
        await ctx.send('`20%`')
    elif n < 15:
        await ctx.send('`10%`')
    elif n < 17:
        await ctx.send('`4%`')
    elif n < 19:
        await ctx.send('`3%`')
    elif n < 21:
        await ctx.send('`1.5`%')
    elif n < 23:
        await ctx.send('`1%`')
    elif n < 25:
        await ctx.send('`0.5%`')
    elif n == 25:
        await ctx.send('25강이 끝이야')
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
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
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
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='🤔 뒷면!', color=0x000000)  # result의 팀을 각각 embed로 출력
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/963302395062931486/doge_black.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
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


# ----------------------------------------------------------------------------------------- 프로필
@bot.command()
async def 프로필(ctx, char_name):
    await ctx.send('현재 로아와에서 봇을 막아버려서 기능이 안됩니다 ㅜㅜ')
    '''
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name

    char_chk = "캐릭터 정보가 없습니다"

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    options.add_argument("window-size=2560x9999") # 세로를 9999로 설정 (headless 모드에서만 작동함)
    url = 'https://loawa.com/char/'
    name = str(char_name)
    url = url + name
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.implicitly_wait(5)
    
    # 캐릭터 존재 확인
    try:
        await ctx.send(f'`{char_name}` 캐릭터 검색을 시작합니다.')
        btn = driver.find_element_by_xpath('//*[@id="im_box"]/div/div[1]/button[2]')
        btn.click()
        driver.implicitly_wait(2)
        #스킬부 없애기
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[7]').click()
        driver.implicitly_wait(1)
        #char_all = driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]')
        #char_all.screenshot('screen_all.png')
        #카드,각인,보석 없애기
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[6]').click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[5]').click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[4]').click()
        driver.implicitly_wait(1)
        #스샷 1
        char_all_1 = driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]')
        char_all_1.screenshot('screen_all_1.png')
        #카드각인보석 복구
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[6]').click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[5]').click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[4]').click()
        driver.implicitly_wait(1)
        #장비 없애기
        driver.find_element_by_xpath('//*[@id="im_box"]/div/div[3]/div[2]/div[1]/div/label[3]').click()
        driver.implicitly_wait(1)
        #스샷 2
        char_all_2 = driver.find_element_by_xpath('//*[@id="char-card-body"]/div[2]')
        char_all_2.screenshot('screen_all_2.png')

        # 이미지 확대 
        img_char = cv2.imread('screen_all_1.png')
        img_2x = cv2.resize(img_char, None, fx=1.35, fy=1, interpolation = cv2.INTER_CUBIC)
        cv2.imwrite('screen_all_1.png', img_2x)

        # 이미지 출력 부
        with open('screen_all_1.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        with open('screen_all_2.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

    except:
        await ctx.send('오타가 났거나 캐릭터 갱신 중이니 다시 검색해봐')
    '''

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
    driver.implicitly_wait(1)
    driver.get(url)
    birth = driver.find_element_by_xpath('//*[@id="srch_txt"]') # x-path값 대입
    birth.click()
    birth.clear() # 텍스트창 클릭후 적혀있는 글 제거 후 입력 (크롬 버전에 따라 달랐던거로..)
    birth.send_keys(date)
    btn = driver.find_element_by_xpath('//*[@id="fortune_birthCondition"]/div[1]/fieldset/input')
    btn.click()

    #while(True): # 크롬창 확인
    #	pass

    fortune_main = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/strong')
    #await ctx.send(fortune_main.text)
    fortune_sub = driver.find_element_by_xpath('//*[@id="fortune_birthResult"]/dl[1]/dd/p')
    #await ctx.send(fortune_sub.text)
    fortune_sub_list = fortune_sub.text.split('.')
    ft_sub = '\n'.join(fortune_sub_list)
    embed = discord.Embed(title='🍀 오늘의 운세', color=random.choice(colors))  # 임베드 타이틀 - 섬네일 - 필드 - 푸터 순서 잘지키기
    embed.add_field(name=f'✒️ {fortune_main.text}', value=f'`{ft_sub}`', inline=False)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
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