#Boop And Headpat Counter Made By Bently#5823

import socket, time, re, shelve, asyncio, os
from pythonosc import udp_client

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 9001)) # Listens on port 9001 to get Vrc's Osc Output
client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # Makes a client to send data to Vrc's Osc Input

last_called_time = 0
call_count = 0

if not os.path.isfile('B_and_H.db'): # This Section Has To Make The Files Needed For Storing The Data
    db = shelve.open('B_and_H')
    db['boops:'] = 0
    db['headpats:'] = 0
    db.close()
    print("Shelve file created with initial starting data")

print("Starting Boop And Headpat Counter!")

async def noseboops():
    global last_called_time, call_count
    current_time = time.time()
    if current_time - last_called_time < 2:
        # increment the call count if the function was called within the last 2 seconds
        call_count += 1
        return
    last_called_time = current_time
    db = shelve.open('B_and_H')
    boops = db['boops:']
    boops += call_count  # increment the number of boops by the number of calls
    print("boops:", boops)
    db['boops:'] = boops
    db.close()
    client.send_message("/chatbox/input", [f"🐾 Boops : {boops} 🐾", True])
    call_count = 0  # reset the call count
    await asyncio.sleep(1)  # pause for 1 second
 
 
async def headpats():
    global last_called_time, call_count
    current_time = time.time()
    if current_time - last_called_time < 2:
        # increment the call count if the function was called within the last 2 seconds
        call_count += 1
        return
    last_called_time = current_time
    db = shelve.open('B_and_H')
    headpats = db['headpats:']
    headpats += call_count  # increment the number of headpats by the number of calls
    print("headpats:", headpats)
    db['headpats:'] = headpats
    db.close()
    client.send_message("/chatbox/input", [f"🐾 Headpats : {headpats} 🐾", True])
    call_count = 0  # reset the call count
    await asyncio.sleep(1)  # pause for 1 second

async def main():
    while True:
        data, address = sock.recvfrom(1024) # receive data from Vrc's Osc and process it making it easier to deal with
        output = data.decode('latin-1').replace("b'avatarparameters", "")
        output = re.sub(r'[^a-zA-Z0-9\s]', '', output)
        
        if "NoseBoopT" in output: # Here Goes The Paramater Name For The NoseBoop
            await noseboops()
            
        if "HeadPatT" in output: # Here Goes The Paramater Name For The Headpat
            await headpats()
                    
asyncio.run(main())