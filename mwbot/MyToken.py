# Discord Bot Token Management
class CToken:
    def __init__(self):
        token_file = open("../Token.txt", 'r')
        self.m_DiscordToken = token_file.readline()
        self.m_DiscordToken = self.m_DiscordToken.replace('\n', '')
        self.m_LostarkToken = token_file.readline()
        self.m_LostarkToken = self.m_LostarkToken.replace('\n', '')
        self.m_GongbangToken = token_file.readline()
        self.m_GongbangToken = self.m_GongbangToken.replace('\n', '')