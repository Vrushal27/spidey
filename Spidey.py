from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Starting the Spidey : wait for some Second.")
from Features.Clap import Tester
from Body.Speak import Speak


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
 

        if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)
        else:

            Reply = ReplyBrain(Data)
            Speak(Reply)
MainExecution()






