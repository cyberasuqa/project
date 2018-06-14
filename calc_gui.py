from tkinter import *
def plus():
    x = window_1.get()
    y = window_2.get()
    if not x.isdigit() and not y.isdigit():
        result['text'] = 'ошибка'
    result['text'] = int(x) + int(y)
def minus():
    x = window_1.get()
    y = window_2.get()
    if not x.isdigit() and not y.isdigit():
        result['text'] = 'ошибка'
    result['text'] = int(x) - int(y)
def multi():
    x = window_1.get()
    y = window_2.get()
    if not x.isdigit() and not y.isdigit():
        result['text'] = 'ошибка'
    result['text'] = int(x) * int(y)
def div():
    x = window_1.get()
    y = window_2.get()
    if x.isdigit() and y.isdigit():
        result['text'] = 'ошибка'
    if y == 0:
        result['text'] = 'ошибка'
    else:
        result['text'] = int(x) / int(y)
root = Tk()
window_1 = Entry(root,width = 10)
window_2 = Entry(root,width = 10)
result = Label(root, bg = 'grey',fg = 'white',width = 20)
b_plus = Button(root,text = '+',command = plus)
b_minus = Button(root,text = '-',command = minus)
b_multi = Button(root, text = '*',command = multi)
b_div = Button(root, text = '/',command = div)
window_1.pack(side = 'left' )
window_2.pack(side = 'left')
result.pack()
b_plus.pack(side = 'left')
b_minus.pack(side = 'left')
b_multi.pack(side = 'left')
b_div.pack(side = 'left')
root.mainloop()