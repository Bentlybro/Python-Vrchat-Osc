#Made By BentlyBro For Public Use. This Can Not Be Used In Any Commercial Way
import time
from pythonosc import udp_client
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
#start timer straight away
start = time.perf_counter()
def timer():
    elapsed = time.perf_counter() - start
    
    # Convert elapsed time to seconds
    seconds = int(elapsed)
    
    # Calculate number of hours and remaining minutes
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    if seconds >= 3600:
        #if time is at least one hour
        # Print elapsed time in hours and minutes
        print(f"{hours} hours and {minutes} minutes.")
        client.send_message("/chatbox/input", [f"[ I Have Been In Vrc For {hours} Hours And {minutes} Minutes ]", True])
    else:
        # If time is less than one hour
        # Print elapsed time in minutes and seconds
        print(f"{minutes} minutes")
        client.send_message("/chatbox/input", [f"[ I Have Been In Vrc For {minutes} Minutes ]", True])
        
    #wait 3 minutes before restarting the script
    time.sleep(180)
    
while True:
    timer()