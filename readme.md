                                    ------------------> Index <----------------------
        
    Intro

    Consumers





--------------------------------------------------------------------------------------------------------------------


Install Django Channels - pip install channnels

        ----------------> Steps to follow <--------------------

Step-1: Create Normal Django project then add channels in its settings.py-> installed app section

        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            'channels',
        ]

                    +

        ASGI_APPLICATION = "gs1.asgi.application"

Step-2: Create Consumer.py

        from channels.consumer import SyncConsumer,AsyncConsumer

        class MySyncConsumer(SyncConsumer):
            def websocket_connect(self,event):
                print('websocket_conneect')
            
            def websocket_receive(self,event):
                print('websocket data receive')

            def websocket_disconnect(self,event):
                print('websocket disconnect')

step-3: Create Routing.py

        from django.urls import path
        from . import consumers

        websocket_urlpatterns = [
            path('ws/sc/',consumers.MySyncConsumer.as_asgi())
        ]

step-4: Add this routing.py in asgi.py

        from channels.routing import ProtocolTypeRouter,URLRouter
        import app.routing

        application = ProtocolTypeRouting(
            {
                'http': get_asgi_application(),
                'websocket':URLRouter(
                    app.routing.websocket_urlpatterns,
                )
            }
        )




--------------------------------------------------------------------------------------------------------------------

                                ----------------> Consumers in channels <----------------

    Consumers are basic unit of Django Code. Consumers are like Django Views.

    Sure! Think of consumers as workers in a factory. In a WebSocket-based application, clients (like web browsers) send messages to the server over WebSocket connections. Consumers are like workers who receive these messages and do something with them.

Here's a breakdown:

1. **WebSocket Connection**: When a client connects to your server over WebSocket, it's like a customer entering a store.

2. **Consumer**: A consumer is like a worker assigned to handle a specific type of task. In this case, it's handling messages from WebSocket connections.

3. **Connect Method**: When a client connects, the `connect` method of the consumer is like the worker greeting the customer. It prepares to handle messages from that customer.

4. **Receive Method**: When the client sends a message, it's like the customer giving a request or asking for something. The `receive` method of the consumer is like the worker receiving this request. The worker then processes the request and decides what to do next.

5. **Disconnect Method**: When the client disconnects, it's like the customer leaving the store. The `disconnect` method of the consumer is like the worker tidying up after the customer and getting ready for the next one.

So, consumers are essentially the workers in your WebSocket-based application who handle incoming messages from clients, do something with them, and possibly send responses back.


                            -------------------> Consumers Type <------------------

    SyncConsumer    And     AsyncConsumer


SyncConsumer

Step-1: Create Project then on your app add file name Consumer.py 

            from channels.consumer import SyncConsumer

            class MySyncConsumer(SyncConsumer):         #inherited SyncConsumer

            #some predifined handlers
                def websocket_connect(self,event):      #calls when cliet initially opens a connection
                    print('Websocket connect')

                def websocket_receive(self,event):      #calls when data received fro client
                    print('websocket Received')

                def websocket_disconnect(self,event):   #calls when connection to the client is lost
                    print('websocket disconnect')   

----------------------------------------------------------------------------------------------------


AsyncConsumer - just add async before function.

ques. Why to use AsyncConsumer?
Ans.  AsyncConsumer allows handling multiple events simultaneously without blocking, improving performance,         scalability, and responsiveness.

Step-1: Create Project then on your app add file name Consumer.py 

            from channels.consumer import SyncConsumer

            class MyAsyncConsumer(AsyncConsumer):         #inherited SyncConsumer

            #some predifined handlers
                async def websocket_connect(self,event):      #calls when cliet initially opens a connection
                    print('Websocket connect')

                async def websocket_receive(self,event):      #calls when data received fro client
                    print('websocket Received')

                async def websocket_disconnect(self,event):   #calls when connection to the client is lost
                    print('websocket disconnect')   


-------------------------------------------------------------------------------------------------------------------

                                --------------> Routing <-------------------

Imagine you're working at a postal office, and your job is to sort incoming mail and direct it to the correct departments or recipients. This process is similar to routing in Django Channels, where incoming messages (or events) are directed to the appropriate consumers for processing.

Here's how it works:

Incoming Mail (Messages):
        Incoming mail arrives at the postal office from various sources, such as different neighborhoods or cities. Similarly, in Django Channels, messages (or events) arrive at the server from different clients or channels, such as WebSocket connections.

Sorting (Routing):
        Your task at the postal office is to sort the mail based on the destination address or department. Similarly, in Django Channels, routing determines which consumer should handle each incoming message based on specific criteria, such as the message type or URL path.

Routing Table (URLRouter):
        Just like you have a sorting system or routing table at the postal office to determine where each piece of mail should go, Django Channels uses a routing table (implemented as a URLRouter) to map incoming messages to the appropriate consumers.

Sending Mail (Processing):
        Once the mail is sorted, it's sent to the respective departments or recipients for further processing. Similarly, in Django Channels, once a message is routed to the appropriate consumer, it's processed accordingly, whether it's sending a response, broadcasting to other clients, or performing some other action.



we call as_asgi() classmethod when routing our consumers.
THis will return Asgi wrapper application that will instantiate a new consumer instance for each connection or scope

we can write routing urls in asgi.py but that's not a good practise according to me.

-------> We will create routing.py file

    from django.urls import path
    from . import consumers

    websocket_urlpatterns = [
        path('ws/sc/',consumers.MySyncCOnsumers.as_asgi())
    ]


    -----------> Now we have to mention that to our asgi.py