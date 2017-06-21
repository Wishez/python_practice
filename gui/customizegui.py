from tkinter001 import *

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Polymorphism was made.')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()