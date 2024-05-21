from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

Window = Tk()
Window.title("등산가는길")
Window.geometry("800x800")

# Frame1 검색창에 대한 프레임

Note = Notebook(Window)
Note.place(x=10, y=10, width=780, height=780)
'''
Frame1 = Frame(Note, width=780, height=780)
Note.add(Frame1,text = " 검색 ")

# 지역 검색창 그리기
Search_Area_Text = Label(Frame1, text=" 지역 검색창(광역시나 자치도를 입력해주세요) ")
Search_Area_Text.place(x=20,y=0)

Txt1 = Entry(Frame1)
Txt1.place(x=10,y=20, width=280, height=30)

Search_Area_Button = Button(Frame1,text = " 검색 ")
Search_Area_Button.place(x=300,y=22)


# 산 검색창 그리기
Guide_Moutain = Label(Frame1, text=" 산 검색창 ")
Guide_Moutain.place(x=20,y=50)

Txt2 = Entry(Frame1,width= 40)
Txt2.place(x=10,y=70, width=280, height=30)

Search_Area_Button = Button(Frame1,text = " 검색 ")
Search_Area_Button.place(x=300,y=72)


# 산 목록을 출력하는 곳
Scrolled_Moutain = ScrolledText(Frame1,width=20,height=40)
Scrolled_Moutain.place(x= 10 ,y=120)

Select_Mountain= Button(Frame1,text = " 선택 ")
Select_Mountain.place(x=10,y=660,width=150, height=80)


# 산불위험도를 출력하는 곳
Fires_Danger_Canvas = Canvas(Frame1, width=220, height=220,bg = "red")
Fires_Danger_Canvas.place(x=170,y=120)


# 해발고도 그래프를 출력하는 곳
Altitude_Canvas = Canvas(Frame1, width=590, height=386,bg = "yellow")
Altitude_Canvas.place(x=170,y=350)


# 지도를 출력하는 곳
Map_Canvas = Canvas(Frame1, width=360, height=320,bg = "blue")
Map_Canvas.place(x=400,y= 20)


'''

# Frame2 세부정보창에 대한 프레임

Frame2 = Frame(Note, width=780, height=780)
Note.add(Frame2,text = " 정보 ")

# 선택한 산의 교통시설을 보여주는 스크롤바

Scrolled_Transport = ScrolledText(Frame2,width=40,height=25)
Scrolled_Transport.place(x= 10 ,y=20)

Window.mainloop()