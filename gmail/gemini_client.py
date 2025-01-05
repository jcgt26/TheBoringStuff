import time
import google.generativeai as genai
import os

if __name__ =='__main__':
    abort_key = 'ctrl+c'
    gen_key = None
    try:
        gen_key = os.environ['GEMINI_KEY']
    except:
        print("API Key not found")
        
    
    genai.configure(api_key = gen_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[
        {'role': 'user', 'parts': 'I want you to see if the content i provide you is about any banking of financial topic, simply respond yes or no'}
    ])

    test_topics = ['My banking card has been stolen', 'my dog is red', 'your account number is 932334***']

    try:
        while True:
            entry = input("> ")
            if(entry == "BYE"):
                break
            for message in test_topics:
                for message_response in chat.send_message(message, stream=True):
                    print(message_response)
            time.sleep(0.5)
        print(chat.history)
    except KeyboardInterrupt:
        print('Bye') # ctrl + c
        

    response = model.generate_content("Explain how AI works")
    print(response.text)