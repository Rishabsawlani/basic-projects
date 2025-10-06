#first install win pywin by wind+r open cmd and write pip install pywin32

'''import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works!")'''
#confirming that it actually works lol now i can finally try to
#solve the exercise on my own


import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
c=(input("enter the names for which u want to get shoutouts seperated by comma:"))
for i in c.split(","):
    speaker.speak(f"shoutout to {i}")
#hogayi mujhse exercise solve yayyyyy!
