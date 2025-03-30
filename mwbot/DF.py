import requests
import re
import All


class CDF:
    def __init__(self, token):
        # init
        self.headers = {
        'accept' : 'application/json',
        'authorization' : 'bearer ' + token
        }

        self.url = "https://api.neople.co.kr/df/"
        self.apikey = "apikey=" + token

        test_url = self.url + "servers?" + self.apikey
        init_response = requests.get(test_url, headers=self.headers)

        # 던파 서버 정상 동작 중인지 체크
        print(f"DF Servers : {init_response}")

    def get_character_id(self, str_in, want_data):
        data_url = self.url + str_in + "&" + self.apikey;
        # url에서 header를 처리해서 가져와라. json 형식.
        data_out = requests.get(data_url, headers=self.headers)

        return data_out.json()['rows'][0][want_data]

    def get_timeline(self, str_in):
        data_url = self.url + str_in + "&" + self.apikey;
        # url에서 header를 처리해서 가져와라. json 형식.
        data_out = requests.get(data_url, headers=self.headers)

        # 먹은 아이템 데이터 목록
        timeline_data = data_out.json()['timeline']['rows'] # 인덱스형식, 'code', 'name', 'date', 'data'(먹은아이템)

        return timeline_data

    # server, character_id / pair 형태로 데이터 반환
    # @param 0 == server, 1 == character_id
    def get_characters(self):
        character_file_read = open("DFCharacters.txt", 'r', encoding='utf-8')
        filelines = character_file_read.readlines() # read line"s"

        character_list = list()
        for line in filelines:
            data = line.strip().split()  # 첫 번째 공백까지만 분리
            server, character_id, character_name = data
            # tuple로 저장
            character_list.append((server, character_id, character_name))

        return character_list

    def register_character(self, server_name, character_name, character_id):
        character_file_read = open("DFCharacters.txt", 'r', encoding='utf-8')
        filelines = character_file_read.readlines() # read line"s"

        current_list = list()
        isAlreadyRegisterData = False
        # 한줄씩 라인을 읽어서 (서버 아이디, 캐릭터 아이디, 캐릭터 이름) 을 저장함.
        for line in filelines:
            if server_name + ' ' + character_id + ' ' + character_name + '\n' == line:
                isAlreadyRegisterData = True
            current_list.append(line)

        if isAlreadyRegisterData == True:
            return False
        else:
            character_file_write = open("DFCharacters.txt", 'a', encoding='utf-8') # append mode로 열어야 마지막에 써짐.
            character_file_write.write(server_name + ' ' + character_id + ' ' + character_name + '\n')
            return True