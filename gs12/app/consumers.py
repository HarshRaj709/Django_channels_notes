from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json
from .models import Chat,Group

class Myconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connection established')
        self.group_name = self.scope['url_route']['kwargs']['groupkanaam']  #accessing nested dictionary value..
        await(self.channel_layer.group_add)(self.group_name,self.channel_name)
        print('group Name..',self.group_name)      #to get group name
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self,event):
        print('established connection message is '+ event['text'])
        print('received messaeg data type',type(event['text']))         # checked data type we got str

        data = json.loads(event['text'])                                # changed data type by using .loads()
        print('converted to dict type',type(data))
        print(data['msg'])                                  #fetched actual message from server side

        user = self.scope['user']
        if user.is_authenticated: 
        # now store that actual message to its actual group
            group = await database_sync_to_async(Group.objects.get)(group = self.group_name)      #used .get() to get only 1 result

            #chat object
            #chat = Chat.objects.filter(group = group)
            chat = Chat(group=group,content=data['msg'])        #saving data to chat model
            print(chat)
            data['user'] = self.scope['user'].username
            await database_sync_to_async(chat.save)()
            
            await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                # 'message':event['text']
                'message':json.dumps(data)
            }
            )
        else:
            await self.send({
                'type':'websocket.send',
                'text': json.dumps({'msg':'login required to send message.','user':'guest'})
            })

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })

    async def websocket_disconnect(self,event):
        print('Disconnect successfully')
        await(self.channel_layer.group_discard)(self.group_name,self.channel_name)        #no need to convert async_to_sync, use await instead
        raise StopConsumer




###################################################################################################################

                                    ############## SyncConsumer ###############


# class Myconsumer(SyncConsumer):
#     def websocket_connect(self,event):
#          print('websocket connected')
#         #  print('channel layer....',self.channel_layer)
#         #  print('channel name....',self.channel_name)
#          self.group_name = self.scope['url_route']['kwargs']['groupkanaam']
#          async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name) #we have to convert it async_to_sync
#          self.send({
#              'type':'websocket.accept',
#          })

#     def websocket_receive(self,event):
#         # print('Message is '+ event['text'])
#         # print(type(event['text']))              #<class 'str'>

#         group = Group.objects.get(group = self.group_name)      #used .get() to get only 1 result

#         data = json.loads(event['text'])                                # changed data type by using .loads()
#         # print('converted to dict type',type(data))
#         # print(data['msg'])   


#     #implementing Authentication in django channels.
#         print('ye h user ka details...........',self.scope['user'])     #if not authenticated then user will show as........... AnonymousUser

#         user = self.scope['user']
#         if user.is_authenticated: 
#             #chat object
#             #chat = Chat.objects.filter(group = group)
#             chat = Chat(group=group,content=data['msg'])        #saving data to chat model
#             #print(chat)
#             chat.save()
#         # Now we want to send user's username along with message
#             data['user'] = self.scope['user'].username              #this will provide us the username of the user
#             print('complete things data have:',data)

#             async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 'type':'chat.message',          #handler
#             # Now we want to send that data dictionary which contains this -- {'msg': 'check data', 'user': 'admin'}
#                 # 'message':event['text']
#                 'message':json.dumps(data)
#             # now this message will go to chat_message function because of ''chat.message'' handler
#             }
#             )
#         else:
#             #self.close()           #we can directly close the connection or we can send user the message to login first.

#             self.send({
#                 'type':'websocket.send',
#                 'text': json.dumps({'msg':'login required to send message.','user':'guest'})        #only show message to non-authenticated user 
#             })
             

#     def chat_message(self,event):
#          print('Event',event)                         #Event {'type': 'chat.message', 'message': '{"msg":"okaye"}'}
#          print('Event',event['message'])                               #Event {"msg":"okaye"}
#          print('Event type',type(event['message']))                  #Event type <class 'str'>
#          self.send({
#              'type':"websocket.send",
#              'text':event['message'],           #added this to get acknowledgment that message send successfully.
#          })
#          # for i in range(30):
#          #     self.send({
#          #         'type':'websocket.send',
#          #         'text': json.dumps(i),
#          #     })
#          #     sleep(1)

#     def websocket_disconnect(self,event):
#          print('websocket connection over',event)
#          print('channel layer....',self.channel_layer)
#          print('channel name....',self.channel_name)
#          async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
#          raise StopConsumer