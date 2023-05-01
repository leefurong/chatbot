# A silly chatbot
# Who always says "You said:<Your last message content>".

def completion(context, chats):
    return chats + [{
        "role": "chatbot",
        "name": context.role_id,
        "content": "You said:"+chats[-1]["content"]
    }]

if __name__ == "__main__":
    class SillyContext():
        def __init__(self):
            self.role_id = "1"
    context = SillyContext()
    chats = [{"role": "user", "name": "123", "content": input()}]
    print(completion(context, chats)[-1]["content"])
