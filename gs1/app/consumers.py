from channels.consumer import SyncConsumer

class MySynccosumers(SyncConsumer):

    def websocket_connect(self,event):
        print('websocket connect',event)
        self.send(
            {
                'type':'websocket.accept'
            }
        )

    def websocket_receive(self,event):
        print('websocket data receive',event)

    def websocket_disconnect(self,event):
        print('websocket disconnect',event)