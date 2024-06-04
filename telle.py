import telepot
import noti

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지역') and len(args)>1:
        print('try to 지역', args[1])
        replyAptData( '201801', chat_id, args[1] )
    elif text.startswith('저장')  and len(args)>1:
        print('try to 저장', args[1])
        save( chat_id, args[1] )
    elif text.startswith('확인'):
        print('try to 확인')
        check( chat_id )
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [지역번호], 저장 [지역번호], 확인 중 하나의 명령을 입력하세요.')
