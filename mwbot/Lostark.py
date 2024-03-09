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

        print(f"Lostark Init : {init_response}")

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

    def get_notice_title(self):
        return self.notice_title

    def get_notice_link(self):
        return self.notice_link
