from tkinter001 import *

def reply(name):
    showinfo(title='popup', message='Привет, %s!' % name)

top = Tk()
top.title('Ввод')
top.iconbitmap('favicon.ico')
Label(top,
  text='Введите своё имя',
).pack(side=TOP)

ent = Entry(top)
ent.pack(side=TOP)

Button(top,
       text='Принять приветствие',
       command=(lambda: reply(ent.get()))
).pack(side=BOTTOM)
# class InputGui(Tk):
#     def __init__(self):
#         self.title('Ввод')
#         self.iconbitmap('favicon.ico')
#         Label(self,
#           text='Введите своё имя',
#         ).pack(side=TOP)
#
#         ent = Entry(self)
#         ent.pack(side=TOP)
#
#         btn = Button(self,
#                command=(lambda: self.reply(ent.get()))
#         )
#         btn.pack(side=LEFT)
#         #
#     def reply(self, name):
#         showinfo(title='popup', message='Hello, %s!' % name)
    # def runGui(self):
    #     self.pack()
    #     self.mainloop()

if __name__ == '__main__':
    top.mainloop()