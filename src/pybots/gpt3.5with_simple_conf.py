

def createBot(conf_text):
    """用简单的设定，创建一个机器人。"""
    def completion(context, chats):
        # TODO: 在发送请求给chatgpt之前， 把conf_text内容带进去。
        return chats

    return completion

if __name__ == "__main__":
    conf = input("请输入您的设定")
    completion = createBot(conf)
    chats = []
    context = {}
    while True:
        msg = input("用户(直接敲回车退出):")
        if not msg:
            break
        chats = chats + [{"role": "user", "name": "123", "content": msg}]
        chats = completion(context, chats)
        print("robot:", chats[-1]["content"])
        