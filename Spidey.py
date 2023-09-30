from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Starting the Spidey : wait for some Second.")
from Features.Clap import Tester
from Body.Speak import Speak
import webbrowser
import pywhatkit


def ClapDetect(kk):

    query = Tester()
    if "True-Mic" == kk:
        print("")
        print(">> Clap Detected >>")
        print("")
        
    else:
        pass  
      
ClapDetect(kk=1)





def MainExecution():
    Speak("Hello sir")
    Speak("I'm Spidy, i'm Ready To Assist You Sir...!!")

    while True:

        Data = MicExecution()
        Data = str(Data)
        
        if len(Data)<=3:
            pass

        elif 'wake up' in Data:
            Speak('online and ready sir!')  
            
        
        elif 'alexa' in Data:
            Speak('who is alexa?')
            Speak('I am spidy sir!')    


        elif 'siri' in Data:
            Speak('who is siri?')
            Speak('I am spidy sir!')    

        elif 'play' in Data:
            Speak('playing ')
            pywhatkit.playonyt(Data) 

        elif 'sleep' in Data:
            Speak('as you wish sir!')   
            Speak('good night sir!')
            

        elif 'stop' in Data:
            Speak('shutting down!')
            exit()

        elif 'open youtube' in Data:
            webbrowser.open("https://youtube.com")

        
        elif 'open whatsapp' in Data:
            webbrowser.open("https://web.whatsapp.com") 
            Speak('opening whatsapp')

           
        elif 'open instagram' in Data:
            webbrowser.open("https://www.instagram.com") 
            Speak('opening') 

        elif 'open snapchat' in Data:
            webbrowser.open("https://web.snapchat.com") 
            Speak('opening')        
    

        
        else:

            Reply = ReplyBrain(Data)
            Speak(Reply)
MainExecution()






