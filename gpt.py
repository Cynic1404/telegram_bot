import g4f

def ask_gpt(messages):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages)
    print(response)
    return response

def check_first_message(messages):
    if not messages:
        return "Start your chat: \n"
    else:
        return "Your message: \n"

messages = []

if __name__=="__main__":
    while True:
        question = input(check_first_message(messages))
        if question == "new_chat":
            messages=[]
            question = input(check_first_message(messages))
        messages.append({"role":"user", "content":question})
        answer=ask_gpt(messages=messages)
        messages.append({"role":"assistant", "content":answer})