import openai
from dotenv import load_dotenv

fileopen = open("Data\Api.txt")
API = fileopen.read()
fileopen.close()


openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAnswer(question,chat_log = None):
    FileLog = open("DataBase\qna_log.txt","r+")
    chat_log_template = FileLog.read()
    # FileLog.close()
    
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nSpidey : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nSpidey : {answer}"
    Filelog = open("DataBase\qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer      


