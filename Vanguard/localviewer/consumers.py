import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Dashboard(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'mqtt'
        self.channel_name = 'mqtt'
        self.room_group_name = 'mqtts'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        #text_data_json = json.loads(text_data)
       # message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": 'ok'}
        )
        
        
    async def send(self, event):
        self.send(text_data=event["text"])
                
    async def updatedashboard(self, event):
        user = event["data"]
        await self.send(json.dumps({"user": user}))