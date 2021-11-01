import json
import discord
client = discord.Client()
from websocket import create_connection
import time
    
                          

@client.event
async def on_message(message):
    if message.guild is None:
        return
    if message.author == client.user:
        return
    if message.content.startswith('!ring') and message.channel.id ==898963815545339924:
      #creating websocket connect on receving !ring 
      ws =create_connection("wss://as-pconnect3.coolkit.cc:8080/api/ws")
      #1 sec delay to make sure connection have been created
      time.sleep(1)
      #sending json file to send our device details to connect our device it is as we are passing username password for our device
      #this is how sonoff switch conenct with their device if you want to know how connecton works check network tab of and check WS connection.
      ws.send(json.dumps({
        "action": "userOnline",
        "version": 8,
        "ts": "1634291285",
        "at": "1e2ce4252d29537454e86f605a71c65390b5e2b8",
        "userAgent": "pc_ewelink",
        "apikey": "<your api>",
        "appid": "vcMG8oLY9CMf3CGg7g8tKlvatvPnRw84",
        "nonce": "uiwGpS4e",
        "sequence": "1634291284159"}))
      #than again delay of 1 sec so so are request can be sended
      time.sleep(1)
      #here this json send the siganl to switch to ring bell
      ws.send(json.dumps({
        "action": "update",
        "deviceid": "your deviceid",
        "apikey": "<your api>",
        "userAgent": "pc_ewelink",
        "sequence": "1634291338622",
        "params": {
        "switch": "on"
       },
     "selfApikey": "<api>"
}))
      embed = discord.Embed(title=f"{message.guild.name}",description=f"{message.author}**YOu successfully alerted the ghostdragon, don't ring the bell too many times as the real bell is in my room which can be very annoying.**",color=discord.Color.green())
      await message.channel.send(embed=embed)


    



client.run('<bot_token>')

