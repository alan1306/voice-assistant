# import speech_recognition as sr
from automation import *
# r=sr.Recognizer()
# def talk(audio):
#     p.say(audio)
#     p.runAndWait()
# def listen():
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print("Listening....")
#         audio=r.listen(source)
#     try:
#         audioText=r.recognize_google(audio)
#         print(audioText)
#         return audioText     
#     except Exception as e:
#         print("say that again please")
#         return None
resume = True
while(resume):
    audioText=listen()
    if(audioText!=None):
        audioText=audioText.lower()
        searchCondition=audioText=="google" or audioText=="youtube" or audioText.find("search")==0 or audioText.find("download")==0
        if searchCondition:
            webSearch(audioText)             
        if audioText.lower()=="stop":
            resume=False
