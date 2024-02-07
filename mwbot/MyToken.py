class CToken:
    def __init__(self):
        token_file = open("../Token.txt", 'r')
        self.m_DiscordToken = token_file.readline()
        self.m_LostarkToken = token_file.readline()
