import requests
import mainnn
from create import Creator
import vk_api
tokennnn=mainnn.get_token.tokenn
vk_session = vk_api.VkApi(token=tokennnn)
from vk_api.longpoll import VkLongPoll, VkEventType
class User:
    def listen():
        longpoll_us = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        print('start')
        for event in longpoll_us.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
           #Слушаем longpoll, если пришло сообщение то:
                if event.text.lower() == 'салам аллейкум': #Если написали заданную фразу
                    if event.from_user: #Если написали в ЛС
                        Creator('[log] '+ event.text.lower()).readwrite()
                        vk.messages.send( #Отправляем сообщение
                            user_id=event.user_id,
                            message='Ваалейкум ассалам', random_id=0
        		)
                elif event.text.lower() == 'начать':
                    if event.from_user: #Если написали в ЛС
                        Creator('[log] '+ str(event.text.lower())).readwrite()
                        vk.messages.send( #Отправляем сообщение
                            user_id=event.user_id,
                            message='Добавь меня в беседу', random_id=0
        		)
