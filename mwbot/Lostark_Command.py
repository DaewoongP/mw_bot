import All
import re
import json


def start(client, lostark, commands, discord):
    # 최신 공지 사항
    @client.hybrid_command(name="로아공지", with_app_command=True, description="로스트아크의 가장 최신 업데이트 내역을 보여줍니다.")
    async def command_notice(ctx: commands.Context):
        embed = discord.Embed(
            title="로아 최신 업데이트 내역",
            description=f"[{lostark.get_notice_title()[0]}]({lostark.get_notice_link()[0]})",
            color=All.random.choice(All.colors)
        )
        # 보낸사람의 이름, 썸넬이 임베드에 보이게됨.
        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        # 보낸 메세지를 삭제하는 기능.
        await ctx.message.delete()
        
    # 간단한 군장 검사
    @client.hybrid_command(name="군장검사", with_app_command=True, description="캐릭터의 간단한 정보를 표시해줍니다.")
    async def command_check_spec(ctx: commands.Context, character_name):
        character_name = All.change_name(character_name)
        # 임베드 생성
        embed = discord.Embed(
            title="군장검사",
            color=All.random.choice(All.colors)
        )


        sibling_list = lostark.find_siblings(character_name=character_name)
        sibling_max_level = 0
        for character_arr in sibling_list:
            # 문자열 처리
            characters_to_remove = "',"
            max_level_string = character_arr.get("ItemMaxLevel")
            for char in characters_to_remove:
                max_level_string = max_level_string.replace(char, "")

            if float(max_level_string) > sibling_max_level:
                sibling_max_level = float(max_level_string)
                max_level_character_in_sibling = character_arr.get("CharacterName")

        profile_list = lostark.find_character(character_name=character_name, filter=lostark.character_filter.profiles)

        embed.add_field(name="이름", value=f"{character_name}", inline=True)
        embed.add_field(name="아이템 레벨", value=f"{profile_list.get("ItemMaxLevel")}", inline=True)
        embed.add_field(name="원정대 레벨", value=f"{profile_list.get("ExpeditionLevel")}", inline=True)

        embed.add_field(name="칭호", value=f"{profile_list.get("Title")}", inline=True)
        embed.add_field(name="클래스", value=f"{profile_list.get("CharacterClassName")}", inline=True)
        embed.add_field(name="캐릭터 레벨", value=f"{profile_list.get("CharacterLevel")}", inline=True)

        embed.set_footer(text=f"검색자 : {ctx.author.display_name}", icon_url=f"{profile_list.get("CharacterImage")}")

        # 보석
        gem_list = lostark.find_character(character_name=character_name, filter=lostark.character_filter.gems)

        gem_levels = list()
        for gem in gem_list.get("Gems"):
            gem_levels.append(int(gem.get("Level")))
        gem_levels.sort(reverse=True)

        def average(lst):
            if not lst:
                return 0
            return sum(lst) / len(lst)

        if len(gem_levels) >= 4:
            embed.add_field(name="보석 최대렙 4개", value=f"{gem_levels[0], gem_levels[1], gem_levels[2], gem_levels[3]}", inline=True)
        embed.add_field(name="보석 평균 레벨", value=f"{round(average(gem_levels), 2)}", inline=True)
        embed.add_field(name="보석 개수", value=f"{len(gem_list.get("Gems"))}", inline=True)

        # 장비 예외처리 필요, 모든 장비 순회 필요
        equipment_list = lostark.find_character(character_name=character_name,
                                                filter=lostark.character_filter.equipment)
        transcendence_sentence = json.loads(equipment_list[4]["Tooltip"])["Element_009"]["value"]["Element_000"]["contentStr"]["Element_001"]["contentStr"]
        find_transcendence_num = re.search(r"(\d+)개", transcendence_sentence)

        if find_transcendence_num:
            embed.add_field(name="초월", value=f"{find_transcendence_num.group(1)}개", inline=True)
        else:
            print(f"{transcendence_sentence}")
            print(f"error : {find_transcendence_num}")
            print("초월 단계 없음")

        # 엘릭서
        embed.add_field(name="엘릭서", value=f"공사중", inline=True)

        # 카드
        card_list = lostark.find_character(character_name=character_name, filter=lostark.character_filter.cards)
        for effect in card_list.get("Effects"):
            for item in effect.get("Items"):
                if item.get("Name") == "세상을 구하는 빛 6세트 (30각성합계)":
                    embed.add_field(name="카드", value=f"세구 30각", inline=False)

        # 원정대 내 가장 높은 캐릭터 이름, 레벨
        embed.add_field(name="원정대 고렙 캐릭터", value=f"{max_level_character_in_sibling} / {sibling_max_level}", inline=False)

        # 출력
        await ctx.send(embed=embed)
        await ctx.message.delete()