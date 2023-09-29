from Body.Speak import Speak
from Features.Clap import Tester
from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting the Spidey : wait for some Second.")
from Body.Speak import Speak
from Features.Clap import Tester



   

def Main():
    Tester()
    Speak("Welcome Sir")
    Speak("I'm Spidy, i'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()

        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)



def ClapDetect():
    query = Tester()
        
      




if __name__ == "__main__":
    Main()
    ClapDetect()