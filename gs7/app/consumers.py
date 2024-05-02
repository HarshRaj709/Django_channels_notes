from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class Myconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected',event)
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self,event):
        print('Data Received',event['text'])
        for i in range(30):
            self.send({
                'type':'websocket.send',
                'text':json.dumps({'count':i})
            })
            sleep(1)

    def websocket_disconnect(self,event):
        print('websocket disconnect',event)
        raise StopConsumer


# class Myconsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print('websocket connected',event)
#         await self.send({
#             'type':'websocket.accept',
#         })

#     async def websocket_receive(self,event):
#         print('Data Received',event['text'])
#         for i in range(30):
#             await self.send({
#                 'type':'websocket.send',
#                 'text':str(i)
#             })
#             await asyncio.sleep(1)

#     async def websocket_disconnect(self,event):
#         print('websocket disconnect',event)
#         raise StopConsumer