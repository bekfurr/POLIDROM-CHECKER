from tkinter import *

def polidrom():
    soz = entry1.get()
    n = len(soz)
    b = ""
    for i in range(n-1, -1, -1):
        b += soz[i]
    if soz == b:
        label2 = Label(win, text="Soz polidrom", foreground="White", background="Green"  )
        label2.grid(row=2, column=0, columnspan=2)
    elif soz == "":
        label2 = Label(win, text="MAYDON BO^SH", foreground="White", background="Red"  )
        label2.grid(row=2, column=0, columnspan=2)
    
    else:
        label2 = Label(win, text="Soz polidrom emas", foreground="White", background="Red"  )
        label2.grid(row=2, column=0, columnspan=2)
        
win = Tk()

win.title("Polidrom Tekshirish")

label1 = Label(win, text="So'zni kiriting:")

label1.grid(row=0, column=0)

entry1 = Entry(win)

entry1.grid(row=0, column=1)

qiymat = Text(win, height=5, width=30)



tugma = Button(win, text="Tekshirish", command=polidrom)
tugma.grid(row=1, column=0, columnspan=2)

win.mainloop()
    






