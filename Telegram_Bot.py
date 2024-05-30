import telegram

class Telegram_Bot:
    def __init__(self):
        Bot_Token = "7345270414:AAGeSMb4hen7L28HZR5dH3yzy6Y34b8raI4"
        self.Chat_Id = "7281344702"
        self.Bot = telegram.Bot(token=Bot_Token)

    def Pass_Message(self,Dict):
        for key,value in Dict.items():
            self.Bot.send_message(chat_id= self.Chat_Id,text = value)
