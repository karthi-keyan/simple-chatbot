import time
import os
from random import randint
import html
import speech_recognition as sr
from tkinter import *
import pyttsx3
from sinchsms import SinchSMS
from pygame import *
from bs4 import BeautifulSoup
import requests

whatcheck=int(0)
def playmusic():
    speech('tell me the song that i should play')
    count=int(0)
    m=int(0)
    inp=speechtotext()
    os.chdir('G:/songs')#change to your current directory
    files=os.listdir('G:/songs')#change to your current directory
    if inp=='random':
        k=randint(0,65)
        for each in files:
            count=count+1
            if count==k:
                mixer.init()
                mixer.music.load(each)
                mixer.music.play()
                s=int(input("to stop press 1     "))
                if s==1:
                    mixer.music.stop()
                    m=1
                
    for each in files:
        if each.startswith(inp):
            mixer.init()
            mixer.music.load(each)
            mixer.music.play()
    if m==0:
        s=int(input("to stop press 1      "))
        if s==1:
            mixer.music.stop()

    speech("should i play another song(1) or exit(0)   ")
    ch=int(input())
    if ch==1:
        playmusic()
    elif ch==0:
        pass
    

def speechtotext():
    speech("type")
    '''return str(input())'''#you can switch between voice and type input
    obj=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        try:
            audio=obj.listen(source)
            print(obj.recognize_google(audio))
            
        except :
            speech("type")
            return str(input())
            
    

    return str(obj.recognize_google(audio))

def smssend():
    client=SinchSMS(XXXXXXXXXXXX,XXXXXXXXXXXXX)#use your userID and password that you can get after creating the account 
    number=XXXXXXXXXXXXX#place the number that you want to send message
    speech("yes i can")
    speech("tell me the message")
    message=speechtotext()
    print('sending message to '+number)
    response=client.send_message(number,message)
    '''response=response['messages'][0]
    if response['status']=='0':
        speech("message was send succesfully")
    else:
        print("sorry error occurs")'''

def speech(talk):
    os.chdir("C:/Program Files (x86)/eSpeak/command_line")
    print(talk)
    engine=pyttsx3.init()
    engine.say(talk)
    engine.runAndWait()
def gameplay():
    speech('we will play stone paper scissor game')
    print("\nhow to play")
    speech("you have to say either stone or paper or scissor when i started the round then based on my simultanious decision point will be given for u or me")
    speech(" player who get 5 points first consired as a winner")
    compscore=int(0)
    playerscore=int(0)
    while(1):
        speech('stone    paper    scissor')
        i=randint(0,2)
        yourchoice={'stone':0,'paper':1,'scissor':2,0:'stone',1:'paper',2:'scissor'}
        j=yourchoice[speechtotext()]
        print('my choice   '+yourchoice[i])
        if [i,j] in [[0,2],[1,0],[2,1]]:
            compscore=compscore+1
            if compscore==5:
                speech("i won   better luck next time")
                break
        elif [i,j] in [[0,1],[1,2],[2,0]]:
            playerscore=playerscore+1
            if playerscore==5:
                speech("you won   congrats")
                break
        print('\nscore\nyourscore {}   myscore  {}'.format(playerscore,compscore))
    
def mathematician(s):
    whatcheck=1
    indiv=s
    result,flag,count=int(0),int(0),int(0)
    for each in indiv:
        if each=="addition" or each=="add":
            flag=1
        elif each=="subtract" or each=="subtraction":
            flag=2
        elif each=="multiply" or each=="multiplication":
            flag=3
        elif each=="divide" or each=="division":
            flag=4
    if flag in [1,2,3,4]:
        return calculate(flag,indiv)
    else:
        return None
def calculate(flag,indiv):
    result=int(0)
    spec,spec1=int(0),int(0)
    for each in indiv:
        if len(each.split(","))>1:
            sub=each.split(',')
            result=calculate(flag,sub)    
        if flag in [1,2,3,4]:
            try:
                if flag==1:
                    result=result+int(each)
                else:
                    if spec==0:
                        result=int(each)
                        spec=int(1)
                    else:
                        if flag==2:
                            result=result-int(each)
                        if flag==3:
                            result=result*int(each)
                        if flag==4:
                            result=result/int(each)
            except ValueError:
                pass

    return result
def search(senten):
    for each in senten:
        if each!='search' and each!='what' and each!='is' and each!='about':
            urllibrary='https://en.wikipedia.org/wiki/'+each
            break
    print(urllibrary)
    data=requests.get(urllibrary).text
    source=BeautifulSoup(data,'lxml')
    info=source.p.text
    speech(info)
    
def category(senten):
    senten=list(senten.split())
    if mathematician(senten) !=None:
     speech("solution is {}".format(mathematician(senten)))
    for each in senten:
        if each =="your" or each=="you" or each=='u' or each =="ur":
            aboutrex(senten)
        if each =="hi":
            speech("hi,nice to see u:)")
        if each=="who":
            speech("Iam a bot who think like <your name>")
        if each=="message":
            for each1 in senten:
                if each1=='send':
                    smssend()
        if each=="play":
            for each1 in senten:
                if each1=='game':
                    gameplay()
        if each=="play":
            for each1 in senten:
                if each1=='music' or each1=='song':
                    playmusic()
        if each=="bye":
            speech("bye take care and see u soon")
        if each =="time":
            for each1 in senten:
                if each1=="now":
                    speech(time.strftime("%H:%M:%S"))
        if whatcheck==0:
            if each=="what" or each=="search" :
                search(senten)
                    
        
    if "joke" in senten and "me" in senten and 'tell' in senten:
        joke()
def joke():
    os.chdir("C:/Users/karthi/Desktop/py/AI")
    repeat=[]
    sub=[]
    select=int(0)
    with open("jokes.txt","r") as cont:
        con=cont.readlines()
    j=randint(0,22)
    if j not in repeat:
        repeat.append(j)
    for each in con:
        if j==select:
            sub.append(each)
        if each=='\n':
            select=select+1
    for each in sub:
        speech(each)
    
    
def aboutrex(senten):
    for each in senten:
        if each =="age":
            speech("my age is 18")
        if each=="create" or each=="creater":
            speech("my creater is <your name>")
    if "tell" and "name"  and "her"in senten:
        speech("whose name :(")
        r=list(str(input()).split())
            
        if "your" and ("lover" or "girlfriend") in r:
            speech("her name is "+"<your crush name goes here>"+heart+heart+heart)
    elif "name" in senten:
        speech("my name is REX")
    if "love" and "in"  in senten:
        speech("yes,her name is"+"<your crush name goes here>"+heart+heart+heart)
        
print(" "*30+"**************")
heart=html.unescape("&hearts;")
for i in range(6):
    if i==1:
        print(" "*30+"*  *      *  *")
    elif i==4:
        print(" "*30+"*    ****    *")
    else:
        print(" "*30+"*"+" "*12+"*")
print(" "*30+"**************")
speech("\n Hi iam REX, what can i do for u")
i=int(0)
while i<10:
    inp=speechtotext()
    category(inp)
    
end=input()
