import random
# 컬러값
colors = [0xFFEEEE, 0xFFF2EE, 0xFFF7EE, 0xFFFBEE, 0xFFFFEE, 0xFBFFEE, 0xF7FFEE, 0xF2FFEE, 0xEEFFEE, 0xEEFFF2,
          0xEEFFF7, 0xEEFFFB, 0xEEFFFF, 0xEEFBFF, 0xEEF2FF, 0xEEEEFF, 0xF2EEFF, 0xF7EEFF, 0xFBEEFF, 0xFFEEFF,
          0xFFEEFB, 0xFFEEF7, 0xFFEEF2, 0xFFD9D9, 0xFFE2D9, 0xFFECD9, 0xFFF5D9, 0xFFFFD9, 0xF5FFD9, 0xECFFD9,
          0xE2FFD9, 0xD9FFD9, 0xD9FFE2, 0xD9FFEC, 0xD9FFF5, 0xD9FFFF, 0xD9F5FF, 0xD9ECFF, 0xD9E2FF, 0xD9D9FF,
          0xE2D9FF, 0xECD9FF, 0xF5D9FF, 0xFFD9FF, 0xFFD9F5, 0xFFD9EC, 0xFFC4C4, 0xFFD2C4, 0xFFE1C4, 0xFFF0C4,
          0xFFFFC4, 0xF0FFC4, 0xE1FFC4, 0xD2FFC4, 0xC4FFC4, 0xC4FFD2, 0xC4FFE1, 0xC4FFF0, 0xC4FFFF, 0xC4F0FF,
          0xC4E1FF, 0xC4D2FF, 0xC4C4FF, 0xD2C4FF, 0xE1C4FF, 0xF0C4FF, 0xFFC4FF, 0xFFC4F0, 0xFFC4E1]

# 이모지 리스트
emoji = ['💡', '📖', '✏️', '🖼️', '⚔️', '🪙', '🍀', '🎉', '🎮', '💰', '📺']

# 던전이름
SIM_SUNG = "심연 : 종말의 숭배자"
JONG_SUNG = "종말의 숭배자"

# 닉네임
def change_name(name):
    if name == "그꿈덧":
        return "그꿈을덧그리며"
    if name == "쉴바용":
        return "쉴드바드세용"
    if name == "부많삶":
        return "부끄럼많은삶을살았습니다"
    if name == "버리":
        return "바리"
    if name == "라펙트":
        return "LastEffect"
    if name == "전창술":
        return "전창술사에용"
    return name

def df_server_name(name):
    if name == "카인":
        return "cain"
    if name == "디레지에":
        return "diregie"
    if name == "시로코":
        return "siroco"
    if name == "프레이":
        return "prey"
    if name == "카시야스":
        return "casillas"
    if name == "힐더":
        return "hilder"
    if name == "안톤":
        return "anton"
    if name == "바칼":
        return "bakal"
    
    return ""

# 엘릭서
elixir_list = ["강맹", "달인", "선각자", "선봉대", "신념", "진군", "칼날 방패", "행운", "회심"]

necklace_list = [
    ["추가 피해 %", 0.7, 1.6, 2.6], ["적에게 주는 피해 %", 0.55, 1.2, 2.0], ["세레나데, 신앙, 조화 게이지 획득량 %", 1.6, 3.6, 6.0],
    ["낙인력 %", 2.15, 4.8, 8.0],["최대 생명력 +", 1300, 3250, 6500],["공격력 +", 80, 195, 390],
    ["무기 공격력 +", 195, 480, 960],["최대 마나 +", 6, 15, 30],["상태이상 공격 지속시간 %", 0.2, 0.5, 1.0],
    ["전투 중 생명력 회복량 +", 10, 25, 50]
    ]

# 연마 옵션 뽑기
# def get_random_option(acc_list):
#     probabilities = [0.063, 0.03, 0.007]
#     color = [0x009CDB, 0xB13AD9, 0xFE9600]
    
#     # 무작위로 속성 선택
#     attribute = random.choice(acc_list)
#     name = attribute[0]
#     options = attribute[1:]
    
#     # 옵션의 개수와 확률 리스트의 길이 일치 여부 확인
#     if len(probabilities) != len(options):
#         raise ValueError("The length of probabilities must match the length of options")
    
#     # 무작위로 옵션을 선택하고, 선택된 옵션의 인덱스 찾기
#     chosen_option = random.choices(options, weights=probabilities)[0]
#     chosen_index = options.index(chosen_option)
    
#     return name, chosen_option, color[chosen_index]


def get_random_option(acc_list, exclude1=None, exclude2=None):
    probabilities = [0.063, 0.03, 0.007]
    color = [0x009CDB, 0xB13AD9, 0xFE9600]

    # 리스트 복사하여 원본 리스트 보호
    filtered_list = [attribute for attribute in acc_list]

    # 제외할 문자열이 주어진 경우 해당 문자열과 일치하는 리스트 제거
    if exclude1 or exclude2:
        filtered_list = [
            attribute for attribute in filtered_list
            if attribute[0] != exclude1 and attribute[0] != exclude2
        ]

    # 무작위로 속성 선택
    attribute = random.choice(filtered_list)
    name = attribute[0]
    options = attribute[1:]

    # 옵션의 개수와 확률 리스트의 길이 일치 여부 확인
    if len(probabilities) != len(options):
        raise ValueError("The length of probabilities must match the length of options")

    # 무작위로 옵션을 선택하고, 선택된 옵션의 인덱스 찾기
    chosen_option = random.choices(options, weights=probabilities)[0]
    chosen_index = options.index(chosen_option)

    return name, chosen_option, color[chosen_index]



# class Select(discord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.add_item(discord.ui.Select(
#             placeholder="메뉴창 이름 입니다."), 
#             options=[
#                 discord.SelectOption(label="test1",description="test1 설명"),
#                 discord.SelectOption(label="test2",description="test2 설명"),
#                 discord.SelectOption(label="test3",description="test3 설명")
#             ]
#         )


# grind_data = {
#     "users": [
#         {
#             "name": ctx.author.name,
#             "id": ctx.author.id,
#             "necklace": [
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 }
#             ],
#             "earring1": [
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 }
#             ],
#             "earring2": [
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 }
#             ],
#             "ring1": [
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 }
#             ],
#             "ring2": [
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 },
#                 {
#                 "option": "",
#                 "value": 0
#                 }
#             ]
#         },
#     ]
# }