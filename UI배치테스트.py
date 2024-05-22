from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

class MainGUI:
    def Search_Area(self):
        self.SelectM = self.Txt1.get()

    def Search_Moutain(self):
        self.SelectA = self.Txt2.get()
        self.SelectM = None

    def __init__(self):
        self.SelectM = None     # 마운틴 검색을 저장하는 변수
        self.SelectA = None     # 지역 검색을 저장하는 변수
        self.initWindow()       # tkinter 윈도우를 초기화

    def initWindow(self):
        self.Window = Tk()
        self.Window.title("등산가는길")
        self.Window.geometry("800x800")

        # Frame1 검색창에 대한 프레임

        self.Note = Notebook(self.Window)
        self.Note.place(x=10, y=10, width=780, height=780)

        self.Frame1 = Frame(self.Note, width=780, height=780)
        self.Note.add(self.Frame1,text = " 검색 ")

        # 지역 검색창 그리기
        Search_Area_Text = Label(self.Frame1, text=" 지역 검색창(광역시나 자치도를 입력해주세요) ")
        Search_Area_Text.place(x=20,y=0)

        self.Txt1 = Entry(self.Frame1)
        self.Txt1.place(x=10,y=20, width=280, height=30)

        self.Search_Area_Button = Button(self.Frame1,text = " 검색 ",command=self.Search_Area)
        self.Search_Area_Button.place(x=300,y=22)


        # 산 검색창 그리기
        Guide_Moutain = Label(self.Frame1, text=" 산 검색창 ")
        Guide_Moutain.place(x=20,y=50)

        self.Txt2 = Entry(self.Frame1,width= 40)
        self.Txt2.place(x=10,y=70, width=280, height=30)

        self.Search_Moutain_Button = Button(self.Frame1,text = " 검색 ",command=self.Search_Moutain)
        self.Search_Moutain_Button.place(x=300,y=72)


        # 산 목록을 출력하는 곳
        self.Scrolled_Moutain = ScrolledText(self.Frame1,width=20,height=40)
        self.Scrolled_Moutain.place(x= 10 ,y=120)

        self.Select_Mountain= Button(self.Frame1,text = " 선택 ")
        self.Select_Mountain.place(x=10,y=660,width=150, height=80)


        # 산불위험도를 출력하는 곳
        self.Fires_Danger_Canvas = Canvas(self.Frame1, width=220, height=220,bg = "red")
        self.Fires_Danger_Canvas.place(x=170,y=120)


        # 해발고도 그래프를 출력하는 곳
        self.Altitude_Canvas = Canvas(self.Frame1, width=590, height=386,bg = "yellow")
        self.Altitude_Canvas.place(x=170,y=350)


        # 지도를 출력하는 곳
        self.Map_Canvas = Canvas(self.Frame1, width=360, height=320,bg = "blue")
        self.Map_Canvas.place(x=400,y= 20)




        # Frame2 세부정보창에 대한 프레임

        self.Frame2 = Frame(self.Note, width=780, height=780)
        self.Note.add(self.Frame2,text = " 정보 ")

        # 선택한 산의 교통시설을 보여주는 스크롤바

        self.Scrolled_Transport = ScrolledText(self.Frame2,width=40,height=25)
        self.Scrolled_Transport.place(x= 10 ,y=20)


        # 교통 시설 선택 버튼
        self.Select_Transport_Button = Button(self.Frame2,text = " 선택 ")
        self.Select_Transport_Button.place(x=350,y=40,width=100, height=80)


        # 텔레그램 선택 버튼
        self.Select_Telegram_Button = Button(self.Frame2,text = " 텔레그램 ")
        self.Select_Telegram_Button.place(x=350,y=140,width=100, height=80)


        # 메일 선택 버튼
        self.Select_Telegram_Button = Button(self.Frame2,text = " 메일 ")
        self.Select_Telegram_Button.place(x=350,y=240,width=100, height=80)


        # 교통시설의 지도를 그리는 캔버스
        self.Map_Canvas = Canvas(self.Frame2, width=265, height=320,bg = "blue")
        self.Map_Canvas.place(x=500,y= 20)


        # 정보들을 출력하는 캔버스
        self.Data_Canvas = Canvas(self.Frame2, width=480, height=360,bg = "blue")
        self.Data_Canvas.place(x=10,y= 380)


        # 산 이미지를 출력하는 캔버스
        self.Image_Canvas = Canvas(self.Frame2, width=265, height=360,bg = "yellow")
        self.Image_Canvas.place(x=500,y= 380)

        self.Window.mainloop()

MainGUI()