import json

from requests import * 
from tkinter import *
from tkinter.messagebox import *

def pars():
    data = {}
    nickname = input_nick.get()           #GET из tkinter
    nickname = "https://api.github.com/users/" + nickname
    nk = get(nickname)
    res = nk.json()
    company, created_at, email = res['company'], res['created_at'], res['email']
    id, name, url = res['id'], res['name'], res['url']
    
    data['company'], data['created_at'], data['email'] = company, created_at, email
    data['id'], data['name'], data['url'] = id, name, url
    
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)    

    showinfo(message='Success')

root = Tk()
root.title('Пескова')
root.geometry('333x333+0+0')
root.resizable(0, 0)

input_nick = StringVar()

text_pole = Entry(width=30, insertbackground='red', textvariable=input_nick)
text_pole.pack(anchor=N)
btn = Button(width=8, height=4, text='Get json', bg='red', command=pars)
btn.pack(anchor=N)

root.mainloop()
