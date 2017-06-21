from tkinter import *
from tkinter.messagebox import showerror
import shelve
from db.person import Person

shelvename = 'db/people-shelve'
fieldnames = ('name', 'age', 'job', 'salary')

class Widget():
    def __init__(self, db, fieldnames, entries={}):
        self.entries = entries
        self.db = db
        self.fieldnames = fieldnames

    def makeWidget(self):
        window = Tk()
        window.title('Обработка людей')
        form = Frame(window)
        form.pack()
        for (ix, label) in enumerate(('key',) + self.fieldnames):
            lab = Label(form, text=label)
            ent = Entry(form)
            lab.grid(row=ix, column=0)
            ent.grid(row=ix, column=1)
            self.entries[label] = ent
        Button(
            window, text='Получить',
            command=(
                lambda: fetchRecord(self.db, self.fieldnames, self.entries)
            )
        ).pack(side=LEFT)
        Button(
            window, text='Обновить',
            command=(
                lambda: updateRecord(self.db, self.fieldnames, self.entries)
            )
        ).pack(side=LEFT)
        Button(
            window, text='Выход',
            command=(lambda: window.quit())
        ).pack(side=RIGHT)
        Button(
            window, text='Очистить',
            command=(
                lambda: clearFields(self.entries)
            )
        ).pack(side=LEFT)
        Button(
            window, text='Удалить',
            command=(
                lambda: deleteRecord(self.db, self.entries)
            )
        ).pack(side=LEFT)
        return window

    def runWidget(self):
        self.makeWidget().mainloop()


def clearFields(entries):
    for ent in entries:
        entries[ent].delete(0, END)
def deleteRecord(db, entries):

    try:
        if db[entries['key'].get()]:
            key = entries['key'].get()

    except:
        showerror(title='Error', message='Такой записи не существует!')
    else:
        del db[key]

def fetchRecord(db, fieldnames, entries):
    key = entries['key'].get()
    try:
        record = db[key] # извлечь запись по ключу, отобразить в форме
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))
def updateRecord(db, fieldnames, entries):
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = Widget(db=db, fieldnames=fieldnames)
window.runWidget()
db.close()