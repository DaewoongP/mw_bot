# Discord Bot Token Management
class CToken:
    def __init__(self):
        token_file = open("../Token.txt", 'r')
        self.m_DiscordToken = token_file.readline() # discord token data
        self.m_DiscordToken = self.m_DiscordToken.replace('\n', '')
        self.m_DFToken      = token_file.readline() # 던파 토큰 데이터
        self.m_DFToken      = self.m_DFToken.replace('\n', '')
        self.m_ServerToken  = token_file.readline() # 서버 토큰 데이터
        self.m_ServerToken  = self.m_DFToken.replace('\n', '')