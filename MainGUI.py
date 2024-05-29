from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from ReadXML import *
from googlemaps import Client
from PIL import Image, ImageTk
import io
import Telegram_Bot
import asyncio
import G_email

class MainGUI:
    def Search_Area(self):                  # 지역 검색처리하는 함수
        self.Init_All()

        self.SearchM = self.Txt1.get()

        if(self.SearchM == "강원도"):
            self.SearchM = "강원특별자치도"

        if (self.SearchM in self.Moutain.Danger_Dict.keys()):
            self.Print_Danger(self.SearchM)

            i = 0

            for key,item in self.Moutain.MoutainDict.items():
                if(key == '강천산'):
                    print(item['위치'],self.SearchM)
                if item['위치'] == self.SearchM:
                    self.Listbox_Mountain.insert(END, key)

                    self.Altitude_Canvas.create_rectangle(self.Graph_Width * i + 10 ,self.Graph_height * (2000-eval(item['고도'])) +20
                                                          ,self.Graph_Width * (i+1)+10,389 - 20,tags='shape')
                    self.Altitude_Canvas.create_text(self.Graph_Width * i + 25,
                                                          self.Graph_height * (2000 - eval(item['고도'])) + 10,text = item['고도'], tags='shape',font=("Arial", 6))
                    self.Altitude_Canvas.create_text(self.Graph_Width * i + 25,
                                                     389-10,
                                                     text=key, tags='shape',font=("Arial", 6))
                    i += 1
        else:
            self.Fires_Danger_Canvas.create_text(0, 120, text="검색 결과가 없습니다", font=("Arial", 18), anchor='w')

    def Search_Moutain(self):               # 산 검색을 처리하는 함수
        self.Init_All()

        self.SearchA = self.Txt2.get()

        if(self.SearchA in self.Moutain.MoutainDict.keys()):
            self.Print_Danger(self.Moutain.MoutainDict[self.SearchA]['위치'])
            self.Listbox_Mountain.insert(END, self.SearchA)

            self.Altitude_Canvas.create_rectangle(10,
                                                  self.Graph_height * (2000 - eval(self.Moutain.MoutainDict[self.SearchA]['고도'])) + 20
                                                  , self.Graph_Width + 10, 389 - 20, tags='shape')
            self.Altitude_Canvas.create_text(+ 25,
                                             self.Graph_height * (2000 - eval(self.Moutain.MoutainDict[self.SearchA]['고도'])) + 10, text=self.Moutain.MoutainDict[self.SearchA]['고도'],
                                             tags='shape', font=("Arial", 6))
            self.Altitude_Canvas.create_text(+ 25,
                                             389 - 10,
                                             text=self.SearchA, tags='shape', font=("Arial", 6))
        else:
            self.Fires_Danger_Canvas.create_text(0, 120, text="검색 결과가 없습니다", font=("Arial", 18), anchor='w')

    def Print_Danger(self,Search):          # 산불 위험예보정보를 출력하는 함수
        self.Fires_Danger_Canvas.create_text(5, 18, text= Search, font=("Arial", 18), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 40, text="산불위험예보", font=("Arial", 18), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 80, text="최대 : " + self.Moutain.Danger_Dict[Search][0], font=("Arial", 14), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 120, text="최소 : " + self.Moutain.Danger_Dict[Search][2]
                                                 , font=("Arial", 14), anchor='w')
        self.Fires_Danger_Canvas.create_text(5, 160, text="평균 : " + self.Moutain.Danger_Dict[Search][1]
                                                 , font=("Arial", 14), anchor='w')

    def On_Select_Mountain(self):           # 산 리스트에서 산을 선택하는 함수
        self.Listbox_Transport.delete(0, END)
        index = self.Listbox_Mountain.curselection()
        self.NowMoutain = self.Listbox_Mountain.get(index[0])
        self.Update_TransPort()
        self.Update_Map()
        self.Update_Image()
        self.Update_Information()

    def On_Select_TransPort(self):
        index = self.Listbox_Transport.curselection()
        self.NowTransPort = self.Listbox_Transport.get(index[0])


        gu_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=" \
                     f"{self.Moutain.MoutainDict[self.NowMoutain]['대중교통'][self.NowTransPort].lat},{self.Moutain.MoutainDict[self.NowMoutain]['대중교통'][self.NowTransPort].lot}&zoom={11}&size=400x400&maptype=roadmap"

        marker_url = f"&markers=color:red%7C{self.Moutain.MoutainDict[self.NowMoutain]['대중교통'][self.NowTransPort].lat},{self.Moutain.MoutainDict[self.NowMoutain]['대중교통'][self.NowTransPort].lot}"

        gu_map_url += marker_url

        response = requests.get(gu_map_url + '&key=' + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)
        self.Transport_Map_Lavel.configure(image=photo)
        self.Transport_Map_Lavel.image = photo


    def Init_All(self):                     # 초기화 하는 함수
        self.SearchA = None
        self.SearchM = None
        self.Fires_Danger_Canvas.delete("all")
        self.Listbox_Mountain.delete(0, END)
        self.Listbox_Transport.delete(0,END)
        self.Transport_Map_Lavel.configure(image=self.photo)
        self.Map_Lavel.configure(image=self.photo)
        self.Image_Lavel.configure(image=self.photo)
        self.Transport_Map_Lavel.image = self.photo
        self.Map_Lavel.image = self.photo
        self.Image_Lavel.image = self.photo
        self.Altitude_Canvas.delete('shape')

    def Update_Map(self):
        gu_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=" \
                     f"{self.Moutain.MoutainDict[self.NowMoutain]['위도']},{self.Moutain.MoutainDict[self.NowMoutain]['경도']}&zoom={11}&size=400x400&maptype=roadmap"


        marker_url = f"&markers=color:red%7C{self.Moutain.MoutainDict[self.NowMoutain]['위도']},{self.Moutain.MoutainDict[self.NowMoutain]['경도']}"

        gu_map_url+= marker_url
        
        response = requests.get(gu_map_url + '&key=' + self.Google_API_Key)
        image = Image.open(io.BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)
        self.Map_Lavel.configure(image=photo)
        self.Map_Lavel.image = photo

    def Update_Image(self):
        image = Image.open('image/mountain/'+self.NowMoutain+".jpg")
        photo = ImageTk.PhotoImage(image)
        self.Image_Lavel.configure(image=photo)
        self.Image_Lavel.image = photo

    def Update_Information(self):
        self.Data_Canvas.delete('all')
        self.Data_Canvas.create_text(5, 18, text= '산 이름은 ' + self.NowMoutain, font=("Arial", 14), anchor='w')
        self.Data_Canvas.create_text(5, 40, text= '위치는 ' + self.Moutain.MoutainDict[self.NowMoutain]['위치'], font=("Arial", 14), anchor='w')
        self.Data_Canvas.create_text(5, 62, text='주소는 ' + self.Moutain.MoutainDict[self.NowMoutain]['주소'],
                                     font=("Arial", 10), anchor='w')
        self.Data_Canvas.create_text(5, 84, text='위도는 ' + self.Moutain.MoutainDict[self.NowMoutain]['위도'],
                                     font=("Arial", 14), anchor='w')
        self.Data_Canvas.create_text(5, 106, text='경도는 ' + self.Moutain.MoutainDict[self.NowMoutain]['경도'],
                                     font=("Arial", 14), anchor='w')

    def Update_TransPort(self):
        if(self.Moutain.MoutainDict[self.NowMoutain]['대중교통']):
            for Key,Value in self.Moutain.MoutainDict[self.NowMoutain]['대중교통'].items():
                 self.Listbox_Transport.insert(END, Key)
        else:
            self.Listbox_Transport.insert(END, "입력된 대중교통 정보가 없습니다.")

    def Send_Email(self):
        if(self.NowMoutain):
            G_email.Pass_Email(self.NowMoutain,self.Moutain.MoutainDict[self.NowMoutain])

    def Send_Telegram(self):
        if (self.NowMoutain):
            asyncio.run(self.Telegram.Pass_Message(self.Moutain.MoutainDict[self.NowMoutain]))


    def __init__(self):
        self.SearchM = None  # 마운틴 검색을 저장하는 변수
        self.SearchA = None  # 지역 검색을 저장하는 변수
        self.NowMoutain = None  # 산을 선택하면 저장되는 변수
        self.NowTransPort = None # 대중교통을 선택하면 저장되는 변수
        self.Moutain = Mountain()  # xml를 불러와서 저장하는 변수
        self.Telegram = Telegram_Bot.Telegram_Bot()     # 텔레그램 봇 생성
        self.Google_API_Key = 'AIzaSyCo4pAx0xdjYC6zBsVXD9uiZ3BuaSWHDLE'
        self.Graph_height = 389 / 2000
        self.Graph_Width = (590-20) / 21
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
        self.Fires_Danger_Canvas = Canvas(self.Frame1, width=220, height=220,bg = "light gray")
        self.Fires_Danger_Canvas.place(x=170,y=120)


        # 해발고도 그래프를 출력하는 곳
        self.Altitude_Canvas = Canvas(self.Frame1, width=590, height=386,bg = "light gray")
        self.Altitude_Canvas.place(x=170,y=350)

        # 지도를 출력하는 곳
        image = Image.open('image/Search_Nothing.jpg')
        self.photo = ImageTk.PhotoImage(image)

        self.Map_Lavel = Label(self.Frame1,image= self.photo)
        self.Map_Lavel.place(x=400,y= 20,width=360,height=320)

        #---------------------------------------------------------------------------------------------------------------
        # Frame2 세부정보창에 대한 프레임

        self.Frame2 = Frame(self.Note, width=780, height=780)
        self.Note.add(self.Frame2,text = " 정보 ")

        # 선택한 산의 교통시설을 보여주는 스크롤바

        self.Transport_Canvas = Canvas(self.Frame2, width=150, height=320, bg="light gray")
        self.Transport_Canvas.place(x=10, y=20)

        self.Listbox_Transport = Listbox(self.Transport_Canvas, selectmode=SINGLE, width=40, height=20)
        self.Listbox_Transport.pack(side=LEFT)

        self.Scrolledbar_Transport = Scrollbar(self.Transport_Canvas, orient=VERTICAL,
                                              command=self.Listbox_Transport.yview)
        self.Scrolledbar_Transport.pack(side=RIGHT, fill=Y)

        self.Listbox_Transport.config(yscrollcommand=self.Scrolledbar_Transport.set)

        # 교통 시설 선택 버튼

        self.Select_Transport_Button = Button(self.Frame2,text = " 선택 ",command=self.On_Select_TransPort)
        self.Select_Transport_Button.place(x=350,y=40,width=100, height=80)


        # 텔레그램 선택 버튼
        image1 = Image.open('image/Telegram.jpg')
        photo = ImageTk.PhotoImage(image1)

        self.Select_Telegram_Button = Button(self.Frame2,text = " 텔레그램 ",image=photo,command=self.Send_Telegram)
        self.Select_Telegram_Button.place(x=350,y=140,width=100, height=80)


        # 메일 선택 버튼
        image = Image.open('image/gmail.JPG')
        photo1 = ImageTk.PhotoImage(image)

        self.Select_Telegram_Button = Button(self.Frame2,text = " 메일 ",image= photo1,command= self.Send_Email)
        self.Select_Telegram_Button.place(x=350,y=240,width=100, height=80)


        # 교통시설의 지도를 그리는 캔버스
        self.Transport_Map_Lavel = Label(self.Frame2,image = self.photo)
        self.Transport_Map_Lavel.place(x=500,y= 20, width=265, height=320)

        # 정보들을 출력하는 캔버스
        self.Data_Canvas = Canvas(self.Frame2, width=480, height=360,bg = "light gray")
        self.Data_Canvas.place(x=10,y= 380)


        # 산 이미지를 출력하는 캔버스
        self.Image_Lavel = Label(self.Frame2, image=self.photo)
        self.Image_Lavel.place(x=500, y=380, width=265, height=360)

        self.Window.mainloop()

MainGUI()