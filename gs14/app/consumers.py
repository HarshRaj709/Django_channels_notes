from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

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
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('message received from client',text_data)
        #text_data = 'custom message'
        await self.send(text_data='custom message')       #to send text data
        #await self.send(binary_data=data)                 #to send binary data
        print('messaeg send to client')

        #await self.close(code=4123)

    async def disconnect(self,close_code):
        print('connection ended',close_code)