import asyncio, discord
from msilib.schema import Component
from logging import PlaceHolder
from email.policy import default
import random
import interactions
import numpy as np
import time
from discord.ui import Select, View
from discord.ext import commands
from discord_buttons_plugin import *

# pip install discord-py-interactions
from interactions import Modal, TextInput, TextStyleType, Button, CommandContext, ComponentContext
# pip install nextcord
from nextcord.ext import commands
import nextcord


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
#------------------------------------------------------------------

@bot.command()
async def test(ctx):
    select = Select(
        placeholder= "원정대 내 캐릭터를 선택할 수 있어요!",
        options=[
        discord.SelectOption(
            label="1", 
            emoji="🎉", 
            description = "test.1",
            #default=True # 가장 처음에 표시되는 값 설정 가능.
        ),
        discord.SelectOption(
            label="2", 
            emoji="🎮", 
            description = "test.2")
    ])

    async def my_callback(interaction):
        await interaction.response.send_message(f"테스트성공 {select.values}")
        await ctx.send(view = view)

    select.callback = my_callback # 콜백 설정
    view = View()
    view.add_item(select)

    await ctx.send(view = view)



@bot.slash_command(
    name="테스트",
    description="테스트중",
    guild_ids=[957373143406755840],
)
async def 테스트(ctx):
    pass

# ---------------------------------------------------------------- modal test
class search_char(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("프로필")  # Modal title

        # Create a text input and add it to the modal
        self.name = nextcord.ui.TextInput(
            label="프로필 검색 (오류뜨면 전송 한번 더눌러주세요!)",
            placeholder="검색할 닉네임을 입력해주세요!",
            min_length=2,
            max_length=12,
        )
        self.add_item(self.name)
        '''
        # Create a long text input and add it to the modal
        self.description = nextcord.ui.TextInput(
            label="Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Information that can help us recognise your pet",
            required=False,
            max_length=1800,
        )
        self.add_item(self.description)
        '''
    async def callback(self, interaction: nextcord.Interaction) -> None:

        
        #This is the function that gets called when the submit button is pressed
        # 옵션 생성
        options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        options.add_argument("headless")
        options.add_argument("window-size=2560x9999") # 세로를 9999로 설정 (headless 모드에서만 작동함)
        char_name = self.name.value
        url = 'https://iloa.gg/character/' + char_name
        msg = await interaction.channel.send(f'`{char_name}` 캐릭터 검색을 시작합니다.\n 10초 정도 걸릴 수 있습니당')
        
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.implicitly_wait(5)
        driver.get(url)
        
    
        # 원정대 캐릭터 확인
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[4]/div[2]/div[1]/span[5]').click()
        time.sleep(2)
        char_all_3 = driver.find_element("xpath",'//*[@id="test"]')
        char_all_3.screenshot('screen_all_3.png')

        # 스샷 (기본창)
        #char_all_1 = driver.find_element("xpath",'//*[@id="__next"]/div/main/div')
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[3]/div/div[1]/div/div[3]/span').click()
        driver.implicitly_wait(5)
        time.sleep(2)
        # 끌부분 클릭
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[4]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[5]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[6]/label/span').click()
        char_all_1 = driver.find_element("xpath",'//*[@id="screenshot"]')
        char_all_1.screenshot('screen_all_1.png')
        # 꺼져있던부분 클릭
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[4]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[5]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[6]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[7]/label/span').click()
        # 원래부분 삭제
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[1]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/label/span').click()
        driver.find_element("xpath",'//*[@id="__next"]/div/main/div/div/div[2]/div/div/div[1]/div[1]/div[3]/label/span').click()
        time.sleep(2)
        char_all_2 = driver.find_element("xpath",'//*[@id="screenshot"]')
        char_all_2.screenshot('screen_all_2.png')

        driver.quit()

        # 이미지 확대 
        '''
        img_char = cv2.imread('screen_all_1.png')
        img_2x = cv2.resize(img_char, None, fx=1.35, fy=1, interpolation = cv2.INTER_CUBIC)
        cv2.imwrite('screen_all_2.png', img_2x)
        '''
        class ViewWithButton(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='1')
            async def button_1(self, button: discord.ui.Button, interaction: discord.Interaction):
                with open('screen_all_1.png', 'rb') as f:
                    picture = discord.File(f)
                    await msg.edit(file=picture)
            @discord.ui.button(style=discord.ButtonStyle.blurple, label='2')
            async def button_2(self, button: discord.ui.Button, interaction: discord.Interaction):
                with open('screen_all_2.png', 'rb') as f:
                    picture = discord.File(f)
                    await msg.edit(file=picture)

            @discord.ui.button(style=discord.ButtonStyle.blurple, label='3')
            async def button_3(self, button: discord.ui.Button, interaction: discord.Interaction):
                with open('screen_all_3.png', 'rb') as f:
                    picture = discord.File(f)
                    await msg.edit(file=picture)
                '''
                select = Select(
                    placeholder= "원정대 내 캐릭터를 선택할 수 있어요!",
                    options=[
                    discord.SelectOption(
                        label="1", 
                        emoji="🎉", 
                        description = "test.1",
                        #default=True # 가장 처음에 표시되는 값 설정 가능.
                    ),
                    discord.SelectOption(
                        label="2", 
                        emoji="🎮", 
                        description = "test.2")
                ])
                

                async def my_callback(interaction):
                    #await interaction.response.send_message(f"테스트성공 {select.values}")
                    await char_msg.edit(view = ViewWithButton())

                select.callback = my_callback # 콜백 설정
                view = View()
                view.add_item(select)

                char_msg = await interaction.send(view = view)
                '''


        # 이미지 출력 부
        with open('screen_all_1.png', 'rb') as f:
            picture = discord.File(f)
            await msg.edit(file=picture, view = ViewWithButton())

        await asyncio.sleep(120)
        await msg.delete()
        


@bot.slash_command(
    name="프로필",
    description="로스트아크 프로필 검색",
    guild_ids=[957373143406755840],
)
async def send(interaction: nextcord.Interaction):
    # sending the modal on an interaction (can be slash, buttons, or select menus)
    modal = search_char()
    await interaction.response.send_modal(modal)
    


#------------------------------------------------------------------

    
@bot.event
async def on_ready():
    print('We have loggedd in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name='!도움 / 이벤트'))




bot.run(token)  # token