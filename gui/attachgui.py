from tkinter001 import *


mainwin = Tk()
Label(mainwin, text=__name__).pack()
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
