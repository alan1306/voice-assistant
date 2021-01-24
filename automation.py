import pyttsx3 as pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import os
import time
import pyperclip
from pytube import YouTube
from pytube.cli import on_progress
p=pyttsx3.init()
import speech_recognition as sr
r=sr.Recognizer()
path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
webbrowser.register("wb", None, webbrowser.BackgroundBrowser(path))
webbrowser=webbrowser.get("wb")
def talk(audio):
    p.say(audio)
    p.runAndWait()
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio=r.listen(source)
    try:
        audioText=r.recognize_google(audio)
        print(audioText)
        return audioText     
    except Exception as e:
        print("say that again please")
        return None
def webSearch(audioText):
    global currentTab
    if(audioText=="google"):
        currentTab="google"
        openGoogle()
    elif(audioText=="youtube"):
        currentTab="youtube"
        print("in websearch")
        openYoutube() 
    elif(audioText.find("search")==0):
        if "youtube" in audioText:
            if("in youtube" in audioText):
                searchQuery=audioText[7:-11]
            else:
                searchQuery=audioText[7:-8]
            searchYoutube(searchQuery)        
        elif "google" in audioText:
            if("in google" in audioText):
                searchQuery=audioText[7:-10]
            else:
                searchQuery=audioText[7:-7]
            searchGoogle(searchQuery)
        else:                
            searchQuery=audioText[7:]
            if currentTab=="youtube":
                print("in youtube")
                searchYoutube(searchQuery)
            elif currentTab=="google":
                searchGoogle(searchQuery)
    elif "download" in audioText:
        talk("right click on the vedio click on copy vedio url and say yes")
        confirmation=""
        while confirmation!="yes":
           confirmation=listen()
           if confirmation=="yes":
                link=pyperclip.paste()
                link1=link[12:19]
                link2=link[8:16]
                if link1!="youtube" and link2!="youtu.be":
                    talk("link is not correct")
                    confirmation=""
           if confirmation=="stop" or confirmation=="close":
                break
        if confirmation=="yes":
            downloadYotube()             
def openGoogle():
    url="https://www.google.com/"
    webbrowser.open(url)
def openYoutube():
    print("in youtube")
    url="https://www.youtube.com/"
    webbrowser.open(url)
def searchYoutube(searchQuery):
    searchQuery.replace(" ","+")    
    url="https://www.youtube.com/results?search_query="+searchQuery
    webbrowser.open(url)
def searchGoogle(searchQuery):
    searchQuery.replace(" ","+")
    url="https://www.google.com/?#q="+searchQuery
    webbrowser.open(url) 
def downloadYotube():
    link=pyperclip.paste()
    vedioAvailable=False
    audioAvailable=False
    yt=YouTube(link,on_progress_callback=on_progress)
    vedioList=yt.streams.filter(progressive="True")
    audioList=yt.streams.filter(only_audio="True")
    if vedioList:
        vedioAvailable=True
        talk("which resolution do you want to download")
        talk("available resolutions are")
        if vedioList.get_by_resolution("720p"):
            talk("720 pixel")
        if vedioList.get_by_resolution("420p"):
            talk("480 pixel")
        if vedioList.get_by_resolution("360p"):
            talk("360 pixel")               
        if vedioList.get_by_resolution("240p"):
            talk("240 pixel")
    else:
        talk("sorry vedio not available for download")
    if audioList:    

        audioAvailable=True       
        talk("or do you want to download audio only")
    else:
        talk("audio also not available")  
    if vedioAvailable or audioAvailable:            
        getResolution=""
        while getResolution!="720" and getResolution!="480" and getResolution!="360" and getResolution!="240":
            getResolution=listen()
            if getResolution!= None and "audio" in getResolution:
                break
        if "audio" not in getResolution: 
            vedio=vedioList.get_by_resolution(getResolution+"p")
            vedio.download() 
        else:
            audioList.first().download()                     