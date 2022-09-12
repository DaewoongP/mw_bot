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
async def test(ctx):
    user = ctx.message.author.nick
    id = ctx.message.author.id  # id 가져오기
    if user == None:
        user = ctx.message.author.name

    char_name = "챠화비"

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    #options.add_argument("headless")
    #options.add_argument("window-size=2560x9999") # 세로를 9999로 설정 (headless 모드에서만 작동함)
    url = 'https://lostark.game.onstove.com/Profile/Character/' + char_name

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(url)

    # xpath 값 대입 char_name값은 이미 적고들어옴
    '''
    char_server = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[1]/span[3]')
    await ctx.send("서버"+char_server.text)
    char_atk = driver.find_element("xpath",'//*[@id="profile-ability"]/div[2]/ul/li[1]/span[2]')
    await ctx.send("공격력"+char_atk.text)
    char_hp = driver.find_element("xpath",'//*[@id="profile-ability"]/div[2]/ul/li[2]/span[2]')
    await ctx.send("체력"+char_hp.text)

    char_stat_crit = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[1]/span[2]') #치명
    await ctx.send("치명" + char_stat_crit.text)
    char_stat_special = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[2]/span[2]') #특화
    await ctx.send("특화" + char_stat_special.text)
    char_stat_dominate = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[3]/span[2]') #제압
    await ctx.send("제압"+char_stat_dominate.text)
    char_stat_swift = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[4]/span[2]') #신속
    await ctx.send("신속"+char_stat_swift.text)
    char_stat_endure = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[5]/span[2]') #인내
    await ctx.send("인내"+char_stat_endure.text)
    char_stat_expertise = driver.find_element("xpath",'//*[@id="profile-ability"]/div[3]/ul/li[6]/span[2]') #숙련
    await ctx.send("숙련"+char_stat_expertise.text)
    
    char_total_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[1]/div[1]/span[2]')
    await ctx.send("원정대"+char_total_LV.text)
    char_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[1]/div[2]/span[2]')
    await ctx.send("전투레벨"+char_LV.text)
    char_item_LV = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[2]/div[2]/span[2]')
    await ctx.send("템레벨"+char_item_LV.text)
    char_title = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[1]/span[2]')
    await ctx.send("칭호"+char_title.text)
    char_guild = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[2]/span[2]')
    await ctx.send("길드"+char_guild.text)
    char_territory = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[4]/span[2]')
    await ctx.send("영지레벨"+char_territory.text)
    char_territory_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[3]/div[4]/span[3]')
    await ctx.send("영지이름"+char_territory_name.text)
    char_equip_compass = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[1]/div')
    await ctx.send("나침반"+char_equip_compass.text)
    char_equip_charm = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[2]/div')
    await ctx.send("부적"+char_equip_charm.text)
    char_equip_emblem = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[1]/div[4]/div/ul/li[3]/div')
    await ctx.send("문장"+char_equip_emblem.text)
    '''
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[1]')
    driver.move_To_Element(target).perform()#
    char_equip_head = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("머리" + char_equip_head.text)
    

    '''
    char_equip_shoulder = driver.find_element("xpath",'')
    await ctx.send("어깨" + char_equip_shoulder.text)
    char_equip_chestpiece = driver.find_element("xpath",'')
    await ctx.send("상의" + char_equip_chestpiece.text)
    char_equip_pants = driver.find_element("xpath",'')
    await ctx.send("하의" + char_equip_pants.text)
    char_equip_gloves = driver.find_element("xpath",'')
    await ctx.send("장갑" + char_equip_gloves.text)
    char_equip_weapon = driver.find_element("xpath",'')
    await ctx.send("무기" + char_equip_weapon.text)
    char_class = driver.find_element("xpath",'')
    await ctx.send("직업" + char_class.text)
    '''
    
    driver.quit()
    


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
    driver.quit()

@bot.event
async def on_ready():
    print('We have loggedd in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name='!도움 / 이벤트'))




bot.run(token)  # token