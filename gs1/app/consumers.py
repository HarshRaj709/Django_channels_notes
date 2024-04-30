from channels.consumer import SyncConsumer

class MySynccosumers(SyncConsumer):

    def websocket_connect(self,event):
        print('websocket connect')

    def websocket_receive(self,event):
        print('websocket data receive')

    def websocket_disconnect(self,event):
        print('websocket disconnect')