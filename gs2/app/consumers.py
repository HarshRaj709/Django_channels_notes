from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer

class MysyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected',event)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        # print('websocket receive',event)
        print('received message is',event['text'])
    
    def websocket_disconnect(self,event):
        print('websocket disconnected',event)
        raise StopConsumer()
