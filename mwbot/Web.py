import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import random
import time
import All


def wait(driver):
    time.sleep(random.uniform(3, 5))
    driver.implicitly_wait(5)


def start(client, commands):
    @client.hybrid_command(name="test", with_app_command=True, description="테스트.")
    async def test(ctx: commands.Context):
        driver_path = os.path.join(os.path.dirname(__file__), "..", "chromedriver-win64", "chromedriver.exe")
        url = 'https://machugi.io/quiz/y1snte0ZeKpzd3W8diZm'

        options = webdriver.ChromeOptions()
        options.add_argument("webdriver.chrome.driver=" + driver_path)

        options.add_argument('window-size=1920,1080')
        options.add_experimental_option("detach", True)  # 화면안꺼지게

        # options.add_argument("--disable-blink-features=AutomationControlled")  # 위험한 옵션일 수도 있음.
        # options.add_argument("disable-gpu")  # 가속 사용 x
        options.add_argument("lang=ko_KR")
        options.headless = False  # 화면 ON
        options.add_argument('incognito')  # 시크릿모드

        driver = webdriver.Chrome(options=options)
        driver.get(url=url)
        driver.implicitly_wait(5)

        # 몇개 풀지 선택하는 옵션들
        buttons = driver.find_element(By.XPATH, '/html/body/div/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]')
        buttons_in_container = buttons.find_elements(By.XPATH, './/button')
        driver.implicitly_wait(5)
        button_list = list()
        for button in buttons_in_container:
            button_list.append(button.get_attribute("aria-label"))

        message = await ctx.send('버튼 선택')
        button_index_num = 0
        button_string = ''
        for b in button_list:
            button_string += f'{button_index_num + 1}. ' + b + " "
            await message.edit(content=button_string)
            await message.add_reaction(All.emoji[button_index_num])
            button_index_num += 1

        driver.close()
        