from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

class Myconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connection established')
        await(self.channel_layer.group_add)('programmers',self.channel_name)
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self,event):
        print('established connection message is '+ event['text'])
        await(self.channel_layer.group_send)(
        'programmers',
        {
            'type':'chat.message',
            'message':event['text']
        }
        )

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })

    async def websocket_disconnect(self,event):
        print('Disconnect successfully')
        await(self.channel_layer.group_discard)('programmers',self.channel_name)        #no need to convert async_to_sync, use await instead
        raise StopConsumer

# class Myconsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print('websocket connected')
#         print('channel layer....',self.channel_layer)
#         print('channel name....',self.channel_name)
#         async_to_sync(self.channel_layer.group_add)('programmers',self.channel_name) #we have to convert it async_to_sync
#         self.send({
#             'type':'websocket.accept',
#         })

#     def websocket_receive(self,event):
#         print('Message is '+ event['text'])
#         print(type(event['text']))              #<class 'str'>
#         async_to_sync(self.channel_layer.group_send)(
#         'programmers',
#         {
#             'type':'chat.message',          #handler
#             'message':event['text']
#         }
#         )

#     def chat_message(self,event):
#         print('Event',event)
#         print('Event',event['message'])
#         print('Event type',type(event['message']))                  #Event type <class 'str'>

#         self.send({
#             'type':"websocket.send",
#             'text':event['message'],           #added this to get acknowledgment that message send successfully.
#         })
#         # for i in range(30):
#         #     self.send({
#         #         'type':'websocket.send',
#         #         'text': json.dumps(i),
#         #     })
#         #     sleep(1)

#     def websocket_disconnect(self,event):
#         print('websocket connection over',event)
#         print('channel layer....',self.channel_layer)
#         print('channel name....',self.channel_name)
#         async_to_sync(self.channel_layer.group_discard)('programmers',self.channel_name)
#         raise StopConsumer