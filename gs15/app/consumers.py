from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio
import json

# class MyConsumer(WebsocketConsumer):
#     def connect(self):
#         print('connection established')
#         self.accept()                       #to accept the connection
#         #self.close()                        # to forcly stopped/reject the connection

#     def receive(self, text_data=None, bytes_data=None):
#         print('message received from client',text_data)
#         #text_data = 'custom message'
#         self.send(text_data='custom message')       #to send text data
#         #self.send(binary_data=data)                 #to send binary data
#         print('messaeg send to client')

#         self.close(code=4123)                           #to add a custom websocket error


#     def disconnect(self,close_code):
#         print('connection ended',close_code)


##################################################################################################################

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connection established')
        #what we want is that to add same groups with each other so that they can share messages 
        await self.channel_layer.group_add('programmers',self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('message received from client',text_data)
        print('type of text_data is ',type(text_data))          #already a string so no need to convert
        await self.channel_layer.group_send(
            'programmers',
            {
                'type':'chat.message',
                'text':text_data,
            }
                                            )
        #await self.send(text_data=text_data)
        print('message send to client')

    async def chat_message(self,event):
        await self.send(text_data=event['text'])        #as we still get our message in event['text']

    async def disconnect(self,close_code):
        print('connection ended',close_code)