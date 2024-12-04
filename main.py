from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("400x400")
def msg_box():
    messagebox.showwarning("Alert","Virus detected!")
button=Button(master=window,command=msg_box,text="Scan_for_virus",width=20)
button.place(x=50,y=50)
window.mainloop()