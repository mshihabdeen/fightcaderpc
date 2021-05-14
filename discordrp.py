from pypresence import Presence
import time


client_id = "840595380983169024"
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
RPC.update(state="In Lobby", details="Street Fighter III: Third Strike", large_image="sflogo",large_text="Street Fighter III: Third Strike",small_image="logo",small_text="Fightcade 2",start=time.time(),buttons=[{"label": "click the funny button", "url": "https://www.youtube.com/watch?v=xvFZjo5PgG0"}])

while True:  # The presence will stay on as long as the program is running
    time.sleep(5) # Can only update rich presence every 5 seconds
