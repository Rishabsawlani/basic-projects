#first of all  we need to learn how to send notificaton through python 
# pip install plyer
'''from plyer import notification


notification.notify(
    title = 'testing',
    message = 'message',
    app_icon = None,
    timeout = 10,
)'''
#aagaya notification
#It takes four parameters:
#It takes four parameters:
#title The large header text at the top of a notification.
#message The longer, smaller text where you put more detailed information.
#app icon the image that appears next to tite and message
#timeout how long the message should show on screen



'''import time
from plyer import notification
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    time.sleep(5)
    #itne seconds baad program execute hoga 

    notification.notify( title = 'water reminder',message = 'its necessary to stay hydrated so dont forget to drink a glass of water regularly',app_icon = None,timeout = 10,)
    #iske karan pani pine ka notification aayega

    speaker.speak("its necessary to stay hydrated so dont forget to drink a glass of water regularly")
    #iske karan voice message aayega pani peene ke liye'''

#apan ne notification aur voice message dono kar diye pani peene ke liye 

'''import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    time.sleep(5)
    speaker.speak("its necessary to stay hydrated so dont forget to drink a glass of water regularly")'''
#isme sirf voice message aayega pani peene ke liye koi notification nahi 


import pyttsx3

def speak_notification(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak_notification("This is another speaking notification.")
