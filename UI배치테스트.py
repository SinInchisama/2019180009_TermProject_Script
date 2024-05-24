from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from ReadXML import *
from googlemaps import Client
from PIL import Image, ImageTk
import io


class MainGUI:
    def Search_Area(self):                  # 지역 검색처리하는 함수
        self.SearchM = self.Txt1.get()

        if(self.SearchM == "강원도"):
            self.SearchM = "강원특별자치도"

        self.Fires_Danger_Canvas.delete("all")
        self.Listbox_Mountain.delete(0, END)

        if (self.SearchM in self.Moutain.Danger_Dict.keys()):
            self.Print_Danger(self.SearchM)

            for key,item in self.Moutain.MoutainDict.items():
                if item[0] == self.SearchM:
                    self.Listbox_Mountain.insert(END, key)
        else:
            self.Init_All()

    def Search_Moutain(self):               # 산 검색을 처리하는 함수
        self.SearchA = self.Txt2.get()
        self.SearchM = None

        self.Fires_Danger_Canvas.delete("all")
        self.Listbox_Mountain.delete(0, END)

        if(self.SearchA in self.Moutain.MoutainDict.keys()):
            self.Print_Danger(self.Moutain.MoutainDict[self.SearchA][0])
            self.Listbox_Mountain.insert(END, self.SearchA)
        else:
            self.Init_All()

    def Print_Danger(self,Search):          # 산불 위험예보정보를 출력하는 함수
        self.Fires_Danger_Canvas.create_text(5, 18, text= Search, font=("Arial", 18), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 40, text="산불위험예보", font=("Arial", 18), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 80, text="최대 : " + self.Moutain.Danger_Dict[Search][0]                                         , font=("Arial", 14), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 120, text="최소 : " + self.Moutain.Danger_Dict[Search][2]
                                                 , font=("Arial", 14), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 160, text="평균 : " + self.Moutain.Danger_Dict[Search][1]
                                                 , font=("Arial", 14), anchor='w')

    def On_Select_Mountain(self):
        index = self.Listbox_Mountain.curselection()
        self.NowMoutain = self.Listbox_Mountain.get(index[0])
        self.Update_Map()

    def Init_All(self):                     # 초기화 하는 함수
        self.Fires_Danger_Canvas.create_text(0, 120, text="검색 결과가 없습니다", font=("Arial", 18), anchor='w')

    def Update_Map(self):
        gu_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=" \
                     f"{self.Moutain.MoutainDict[self.NowMoutain][2]},{self.Moutain.MoutainDict[self.NowMoutain][3]}&zoom={13}&size=400x400&maptype=roadmap"

        print(self.NowMoutain)
        
        response = requests.get(gu_map_url + '&key=' + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)
        self.Map_Lavel.configure(image=photo)
        self.Map_Lavel.image = photo

    def __init__(self):
        self.SearchM = None  # 마운틴 검색을 저장하는 변수
        self.SearchA = None  # 지역 검색을 저장하는 변수
        self.NowMoutain = None  # 산을 선택하면 저장되는 변수
        self.Moutain = Mountain()  # xml를 불러와서 저장하는 변수
        self.Google_API_Key = 'AIzaSyCo4pAx0xdjYC6zBsVXD9uiZ3BuaSWHDLE'
        self.initWindow()  # tkinter 윈도우를 초기화

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
        self.MoutainList_Canvas = Canvas(self.Frame1, width=150, height=520, bg="red")
        self.MoutainList_Canvas.place(x=10,y=120)

        self.Listbox_Mountain = Listbox(self.MoutainList_Canvas, selectmode=SINGLE, width=20, height=33)
        self.Listbox_Mountain.pack(side=LEFT)

        self.Scrolledbar_Mountain = Scrollbar(self.MoutainList_Canvas, orient=VERTICAL, command=self.Listbox_Mountain.yview)
        self.Scrolledbar_Mountain.pack(side=RIGHT, fill=Y)

        self.Listbox_Mountain.config(yscrollcommand=self.Scrolledbar_Mountain.set)

        self.Select_Mountain_Button= Button(self.Frame1, text =" 선택 ",command=self.On_Select_Mountain)
        self.Select_Mountain_Button.place(x=10, y=660, width=150, height=80)


        # 산불위험도를 출력하는 곳
        self.Fires_Danger_Canvas = Canvas(self.Frame1, width=220, height=220,bg = "red")
        self.Fires_Danger_Canvas.place(x=170,y=120)


        # 해발고도 그래프를 출력하는 곳
        self.Altitude_Canvas = Canvas(self.Frame1, width=590, height=386,bg = "yellow")
        self.Altitude_Canvas.place(x=170,y=350)


        # 지도를 출력하는 곳
        gu_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=" \
                     f"{self.Moutain.MoutainDict['가리산'][2]},{self.Moutain.MoutainDict['가리산'][3]}&zoom={13}&size=400x400&maptype=roadmap"

        response = requests.get(gu_map_url + '&key=' + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)

        self.Map_Lavel = Label(self.Frame1,image= photo)
        self.Map_Lavel.place(x=400,y= 20,width=360,height=320)


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