from VK.bot import VkBot
from settings import grp_token

if __name__ == '__main__':
    session = VkBot(grp_token)
    session.start_bot()
