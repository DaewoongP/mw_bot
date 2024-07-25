import All
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
        #await ctx.message.delete()

    # 간단한 군장 검사
    @client.hybrid_command(name="군장검사", with_app_command=True, description="캐릭터의 간단한 정보를 표시해줍니다.")
    async def command_check_spec(ctx: commands.Context, character_name):
        character_name = All.change_name(character_name)

        sibling_list = lostark.find_siblings(character_name=character_name)
        sibling_max_level = 0
        max_level_character_in_sibling = ""
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

        # 임베드 생성
        embed = discord.Embed(
            title=f"[{profile_list.get('Title')}] {character_name} ({profile_list.get('CharacterClassName')})",
            color=All.random.choice(All.colors)
        )
        embed.set_footer(text=f"검색자 : {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        # embed.add_field(name="이름", value=f"{character_name}", inline=True)
        embed.add_field(name="아이템 레벨", value=f"{profile_list.get('ItemMaxLevel')}", inline=True)
        embed.add_field(name="원정대 레벨", value=f"{profile_list.get('ExpeditionLevel')}", inline=True)
        embed.add_field(name="캐릭터 레벨", value=f"{profile_list.get('CharacterLevel')}", inline=True)

        # 보석
        gem_list = lostark.find_character(character_name=character_name, filter=lostark.character_filter.gems)

        gem_levels = list()
        for gem in gem_list.get("Gems"):
            current_gem_level = 0
            current_gem_level = int(gem.get("Level"))
            if "겁화" in gem.get("Name"):
                current_gem_level += 2
            elif "작열" in gem.get("Name"):
                current_gem_level += 2
            gem_levels.append(current_gem_level)
        gem_levels.sort(reverse=True)

        def average(lst):
            if not lst:
                return 0
            return sum(lst) / len(lst)

        if len(gem_levels) >= 4:
            embed.add_field(name="보석 최대렙 4개", value=f"{gem_levels[0], gem_levels[1], gem_levels[2], gem_levels[3]}", inline=True)
        embed.add_field(name="보석 평균 레벨", value=f"멸홍기준 {round(average(gem_levels), 2)}", inline=True)
        embed.add_field(name="보석 개수", value=f"{len(gem_list.get('Gems'))}", inline=True)

        # 장비 예외처리 필요, 모든 장비 순회 필요
        equipment_list = lostark.find_character(character_name=character_name,
                                                filter=lostark.character_filter.equipment)

        transcendence_num = 0
        elixir_list = tuple()
        for equip in equipment_list:
            json_equip_data = json.loads(equip['Tooltip'])
            if equip['Type'] == "무기":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                pass
            if equip['Type'] == "투구":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                elixir_list = lostark.find_elixir(json_equip_data)
                pass
            if equip['Type'] == "상의":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                pass
            if equip['Type'] == "하의":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                pass
            if equip['Type'] == "장갑":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                pass
            if equip['Type'] == "어깨":
                transcendence_num = lostark.find_transcendence(json_equip_data, "모든 장비에 적용된 총")
                pass

        # 카드
        card_list = lostark.find_character(character_name=character_name, filter=lostark.character_filter.cards)
        for effect in card_list.get("Effects"):
            for item in effect.get("Items"):
                if item.get("Name") == "세상을 구하는 빛 6세트 (30각성합계)":
                    embed.add_field(name="카드", value=f"세구 30", inline=True)
                    break
                elif item.get("Name") == "카제로스의 군단장 6세트 (30각성합계)":
                    embed.add_field(name="카드", value=f"암구 30", inline=True)
                    break
                elif item.get("Name") == "남겨진 바람의 절벽 6세트 (30각성합계)":
                    embed.add_field(name="카드", value=f"남바절 30", inline=True)
                    break
                elif item.get("Name") == "창의 달인 6세트 (30각성합계)":
                    embed.add_field(name="카드", value=f"창달 30", inline=True)
                    break
                else:
                    embed.add_field(name="카드", value=f".", inline=True)
                    break

        # 엘릭서
        # 레벨 제한 필요
        if elixir_list is None:
            embed.add_field(name="엘릭서", value=f"X", inline=True)
        else:
            embed.add_field(name="엘릭서", value=f"{elixir_list[0]} : {elixir_list[1]}단계", inline=True)

        # 초월
        embed.add_field(name="초월", value=f"{transcendence_num}개", inline=True)

        # 원정대 내 가장 높은 캐릭터 이름, 레벨
        embed.add_field(name="원정대 고렙 캐릭터", value=f"{max_level_character_in_sibling} / {sibling_max_level}", inline=False)

        # 출력
        await ctx.send(embed=embed)
