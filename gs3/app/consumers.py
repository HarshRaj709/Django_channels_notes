from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer

# class Myasyncconsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print('websocket connect',event)
#         self.send({
#             'type':'websocket.accept'
#         })

#     def websocket_receive(self,event):
#         print('received message is',event['text'])

#     def websocket_disconnect(self,event):
#         print('websocket disconnected',event)
#         #raise StopConsumer


class Myasyncconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect',event)
        await self.send({                           # here we have to add await as we are using 
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('received message is',event['text'])

    async def websocket_disconnect(self,event):
        print('websocket disconnected',event)
        raise StopConsumer