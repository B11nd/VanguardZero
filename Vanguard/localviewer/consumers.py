import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import InMemoryChannelLayer

channel_layer = InMemoryChannelLayer()

class Dashboard(AsyncWebsocketConsumer):
    groups = ["broadcast"]
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print("server says disconnected")
    

    async def receive(self, text_data=None, bytes_data=None):
        print("server says client message received: ", text_data)
        await self.send("Server sends Welcome")
                
    async def send(self, event):
        pass
                        
    async def updatedashboard(self, event):
        user = event["text"]
        await self.send(json.dumps({"user": user}))
channel_name = "my_channel"