from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *

def print_checbox():
    if (v1.get() + v2.get()) == 2 or\
            (v1.get() + v3.get()) == 2 or\
            (v2.get() + v3.get()) == 2 or\
            (v1.get() + v2.get() + v3.get()) == 3:       
        showerror(title='ERROR', message='Только один!')
    elif v1.get() == 1  and ((v2.get() and v3.get()) == 0):
        showinfo(title='Variant 1', message='Вы выбрали первый вариант')
    elif v2.get() == 1  and ((v1.get() and v3.get()) == 0):
        showinfo(title='Variant 2', message='Вы выбрали второй вариант')
    elif v3.get() == 1  and ((v1.get() and v2.get()) == 0):
        showinfo(title='Variant 3', message='Вы выбрали третий вариант')
    else:
        showerror(title='ERROR', message='Выберите хоть что-то!')

def open_txt_file():

    try:
        txt = askopenfilename(title='ВЫБЕРИТЕ ФАЙЛ')
        with open(txt, "r") as f:
                in_file_text = f.read()
                in_file = Text(vkladka_3, width=50, height=15 , font=('Arial, 14'))
                in_file.insert(END, in_file_text)
                in_file.pack()

    except FileNotFoundError:
        showerror(title='Error', message='Файл не был выбран!')

def clicked_combobox_calc():
    try:
        if combo.get() == "+":
            result_pole.config(text=int(combo_numbers_1.get()) + int(combo_numbers_2.get()))
        elif combo.get() == "-":
            result_pole.config(text=int(combo_numbers_1.get()) - int(combo_numbers_2.get()))
        elif combo.get() == "*":
            result_pole.config(text=int(combo_numbers_1.get()) * int(combo_numbers_2.get()))
        else:
            result_pole.config(text=int(combo_numbers_1.get()) / int(combo_numbers_2.get()))
    except ZeroDivisionError:
        showerror(title='ZeroDivisionError', message='На ноль делить нельзя!')

root = Tk()
root.geometry('600x350+0+0')
root.title('Пескова Александра')
root.resizable(width=False, height=False)

nk = ttk.Notebook(root)
nk.pack(fill=BOTH, expand=True)

vkladka_1 = ttk.Frame(nk)
vkladka_2 = ttk.Frame(nk)
vkladka_3 = ttk.Frame(nk)

nk.add(vkladka_1, text='Калькулятор')
nk.add(vkladka_2, text='Кнопки')
nk.add(vkladka_3, text='Файлы')

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
checkbox_1  = Checkbutton(vkladka_2, text='1', variable=v1, onvalue=1, offvalue=0).pack()
checkbox_2  = Checkbutton(vkladka_2, text='2', variable=v2, onvalue=1, offvalue=0).pack()
checkbox_3  = Checkbutton(vkladka_2, text='3', variable=v3, onvalue=1, offvalue=0).pack()
bt_1 = Button(vkladka_2, text='Нажми на меня', command=print_checbox).pack()

btn_open_file = Button(vkladka_3, text='Upload file', command=open_txt_file).pack()

var = IntVar()
var.set(0)
var1 = IntVar()
var1.set(0)

numbers = [str(i) for i in range(10)]
combo_numbers_1 = ttk.Combobox(vkladka_1, values=numbers, textvariable=var)
combo_numbers_2 = ttk.Combobox(vkladka_1, values=numbers, textvariable=var1)
combo_numbers_1.place(x=1, y=1)
combo_numbers_2.place(x=301, y=1)

operands = ["+", "-", "*", "/"]
combo= ttk.Combobox(vkladka_1, values=operands)
combo.place(x=151, y=1)

btn = Button(vkladka_1, text="=", command=clicked_combobox_calc)
btn.place(x=447, y=1)
result_pole = ttk.Label(vkladka_1, text=" ", width=30, background='white')
result_pole.place(x=470, y=1)


root.mainloop()

