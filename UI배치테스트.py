from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

Window = Tk()
Window.title("등산가는길")
Window.geometry("800x800")

# Frame1 검색창에 대한 프레임

Note = Notebook(Window)
Note.place(x=10, y=10, width=780, height=780)

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
Fires_Danger_Canvas = Canvas(Frame1, width=220, height=200,bg = "red")
Fires_Danger_Canvas.place(x=170,y=120)


# Frame2 세부정보창에 대한 프레임

#Frame2 = Frame(Window)
#Frame2.pack()

#Note = Notebook(Window)
#Note.place(x=60,y=0)



#Note2.add(Frame2,text=" 정보 ")

Window.mainloop()