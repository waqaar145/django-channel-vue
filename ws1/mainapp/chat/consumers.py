from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json

class ChatConsumer(AsyncConsumer):
     async def websocket_connect(self, event):
         print("connect", event)
         user = self.scope['url_route']['kwargs']['username']
         chat_room = user
         self.chat_room = chat_room
         print(chat_room)
         await self.channel_layer.group_add(
             chat_room,
             self.channel_name
         )
         await self.send({
            "type": "websocket.accept",
        })

     async def websocket_receive(self, event):
         print("receive", event)
         front_text = event.get('text', None)
         if front_text is not None:
             loaded_dict_data = json.loads(front_text)
             print('loaded_dict_data', loaded_dict_data)
             msg = loaded_dict_data.get("message")
             myResponse = {
                 "message": msg
             }
             await self.channel_layer.group_send(
                 self.chat_room,
                 {
                     "type": "chat_message",
                     "text": json.dumps(myResponse)
                 }
             )

     async def chat_message(self, event):
         # send actual message
         await self.send({
             "type": "websocket.send",
             "text": event['text']
         })

     def websocket_disconnect(self, event):
         print("disconnected", event)




    # def connect(self):
    #     print('connecting to channels')
    #     self.accept()
    #
    # def disconnect(self, close_code):
    #     pass
    #
    # def receive(self, event):
    #     print("receive", event)
        # front_text = event.get('text', None)
        # if front_text is not None:
        #     loaded_dict_data = json.loads(front_text)
        #     msg = loaded_dict_data.get("message")
        #     print(msg)
        # msg = loaded_dict_data.get("message")
        # self.send({
        #     'message': "receive =="
        # })

    # async def disconnect(self, event):
    #     print("disconnected", event)
