from tkinter import *

def label():
    label1 = Label(window , text = "BUTTON PRESSED" , font = "Times 20 bold" , fg = "black").grid(row = 1 , column =0 , padx = 10 , pady = 10)

def label2():
    xyz = Label(window , text = "WELCOME TO PYTROOPS" , font = "Times 20 bold" , fg = "black").grid(row = 2 , column =0)

window = Tk()
window.title('PYTROOPS')
window.geometry("600x600")
window.configure(background = "yellow")
pic = PhotoImage(file = "play2.png")

#btn1 = Button(window , text = "PRESS" , command = label , height = 2 , width = 10 , bg = "black" , fg = 'white'
              #,font = "Times 20 bold" , borderwidth = 20).grid(row = 0  , column = 0 ,   padx = 80 , pady = 80)
btn2 = Button(window , image = pic ,font= 20, command = label2,height=53, width=60,fg = "black").grid(row =0 , column = 0, padx =50, pady =90)

window.mainloop()