#Define a new function to open the window
def open_win():
    new=Toplevel(win)
    new.geometry("750x250")
    new.title("New Window")
    #create a label in new window
    Label(new, text="Corn Hybrid A: ", font=('Helvetica 17 bold')).pack (pady=30)
    Label(new, text="Corn Hybrid B: ", font=('Helvetica 17 bold')).pack(pady=30)

    #Define a new function to open the window
def open_win2():
    new2=Toplevel(win)
    new2.geometry("750x250")
    new2.title("New Window")
    #create a label in new window
    Label(new2, text="Soybean Hybrid A:", font=('Helvetica 17 bold')).pack (pady=30)
    Label(new2, text="Soybean Hybrid B:", font=('Helvetica 17 bold')).pack(pady=30)

#Primary (initial window)
#Import tkinter library
from tkinter import *
from tkinter import ttk

#create an instance of tkinter frame or window
win=Tk()
#set geomerty of tkinter frame
win.geometry("750x250")
win.title("Buy Seeds")
#crete a label in new window
Label(win, text="Select Either Corn or Bean seed type to get started:",
      font=("helvetica 17 bold")).pack(pady=30)



#Create a button to open a new window
ttk.Button(win, text="Corn", command=open_win).pack()
ttk.Button(win, text="Beans", command=open_win2).pack()
exit_button =Button(win, text="Exit", command=win.destroy).pack()

win.mainloop()

