from tkinter import *
from tkinter.ttk import *

Window = Tk()
Window.title("등산가는길")
Window.geometry("800x800")

# Frame1 검색창에 대한 프레임

Note = Notebook(Window)
Note.place(x=10, y=10, width=780, height=780)

Frame1 = Frame(Note, width=780, height=780)
Note.add(Frame1,text = " 검색 ")

Txt1 = Entry(Frame1,width= 40)
Txt1.place(x=10,y=20)

Txt2 = Entry(Frame1,width= 40)
Txt2.place(x=10,y=60)


# Frame2 세부정보창에 대한 프레임

#Frame2 = Frame(Window)
#Frame2.pack()

#Note = Notebook(Window)
#Note.place(x=60,y=0)



#Note2.add(Frame2,text=" 정보 ")

Window.mainloop()