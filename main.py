import requests
from bs4 import BeautifulSoup
import math
from tkinter import *


def find(texts: str, letter: str) -> int:
    count = texts.count(letter, 0, len(texts))
    return count


def ix(p, result):
    result += -(1 * p * math.log2(p))
    return result


window = Tk()

window.geometry("600x600")
window.title("Lab1")
label1 = Label(window, text="Подсчёт количества информации в тексте", font=('Tahoma', 19, 'bold'))
label1.place(x=10, y=15)
label2 = Label(window, text="Введите URL сайта: ", font=('Tahoma', 16, 'bold'))
label2.place(x=20, y=75)
url_r = Entry(window, font=('Tahoma', 12, 'bold'))
url_r.place(x=270, y=80, width=300)
text_in = Text(window, bg='grey', font=('Tahoma', 9))
text_in.place(x=10, y=140, height=400, width=280)
text_out = Text(window, bg='grey', font=('Tahoma', 9))
text_out.place(x=310, y=140, height=400, width=280)


def click():
    str_var = ""
    url = url_r.get()
    if url == "":
        text_out.delete(1.0, END)
        text_out.insert(1.0, "Ошибка: URL не введён")
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="lxml")
        quotes = soup.find_all('p', class_='book')
        for quote in quotes:
            str_var += quote.text
        text_in.insert(1.0, str_var)
        a = text_in.get("1.0", END)
        result = 0
        rest = 0
        v = {}
        dict = []
        t_out = ""
        text_out.delete(1.0, END)
        for let in a:
            if dict.count(let) < 1:
                if let != "\n":
                    dict.append(let)
        for fin in range(len(dict)):
            temp = find(a, dict[fin])
            v.update({dict[fin]: temp})
            rest += ix(temp / len(a), result)
        v_sort = list(v.items())
        v_sort.sort(key=lambda i: i[1])
        for i in v_sort:
            t_out += i[0] + "\t|\t" + str(i[1]) + "\n"
        t_out += "Количество информации " + "{:.3f}".format(rest) + " бит"
        text_out.insert(1.0, t_out)


button_calc = Button(window, text=" Посчитать количество информации", font=('Tahoma', 12), fg="green", bd=0,
                     command=click)
button_calc.place(x=150, y=550, width=300)
window.mainloop()
