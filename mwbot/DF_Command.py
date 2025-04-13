import All
import json
from datetime import datetime

def is_valid_date(date_str):
    try:
        # YYMMDD 형식인지 확인
        if len(date_str) != 6 or not date_str.isdigit():
            return False
        
        # 날짜 파싱 시도
        datetime.strptime(date_str, "%y%m%d")
        return True
    except ValueError:
        return False

def subtract_one_minute(time_str):
    from datetime import datetime, timedelta

    # 문자열 → datetime 객체로 변환
    time_obj = datetime.strptime(time_str, "%H%M")

    # 1분 빼기
    new_time = time_obj - timedelta(minutes=1)

    # 다시 문자열로 반환
    return new_time.strftime("%H%M")

def start(client, DF, commands, discord):
    @client.hybrid_command(name="던파등록", with_app_command=True, description="내 캐릭터를 태초 알람에 등록합니다.")
    async def command_notice(ctx: commands.Context, server_name, character_name):

        # 한글 서버 이름에서 영어 서버 이름으로 변환
        response_server_name = All.df_server_name(server_name)
        if response_server_name == "":
            await ctx.send("잘못된 서버 이름입니다.")
            return # 오류

        # DFCharacters.txt
        characterID = DF.get_character_id(f"servers/{response_server_name}/characters?characterName={character_name}", "characterId")
        # register
        if DF.register_character(response_server_name, character_name, characterID) == True:
            ### embed
            embed = discord.Embed(
                title="-던- 캐릭터 등록",
                description=f"[{server_name}]({character_name}) 등록 완료!",
                color=All.random.choice(All.colors)
            )
        
            # 보낸사람의 이름, 썸넬이 임베드에 보이게됨.
            embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
            ### ~embed
        else:
            await ctx.send("이미 등록된 캐릭터 이름이거나, 잘못된 캐릭터 이름입니다.")
    
    @client.hybrid_command(name="오늘태초", with_app_command=True, description="오늘 태초 먹은사람이 있는지 체크합니다.")
    async def command_today_bitic(ctx: commands.Context):
        char_list = DF.get_characters()
        # current date
        today_str = datetime.today().strftime('%Y%m%d')
        current_time = subtract_one_minute(datetime.today().strftime('%H%M')) # 1분빼서 확인

        # 504	아이템 획득(항아리&상자)
        # 505	아이템 획득(던전 드랍)
        # 506	아이템 획득(조각 교환)
        # 507	아이템 획득(레이드 카드 보상)
        # 508	아이템 획득(상점)

        code_list = [505, 507]
        
        data_limit = 100

        # --->> debug timeline
        open("DFTimeline.txt", 'w', encoding='utf-8').close() # txt생성 후 바로 닫으면 빈파일로 초기화
        timelinefile = open("DFTimeline.txt", 'a', encoding='utf-8')
        # ---<<

        bitic_list = list()

        for char in char_list:
            item_list = list()
            for code in code_list:
                timelinedata = DF.get_timeline(
                    f"servers/{char[0]}" +
                    f"/characters/{char[1]}" +
                    f"/timeline" +
                    f"?limit={data_limit}" +
                    f"&code={code}" +
                    f"&startDate={today_str}T0000" +
                    f"&endDate={today_str}T{current_time}")
                    #f"&startDate={today_str}T0000" +
                    #f"&endDate={today_str}T{current_time}")
                item_list.extend(timelinedata)
                # --->> debug timeline
                if 0 < len(timelinedata):
                    timelinefile.write(f"[{char[2]}] ---------->\n")
                    json.dump(timelinedata, timelinefile, ensure_ascii=False, indent=4) # json데이터 바로 저장
                    timelinefile.write(f"\n")
                # ---<<
            numitem_regendery = 0
            numitem_epic = 0
            numitem_bitic = 0
            numitem_total = 0
            for item in item_list:
                if item['data']['itemRarity'] == "레전더리":
                    numitem_regendery += 1
                    numitem_total += 1
                elif item['data']['itemRarity'] == "에픽":
                    numitem_epic += 1
                    numitem_total += 3
                elif item['data']['itemRarity'] == "태초":
                    numitem_bitic += 1
                    numitem_total += 10 # 포인트제 훈쌤 요청
            bitic_list.append((char[2], numitem_total, numitem_regendery, numitem_epic, numitem_bitic))

        bitic_list.sort(key=lambda x: x[1], reverse=True)
        embed = discord.Embed(
            title=f"[오늘 태초 리스트] - {today_str}",
            color=All.random.choice(All.colors)
        )
        
        for bitic_item in bitic_list:
            embed.add_field(name=f"{bitic_item[0]} - {bitic_item[1]}pt", value=f"레전 : {bitic_item[2]}, 에픽 : {bitic_item[3]}, 태초 : {bitic_item[4]}", inline=True)

        embed.set_footer(text=f"검색 반영까지 최대 1분 소요, 던전 & 카드 기준으로 출력")
        await ctx.send(embed=embed)
        

    @client.hybrid_command(name="언제태초", with_app_command=True, description="특정 날짜 태초 먹은사람이 있는지 체크합니다.\n/언제태초 250401")
    async def command_bitic(ctx: commands.Context, when_bitic):
        char_list = DF.get_characters()
        # current date
        if False == is_valid_date(when_bitic):
            await ctx.send("날짜 입력이 잘못되었습니다. ('250401' 형태로 입력)")
            return

        # 20250401 형태로 수정
        when_bitic = "20" + when_bitic

        if datetime.today().strftime('%Y%m%d') ==  when_bitic:
            await ctx.send("오늘 날짜는 오늘태초로 입력해주세요.")
            return

        # 504	아이템 획득(항아리&상자)
        # 505	아이템 획득(던전 드랍)
        # 506	아이템 획득(조각 교환)
        # 507	아이템 획득(레이드 카드 보상)
        # 508	아이템 획득(상점)

        code_list = [505, 507]
        
        data_limit = 100

        # --->> debug timeline
        open("DFTimeline.txt", 'w', encoding='utf-8').close() # txt생성 후 바로 닫으면 빈파일로 초기화
        timelinefile = open("DFTimeline.txt", 'a', encoding='utf-8')
        # ---<<

        bitic_list = list()

        for char in char_list:
            item_list = list()
            for code in code_list:
                timelinedata = DF.get_timeline(
                    f"servers/{char[0]}" +
                    f"/characters/{char[1]}" +
                    f"/timeline" +
                    f"?limit={data_limit}" +
                    f"&code={code}" +
                    f"&startDate={when_bitic}T0000" +
                    f"&endDate={when_bitic}T2359")
                item_list.extend(timelinedata)
                # --->> debug timeline
                if 0 < len(timelinedata):
                    timelinefile.write(f"[{char[2]}] ---------->\n")
                    json.dump(timelinedata, timelinefile, ensure_ascii=False, indent=4) # json데이터 바로 저장
                    timelinefile.write(f"\n")
                # ---<<
                
            numitem_regendery = 0
            numitem_epic = 0
            numitem_bitic = 0
            numitem_total = 0

            for item in item_list:
                if item['data']['itemRarity'] == "레전더리":
                    numitem_regendery += 1
                    numitem_total += 1
                elif item['data']['itemRarity'] == "에픽":
                    numitem_epic += 1
                    numitem_total += 3
                elif item['data']['itemRarity'] == "태초":
                    numitem_bitic += 1
                    numitem_total += 10 # 포인트제 훈쌤 요청
            bitic_list.append((char[2], numitem_total, numitem_regendery, numitem_epic, numitem_bitic))

        bitic_list.sort(key=lambda x: x[1], reverse=True)
        embed = discord.Embed(
            title=f"[{when_bitic} 태초 리스트]",
            color=All.random.choice(All.colors)
        )
        
        for bitic_item in bitic_list:
            embed.add_field(name=f"{bitic_item[0]} - {bitic_item[1]}pt", value=f"레전 : {bitic_item[2]}, 에픽 : {bitic_item[3]}, 태초 : {bitic_item[4]}", inline=True)

        embed.set_footer(text=f"검색 반영까지 최대 1분 소요, 던전 & 카드 기준으로 출력")
        await ctx.send(embed=embed)