import All
import json
from datetime import datetime


def start(client, DF, commands, discord):
    @client.hybrid_command(name="던파등록", with_app_command=True, description="내 캐릭터를 태초 알람에 등록합니다.")
    async def command_notice(ctx: commands.Context, server_name, character_name):

        # 한글 서버 이름에서 영어 서버 이름으로 변환
        response_server_name = All.df_server_name(server_name)

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
            await ctx.send("이미 등록된 캐릭터입니다!")
    
    @client.hybrid_command(name="오늘태초", with_app_command=True, description="오늘 태초 먹은사람이 있는지 체크합니다.")
    async def command_notice(ctx: commands.Context):
        char_list = DF.get_characters()
        # current date
        today_str = datetime.today().strftime('%Y%m%d')
        current_time_str = datetime.today().strftime('%H%M')

        # 504	아이템 획득(항아리&상자)
        # 505	아이템 획득(던전 드랍)
        # 506	아이템 획득(조각 교환)
        # 507	아이템 획득(레이드 카드 보상)
        # 508	아이템 획득(상점)

        code_box = 504
        code_dungeon = 505
        code_card = 507
        code_shop = 508

        data_limit = 100

        item_list = list()
        bitic_list = list()

        for char in char_list:
            item_list = DF.get_timeline(
                f"servers/{char[0]}" +
                f"/characters/{char[1]}" +
                f"/timeline" +
                f"?limit={data_limit}" +
                f"&code={code_dungeon}" +
                f"&startDate=20250329T0000" +
                f"&endDate=20250329T2359")
                #f"&startDate={today_str}T0000" +
                #f"&endDate={today_str}T{current_time_str}")
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
            title=f"[오늘 태초 리스트] - 레전 1, 에픽 3, 태초 10",
            color=All.random.choice(All.colors)
        )
        
        for bitic_item in bitic_list:
            embed.add_field(name=f"{bitic_item[0]} - {bitic_item[1]}pt", value=f"레전 : {bitic_item[2]}, 에픽 : {bitic_item[3]}, 태초 : {bitic_item[4]}", inline=True)

        await ctx.send(embed=embed)