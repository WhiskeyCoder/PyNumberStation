import time
from playsound import playsound
import threading
import base64

timeDelaySec = 600
haveMessage = True
ampSound = "backgroundnoise/amp.wav"
message_recive = input("What do you want to send: ")
message_convert = base64.b64encode(bytes(message_recive, 'utf-8'))
message1 = str(message_convert).replace("'", "").replace("=", "").strip()
message = message1[1:]

while haveMessage == True:
    playsound('Beep.wav')
    t = threading.Thread(target=playsound, args=(ampSound,))
    t.start()
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    print("last message was at: " + currentTime)
    print("message was: " + message)
    messageList = list(message)
    for listChar in messageList:
        soundChar = "numberstation/" + listChar + ".wav"
        playsound(soundChar)
    playsound('Beep.wav')
    time.sleep(timeDelaySec)
