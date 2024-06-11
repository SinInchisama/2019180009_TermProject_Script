import asyncio
import telepot      # => 안되던 이유 : telegram으로 쓰고있어서
import ReadXML

class Telegram_Bot:
    def Pass_Message(self,Dict):
        for key,value in Dict.items():
            self.Bot.sendMessage(chat_id= self.Chat_Id,text = value)

    def Handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.Bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')

        if args[0] in ReadXML.CtpvNm and args <2:




    def __init__(self):
        Bot_Token = "7345270414:AAGeSMb4hen7L28HZR5dH3yzy6Y34b8raI4"
        self.Chat_Id = "7281344702"
        self.Bot = telepot.Bot(token=Bot_Token)
        self.Bot.message_loop(Handle)
