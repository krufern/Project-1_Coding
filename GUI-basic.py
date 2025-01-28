from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')
GUI.title('Pre-ENG App')

L = Label(GUI, text = 'กรอกข้อมูล', font=('Angsana New',25))
L.pack()

L = Label(GUI, text = 'คุณสมบัติ\n\n- อายุระหว่าง 20 - 25 ปี\n- วุฒิปริญญาตรี', font=('Angsana New',20))
L.pack()

E1 = ttk.Entry(GUI,font=('Angsana New', 20))
E1.pack()


GUI.mainloop()