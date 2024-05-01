from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer

# class Myconsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print('websocket connected',event)
#         self.send({
#             'type':'websocket.accept',
#         })

#     def websocket_receive(self,event):
#         print('data receive',event['text'])
#         self.send({
#             'type':'websocket.send',
#             'text':'This message is sent by server'
#         })

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
        await self.send({
            'type':'websocket.send',
            'text':'This message is sent by server'
        })

    async def websocket_disconnect(self,event):
        print('websocket disconnect',event)
        raise StopConsumer