from random import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import mainnn
import threading
from create import Creator
from reader import Read
token_vk=mainnn.get_token.tokenn
# event.object['from_id'] - ид написавшего
# event.object['text'] - текст



vk_session = VkApi(token=token_vk)
class Chat(threading.Thread):
    admchat='admin_chat'
    roditeli='rod_chat'
    besedy='norm_chat'
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        longpoll = VkBotLongPoll(vk_session, "184001120")
        vk = vk_session.get_api()
        print('start...')
        for event in longpoll.listen():
            try:
                res=event.object['text'].lower()
                fromm=event.object['from_id']
                if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                    print(res)
                    print(fromm)
                    if ('идентификатор:' in res) and ((event.object['from_id']==202338438) or (event.object['from_id']=='202338438') or ( event.object['from_id']==550379895) or ( event.object['from_id']=='550379895')):
                        print('in')
                        if 'аптека' in res:
                            admin_chat=event.object['peer_id']
                            Creator(str(admin_chat)+' admin_chat').readwrite()

                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='Идентификатор записан')
                        elif 'норм' in res:
                            chatchat=event.object['peer_id']
                            Creator(str(chatchat)+' norm_chat').readwrite()

                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='Идентификатор записан')
                        elif 'родители' in res:
                            rodchat=event.object['peer_id']
                            Creator(str(rodchat)+' rod_chat').readwrite()

                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='Идентификатор записан')
                    elif Read(event.object['peer_id'], 'admin_chat').read():
                        if 'бот' in res:
                            if 'привет' in res:
                                random_id = round(random() * 10 ** 9)
                                chat_id = int(event.chat_id)
                                vk.messages.send(random_id=random_id,chat_id=chat_id,message='Привет')
                        elif 'салам аллейкум' in res:
                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='@id'+str(event.object['from_id'])+' Ваалейкум ассалам')
                        elif 'иди нахуй' in res:
                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='ты ахуел? сам иди')
                        elif 'соси' in res or 'саси' in res:
                            random_id = round(random() * 10 ** 9)
                            chat_id = int(event.chat_id)
                            vk.messages.send(random_id=random_id,chat_id=chat_id,message='пососи ты лучше ;)')

            except:
                continue
