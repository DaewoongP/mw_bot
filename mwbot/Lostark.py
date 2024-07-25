import requests
import re
import All


class CCharacter_Filter:
    def __init__(self):
        self.profiles = "profiles"
        self.equipment = "equipment"
        self.avatars = "avatars"
        self.skills = "combat-skills"
        self.engravings = "engravings"
        self.cards = "cards"
        self.gems = "gems"
        self.colosseums = "colosseums"
        self.collectibles = "collectibles"
        # /characters/{name}/siblings ## 원정대 캐릭터 전부 출력
        self.characters = "characters"


class CLostark:
    def __init__(self, token):
        # init
        self.headers = {
        'accept' : 'application/json',
        'authorization' : 'bearer ' + token
        }
        init_url = 'https://developer-lostark.game.onstove.com/example/api'
        init_response = requests.get(init_url, headers=self.headers)
           
        
        print(f"Lostark Init : {init_response}")

        ### 공지사항 초기화 ###
        # notice : [Title, Date, Link, Type]
        # "Title": "string",
        # "Date": "2024-02-07T09:58:02.480Z",
        # "Link": "string",
        # "Type": "공지"
        notice_url = 'https://developer-lostark.game.onstove.com/news/notices'
        notice_response = requests.get(notice_url, headers=self.headers)

        self.notice_title = list()
        for title in notice_response.json():
            if "업데이트 내역" in title.get("Title"):
                self.notice_title.append(title.get("Title"))

        self.notice_link = list()
        for link in notice_response.json():
            self.notice_link.append(link.get("Link"))
        ### 공지사항 초기화 ... ###

        ### 캐릭터 정보 가져오기 ###
        self.character_filter = CCharacter_Filter()

    def find_siblings(self, character_name):
        character_url = f"https://developer-lostark.game.onstove.com/characters/{character_name}/siblings"
        character_response = requests.get(character_url, headers=self.headers)
        ret_list = list()
        for cl in character_response.json():
            ret_list.append(cl)

        return ret_list

    def find_character(self, character_name, filter:CCharacter_Filter):
        character_url = f"https://developer-lostark.game.onstove.com/armories/characters/{character_name}/{filter}"
        return requests.get(character_url, headers=self.headers).json()

    ### 캐릭터 정보 가져오기 ... ###

    def get_notice_title(self):
        return self.notice_title

    def get_notice_link(self):
        return self.notice_link

    def get_character_filter(self):
        return self.character_filter

    def find_transcendence(self, data, target_str):
        count = 0
        for key, value in data.items():
            if isinstance(value, dict):
                count += self.find_transcendence(value, target_str)
            elif isinstance(value, str) and target_str in value:
                match = re.search(r"(\d+)개", value)
                if match:
                    count += int(match.group(1))
        return count

    def find_elixir(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                result = self.find_elixir(value)
                if result is not None:
                    return result
            elif isinstance(value, str):
                for target_str in All.elixir_list:
                    if target_str in value:
                        match = re.search(r"({}) \((\d+)단계\)".format(target_str), value)
                        if match:
                            return target_str, match.group(2)
        return None
