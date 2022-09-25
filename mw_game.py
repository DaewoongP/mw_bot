import asyncio, discord
import random
import numpy as np
import time
# from discord.ui import Button, View
from discord.ext import commands
from discord_buttons_plugin import *

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# opencv
import cv2

import re


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

token_text = open("C:\\Users\\qsc14\\Desktop\\discord\\token\\mw_game_bot_token.txt", 'r')
token = token_text.readline() #토큰을 로컬 텍스트에서 가져옴

# discord bot developer portal 에서 message content intent (ON) 설정 이후 True 까지 해줘야 command가 돌아감
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='#', intents=intents, help_command=None) # 전처리 기호
buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
    print('We have loggedd in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.dnd,#online, idle, dnd, offline
                              activity=discord.Game(name='코드짜는중'))


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
        rf += 1  # 강화 수치 증가 (성공)

        channel = bot.get_channel(323766857708470272)
        embed = discord.Embed(title='```강화 성공 !!```', color=rf_effect)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
        embed.add_field(name='강화 확률', value=f'{success * 100}%', inline=True)
        embed.add_field(name='강화 상태', value=f'{rf} => {rf + 1}', inline=False)
        embed.add_field(name='누른 횟수', value=f'{rf_try}번 만에 성공', inline=True)
        await ctx.send(embed=embed)

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
            rf -= 1 # 강화 수치 하락 (실패)

            channel = bot.get_channel(323766857708470272)
            embed = discord.Embed(title='```강화 하락 ㄷㄷ```', color=rf_effect)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/957612748978683914/960451886740291624/unknown.png')
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
            embed.add_field(name='이전 강화 수치', value=f'{rf}강', inline=True)
            embed.add_field(name='하락 확률', value=f'{success * 100}%', inline=True)
            embed.add_field(name='강화 상태', value=f'{rf} => {rf - 1}', inline=False)
            embed.add_field(name='누른 횟수', value=f'{rf_try}번이나 눌렀는데 떨어짐 ㅠ', inline=True)
            await ctx.send(embed=embed)


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


    
@bot.event
async def on_ready():
    print('We have loggedd in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name='!도움 / 이벤트'))




bot.run(token)  # token