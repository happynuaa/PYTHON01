from random import randint
from tkinter import Tk, Button
import tkinter


def numbering(kuchi, numCount, minNum, maxNum):
    print("口数：", kuchi, " 文字数：", numCount, " 最小文字：", minNum, " 最大文字：", maxNum)
    print(numbering)

    text_widget.delete('1.0', 'end')
    for _ in range(kuchi):
        numlist = list()
        while len(numlist) < numCount:
            number = randint(minNum, maxNum)
            if not number in numlist:
                numlist.append(number)

        numlist.sort()
        print(numlist)

        text_widget.insert('1.0', '\t'.join(
            [str(num) for num in numlist]) + "\n\n")


def bAaction():
    kuchi = int(txt.get())
    print("====== ロト７のナンバーズを", kuchi, "口生成します。 ======")
    numbering(kuchi, 7, 1, 37)


def bBaction():
    kuchi = int(txt.get())
    print("====== ロト6のナンバーズを", kuchi, "口生成します。 ======")
    numbering(kuchi, 6, 1, 34)


def bCaction():
    kuchi = int(txt.get())
    print("====== ミニロトのナンバーズを", kuchi, "口生成します。 ======")
    numbering(kuchi, 5, 1, 31)


def bDaction():
    kuchi = int(txt.get())
    print("====== ナンバーズ４のナンバーズを", kuchi, "口生成します。 ======")
    numbering(kuchi, 4, 0, 9)


def bEaction():
    kuchi = int(txt.get())
    print("====== ナンバーズ３のナンバーズを", kuchi, "口生成します。 ======")
    numbering(kuchi, 3, 0, 9)


root = Tk()
root.geometry('500x380')
root.title('宝くじナンバー生成')
lbl = tkinter.Label(text='口数')
lbl.place(x=30, y=20)
txt = tkinter.Entry(width=20)

txt.place(x=90, y=20)
txt.insert(tkinter.END, "5")
btnWitdh = 10
xpoint = 30
xwidth = 85
ypoint = 50

buttonA = Button(root, text='ロト７', command=bAaction, width=btnWitdh)
buttonB = Button(root, text='ロト６', command=bBaction, width=btnWitdh)
buttonC = Button(root, text='ミニロト', command=bCaction, width=btnWitdh)
buttonD = Button(root, text='ナンバーズ４', command=bDaction, width=btnWitdh)
buttonE = Button(root, text='ナンバーズ３', command=bEaction, width=btnWitdh)
buttonA.place(x=xpoint, y=ypoint)
buttonB.place(x=xpoint+xwidth, y=ypoint)
buttonC.place(x=xpoint+xwidth*2, y=ypoint)
buttonD.place(x=xpoint+xwidth*3, y=ypoint)
buttonE.place(x=xpoint+xwidth*4, y=ypoint)
text_widget = tkinter.Text(root, height=20, width=60)
text_widget.place(x=30, y=90)
root.mainloop()
