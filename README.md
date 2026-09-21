# Minecraft Bot

A Discord bot made for administrating a Minecraft server. It runs on my home server running Ubuntu Server.

## Features
🟢 Start the Minecraft server with !start_server  
🔴 Stop the Minecraft server with !stop_server  
📊 Check whether the server is running with !server_status  
👥 See which players are online with !spiller_liste  
⚙️ Run Minecraft commands directly through Discord with !command  
## Examples
!server_status  
!start_server  
!stop_server  
!spiller_liste  

!command list  
!command time set day  
!command weather clear  
!command give Dissing2006 diamond 10  
!command say Hello from Discord!  

The !command command forwards the entered Minecraft command to the server using RCON.

## Technologies
Python  
discord.py  
Minecraft Paper  
RCON  
Ubuntu Server  
systemd  
Architecture  
Discord  
   ↓  
Discord Bot  
   ↓  
RCON  
   ↓  
Minecraft Paper Server  
   ↓  
Ubuntu Home Server  

The bot runs as a systemd service on the same Ubuntu server as the Minecraft server.

## Purpose
The purpose was to play around with my home server to learn linux while also implementing something fun. 
