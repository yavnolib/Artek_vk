# from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
# import vk_api
# import requests
# import time
# API-ключ созданный ранее

# vk=vk_api.VkApi(token=tokenn)
# vk._auth_token()
# vk.get_api()
# longpool=VkBotLongPoll(vk, 184001120)
# print('connect')
# while True:
#     try:
#         for event in longpool.listen():
#             if event.type==VkBotEventType.MESSAGE_NEW:
#                 if event.object.peer_id != event.object.from_id:
#                     if event.object.text.lower()=='привет':
#                         vk.method('messages.send', {'peer_id':event.object.peer_id, 'message':'привет','random_id':0})
#
#                 elif event.object.peer_id == event.object.from_id:
#                     if event.object.text.lower()=='окей':
#                         vk.method('messages.send', {'peer_id':event.object.from_id, 'message':'привет','random_id':0})
#             else:
#                 print(event)
#     except Exception as E:
#         print('wait...')
#         time.sleep(0.5)
class get_token(object):
    """docstring for get_token."""
    tokenn = "8169ac79fcc9e56e8965bfd9ba3a60b37567fdbb82290cdb300b5e65b599d075cfafc6fecd8930da7d310"
    group_id=184001120
