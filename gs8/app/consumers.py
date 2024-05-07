from channels.consumer import SyncConsumer
from time import sleep
from channels.exceptions import StopConsumer
import json

# class Myconsumer(SyncConsumer):
#     def websocket_connect(self,events):
#         print('websocket connected')
#         self.send({
#             'type':'websocket.accept',
#         })

#     def websocket_receive(self,event):
#         print('Message is '+ event['text'])
#         for i in range(30):
#             self.send({
#                 'type':'websocket.send',
#                 'text': json.dumps(i),
#             })
#             sleep(1)

#     def websocket_disconnect(self,event):
#         print('websocket connection over',event)
#         raise StopConsumer

class Myconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected')
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self,event):
        print('Message is '+ event['text'])
        # for i in range(30):
        #     self.send({
        #         'type':'websocket.send',
        #         'text': json.dumps(i),
        #     })
        #     sleep(1)

    def websocket_disconnect(self,event):
        print('websocket connection over',event)
        raise StopConsumer