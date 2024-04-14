from tkinter import Tk, Entry, Button, StringVar

class calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg ='gray')
        master.resiable(False,False)
        
        self.equation = StringVar
        self.entry_value = ''
        Entry(width=17, bg = '#fff', font=('Arial Bold', 28))



root = Tk()
root.mainloop()