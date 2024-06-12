import asyncio
import telepot      # => 안되던 이유 : telegram으로 쓰고있어서
import ReadXML
import threading
from telepot.loop import MessageLoop

class Telegram_Bot:
    def Pass_Message(self,Dict):
        for key,value in Dict.items():
            self.Bot.sendMessage(chat_id= self.Chat_Id,text =key + "는 " + value)
        self.Bot.sendMessage(chat_id=self.Chat_Id, text='----------------------------------------------------------------------------------------------------')

    def replyAptData(self,user, loc_param):
        # 이부분은 데이터를 받아오는 부분인데 나는 다르게 바꿔서 #res_list = noti.getData(loc_param, date_param)
        res_list = self.getData(loc_param)
        for r in res_list:
            self.Pass_Message(r)

    def getData(self,loc_param):
        M_list = list()
        for key,item in ReadXML.Mountain_Data.MoutainDict.items():
            if(item['위치'] == loc_param):
                M_list.append({"산이름":key,'위치':item['위치'],'주소':item['주소'],'위도':item['위도'],'경도':item['경도'],'고도':item['고도']
                               })
        return M_list

    def Handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.Bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')
        if args[0] in ReadXML.CtpvNm and len(args) <2:
            if args[0] == '강원도':
                args[0] = '강원특별자치도'
            self.replyAptData(chat_id, args[0])
        elif args[0] in ReadXML.Mountain_Data.MoutainDict.keys():
            self.Pass_Message(ReadXML.Mountain_Data.MoutainDict[args[0]])
        else:
            self.Bot.sendMessage(chat_id, '모르는 명령어입니다.\n정확한 지역명 또는 산명을 알려주세요.')

    def run_telepot_bot(self):
        MessageLoop(self.Bot, self.Handle).run_as_thread()

    def __init__(self):
        Bot_Token = "7345270414:AAGeSMb4hen7L28HZR5dH3yzy6Y34b8raI4"
        self.Chat_Id = "7281344702"
        self.Bot = telepot.Bot(token=Bot_Token)
        #self.Bot.message_loop(Handle)
