# This Script Loops Through Messages That Get Shown In The Message Boxes  #
# Made By Bently#5823 #
import time
from pythonosc import udp_client
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
def loop():
    # Messages To Loop #
    client.send_message("/chatbox/input", ["Text Here Will Be Shown In The Chatbox", True])
    # Wait 10 Seconds Between Messages#
    time.sleep(10)
    client.send_message("/chatbox/input", ["Text Here Will Be Shown In The Chatbox", True])
    # Wait 3 Minutes #
	time.sleep(180)
	
while True:
	loop()