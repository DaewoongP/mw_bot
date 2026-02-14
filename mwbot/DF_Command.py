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
        # 513   아이템 획득(던전 카드 보상)

        code_list = [505, 507, 513]
        
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
        # 513   아이템 획득(던전 카드 보상)

        code_list = [505, 507, 513]
        
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


    def is_later(date1_str, date2_str):
        date1 = datetime.strptime(date1_str, "%Y%m%d")
        date2 = datetime.strptime(date2_str, "%Y%m%d")
        return date1 < date2

    def add_two_months(date_str):
        date = datetime.strptime(date_str, "%Y%m%d")
        year = date.year
        month = date.month + 2
        day = date.day

        # 월이 12 초과이면 년도 증가
        if month > 12:
            month -= 12
            year += 1

        # 해당 월의 마지막 날보다 크면 마지막 날로 조정
        # 예: 1월 31일 → 3월 31일 (없으면 3월 30, 29로 조정)
        while True:
            try:
                new_date = datetime(year, month, day)
                break
            except ValueError:
                day -= 1  # 존재하지 않는 날짜면 하루씩 줄임

        return new_date.strftime("%Y%m%d")

    @client.hybrid_command(name="기린체크", with_app_command=True, description="중천 시즌 시작부터 비틱 수치")
    async def command_bitic(ctx: commands.Context, server_name, character_name):
         # 한글 서버 이름에서 영어 서버 이름으로 변환
        _serverName = All.df_server_name(server_name)
        if _serverName == "":
            await ctx.send("잘못된 서버 이름입니다.")
            return # 오류

        # Get Character id 
        _characterID = DF.get_character_id(f"servers/{_serverName}/characters?characterName={character_name}", "characterId")

        _today = datetime.today().strftime('%Y%m%d') # ex) 20250501
        _currentTime = subtract_one_minute(datetime.today().strftime('%H%M')) # 1분빼서 확인
        _startDate = "20250109"

        _codeList = "505,507,513" # 코드 리스트는 쉼표로 구분해도 처리된다.
        MAX_DATA = 100 # 설정 없으면 10, 최대값 100 (limit를 100으로 두는게 거의 베스트로 보임, 요청수 1로 처리된다.)
        # 기간설정 최대치가 90일 이므로, 2달에 걸쳐 검색

        #       next 요청변수 사용 예시
        # ex) /timeline?next=<next>&apikey=<apikey>
        # ※ next 사용 시 limit, code, startDate, endDate등 요청변수는 최초 조회 기준으로 적용됩니다. 
        # -> 최초조회 기준이므로, 요청 변수를 따로 주지않고, next만 담아서 처리해도 된다는 뜻같음. -> limit 바꿔도 최초기준으로 처리된다.

        # timeline 값에 next변수가 주어지는데, 해당값을 대입해서 보내면 처리가능.
        # 다음 값이 없을경우 null로 반환

        # 따로 함수로 관리하기엔 너무 대충 짜서 여기서 처리

        while True:
            _addedDate = add_two_months(_startDate)

            if is_later(_addedDate, _today):
                # today가 더크면
                _timeLineData = DF.get_timeline_json(
                    f"servers/{_serverName}" +
                    f"/characters/{_characterID}" +
                    f"/timeline" +
                    f"?limit={MAX_DATA}" +
                    f"&code={_codeList}" +
                    f"&startDate={_startDate}T0000" +
                    f"&endDate={_addedDate}T2359")
            else:
                _timeLineData = DF.get_timeline_json(
                    f"servers/{_serverName}" +
                    f"/characters/{_characterID}" +
                    f"/timeline" +
                    f"?limit={MAX_DATA}" +
                    f"&code={_codeList}" +
                    f"&startDate={_startDate}T0000" +
                    f"&endDate={_today}T{_currentTime}")



            _startDate = _addedDate # 다음 검색을 위해 초기화



        # 중천 시즌 시작 -> 250108
        # -- 환요오괴 리스트 -- (전부 1배수)
        # 모독 : 적막의 회랑
        # 모독 : 일렁이는 군도
        # 광포 : 크루얼 비스트
        # 광포 : 청해의 심장
        # 환란 : 길잡이 강
        # 환란 : 별내림 숲

        # 베누스 -> 찬사의 광장 13

        # ---- 상던 ----
        # 꿈결 속 흰 구름 계곡 5
        # 꿈결 속 솔리다리스 7
        # 달이 잠긴 호수 10
        # 애쥬어 메인 15
        # 침묵의 성소 17 (여신전)

        # -- 숭 --
        # 종말의 숭배자
        # 심연 : 종말의 숭배자 13

        # if 507에 데이터가 존재하면, 해당 날짜(시간) 201 코드로 검색 -> 나벨이면 추가
        # 나벨 - 싱글 (무의지의 장벽) --> 13배수
        # 나벨 - 레이드 --> 19배수