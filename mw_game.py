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

    char_name = "그꿈을덧그리며"

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    options.add_argument("window-size=2560x9999") # 세로를 9999로 설정 (headless 모드에서만 작동함)
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
    

    char_set = []
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[1]')
    ActionChains(driver).move_to_element(target).perform() #ActionChains를 통해 movetoelement 구현
    # 마우스 등 특수한 동작 시행시에 액션체인 사용해보는거 나쁘지않을듯
    char_equip_head = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_head_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("머리" + char_equip_head.text + " " + char_equip_head_qual.text)
    char_set_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[2]')
    char_set.append(char_set_2.text) # 머리

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[2]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_shoulder = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_shoulder_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("어깨" + char_equip_shoulder.text + " " + char_equip_shoulder_qual.text)
    char_set_3 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[6]')
    char_set.append(char_set_3.text) # 어깨

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[3]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_chestpiece = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_chestpiece_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("상의" + char_equip_chestpiece.text + " " + char_equip_chestpiece_qual.text)
    char_set_4 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[3]')
    char_set.append(char_set_4.text) # 상의

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[4]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_pants = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_pants_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("하의" + char_equip_pants.text + " " + char_equip_pants_qual.text)
    char_set_5 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[4]')
    char_set.append(char_set_5.text) # 하의

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[5]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_gloves = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_gloves_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("장갑" + char_equip_gloves.text + " " + char_equip_gloves_qual.text)
    char_set_6 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[5]')
    char_set.append(char_set_6.text) # 장갑

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[6]')
    ActionChains(driver).move_to_element(target).perform()
    char_equip_weapon = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    char_equip_weapon_qual = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    await ctx.send("무기" + char_equip_weapon.text + " " + char_equip_weapon_qual.text)
    char_set_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[10]/div[1]/span[1]')
    char_set.append(char_set_1.text) # 무기 세트효과까지 뽑아냄
    
    # 직업
    char_class = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[3]/font')
    class_text_len = len(char_class.text) - 3
    await ctx.send("직업" + char_class.text[:class_text_len])

    # char_set list에 세트효과가 각각 들어가있음
    await ctx.send("세트 효과" + char_set[0])
    await ctx.send("세트 효과" + char_set[1])
    await ctx.send("세트 효과" + char_set[2])
    await ctx.send("세트 효과" + char_set[3])
    await ctx.send("세트 효과" + char_set[4])
    await ctx.send("세트 효과" + char_set[5])
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
    await ctx.send(char_set_t_1 + char_set_t_2 + char_set_t_3 
                 + char_set_t_4 + char_set_t_5 + char_set_t_6 
                 + char_set_t_7 + char_set_t_8 + char_set_t_9)
    
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[7]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_neck = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("목걸이" + char_acc_neck.text)
    char_acc_neck_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_neck_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_neck_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_neck_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    await ctx.send("목걸이 등급" + char_acc_neck_rate.text)
    await ctx.send("목걸이 품질" + char_acc_neck_qual.text)
    await ctx.send("목걸이 특성 " + char_acc_neck_stat.text)
    await ctx.send("목걸이 각인" + char_acc_neck_active.text)
    
    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[8]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ear_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("귀걸이1" + char_acc_ear_1.text)
    char_acc_ear_1_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ear_1_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ear_1_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ear_1_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    await ctx.send("귀걸이1 등급" + char_acc_ear_1_rate.text)
    await ctx.send("귀걸이1 품질" + char_acc_ear_1_qual.text)
    await ctx.send("귀걸이1 특성 " + char_acc_ear_1_stat.text)
    await ctx.send("귀걸이1 각인" + char_acc_ear_1_active.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[9]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ear_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("귀걸이2" + char_acc_ear_2.text)
    char_acc_ear_2_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ear_2_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ear_2_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ear_2_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    await ctx.send("귀걸이2 등급" + char_acc_ear_2_rate.text)
    await ctx.send("귀걸이2 품질" + char_acc_ear_2_qual.text)
    await ctx.send("귀걸이2 특성 " + char_acc_ear_2_stat.text)
    await ctx.send("귀걸이2 각인" + char_acc_ear_2_active.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[10]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ring_1 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("반지1" + char_acc_ring_1.text)
    char_acc_ring_1_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ring_1_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ring_1_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ring_1_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    await ctx.send("반지1 등급" + char_acc_ring_1_rate.text)
    await ctx.send("반지1 품질" + char_acc_ring_1_qual.text)
    await ctx.send("반지1 특성 " + char_acc_ring_1_stat.text)
    await ctx.send("반지1 각인" + char_acc_ring_1_active.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[11]')
    ActionChains(driver).move_to_element(target).perform()
    char_acc_ring_2 = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[1]/p/font')
    await ctx.send("반지2" + char_acc_ring_2.text)
    char_acc_ring_2_rate = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font')
    char_acc_ring_2_qual = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[2]/span[5]/span[1]')
    char_acc_ring_2_stat = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[6]')
    char_acc_ring_2_active = driver.find_element("xpath", '//*[@id="lostark-wrapper"]/div[2]/div[7]')
    await ctx.send("반지2 등급" + char_acc_ring_2_rate.text)
    await ctx.send("반지2 품질" + char_acc_ring_2_qual.text)
    await ctx.send("반지2 특성 " + char_acc_ring_2_stat.text)
    await ctx.send("반지2 각인" + char_acc_ring_2_active.text)
    

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[14]') 
    ActionChains(driver).move_to_element(target).perform() # 장착 각인
    char_active_1_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[1]')
    char_active_1_value = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[2]')
    await ctx.send("장착 각인 1 이름" + char_active_1_name.text)
    await ctx.send("장착 각인 1 값" + char_active_1_value.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[15]') 
    ActionChains(driver).move_to_element(target).perform() # 장착 각인
    char_active_1_name = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[1]')
    char_active_1_value = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/font[2]')
    await ctx.send("장착 각인 2 이름" + char_active_1_name.text)
    await ctx.send("장착 각인 2 값" + char_active_1_value.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[13]') 
    ActionChains(driver).move_to_element(target).perform() # 돌
    char_stone_rate = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font') # 돌 등급
    char_stone_active = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[7]') # 돌 효과
    await ctx.send("돌 등급" + char_stone_rate.text)
    await ctx.send("돌 효과" + char_stone_active.text)

    target = driver.find_element("xpath",'//*[@id="profile-equipment"]/div[2]/div[12]') 
    ActionChains(driver).move_to_element(target).perform() # 팔찌
    char_brace_rate = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[2]/span[2]/font/font') # 팔찌 등급
    char_brace_active = driver.find_element("xpath",'//*[@id="lostark-wrapper"]/div[2]/div[5]') # 팔찌 효과
    await ctx.send("팔찌 등급" + char_brace_rate.text)
    await ctx.send("팔찌 효과" + char_brace_active.text)
    '''

    # 아바타 탭으로 변경
    driver.find_element("xpath",'//*[@id="profile-ability"]/div[1]/div[1]/a[2]').click() 

    char_avartar_islegend = []
    # 아바타 귀걸이 눈장식등 개수마다 번호가 계속 달라져서 한가지로 못할듯, 전체를 보고 판단하던가, 아바타 탭자체를 없애던가 하는게 편할거같음.
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
    await ctx.send(char_card.text)
    '''
    # 카드 보석 스킬렙 트포 룬 내실개수 원정대 selectmenu 로딩메세지
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