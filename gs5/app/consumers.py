from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio      #when we try to run it with async Consumers

# class Myconsumer(SyncConsumer):                   #problem with SyncConsumer is that it can serve to 1 client at a time.
#     def websocket_connect(self,event):
#         print('websocket connected',event)
#         self.send({
#             'type':'websocket.accept',
#         })

#     def websocket_receive(self,event):
#         print('data receive',event['text'])
#         for i in range(50):
#             self.send({
#                 'type':'websocket.send',
#                 'text':str(i)
#             })
#             sleep(1)

#     def websocket_disconnect(self,event):
#         print('websocket disconnect',event)
#         raise StopConsumer


class Myconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connected',event)
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self,event):
        print('data receive',event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            await asyncio.sleep(2)

    async def websocket_disconnect(self,event):
        print('websocket disconnect',event)
        raise StopConsumer