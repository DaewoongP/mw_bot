import requests
import json


class CLostark:
    def __init__(self, token):
        # init
        self.headers = {
        'accept': 'application/json',
        'authorization': token
        }
        init_url = 'https://developer-lostark.game.onstove.com/example/api'
        init_response = requests.get(init_url, headers=self.headers)

        # notice : [Title, Date, Link, Type]
        # "Title": "string",
        # "Date": "2024-02-07T09:58:02.480Z",
        # "Link": "string",
        # "Type": "공지"
        notice_url = 'https://developer-lostark.game.onstove.com/news/notices'
        notice_response = requests.get(notice_url, headers=self.headers)
        self.notice_list = notice_response.json()

    def get_notice(self):
        return self.notice_list
