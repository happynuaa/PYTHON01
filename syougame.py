from tkinter import Tk, Canvas
from time import sleep


winXsz = 800
winYsz = 600

fightYsz = 50
fighterXsize = 50
fightHeadXsz = 40
spaceYsize = 20
x = winXsz/2
y = winYsz-fightYsz
t = 0


def right(event):
    global x
    if x < winXsz - fighterXsize / 2:
        c.move(ship, 10, 0)
        x += 10


def left(event):
    global x
    if x > fighterXsize / 2:
        c.move(ship, -10, 0)
        x += -10


def up(event):
    global y
    if y > 200:
        c.move(ship, 0, -10)
        y += -10


def down(event):
    global y
    if y < winYsz:
        c.move(ship, 0, 10)
        y += 10


def beem(event):
    global x
    global y
    global t
    if t == 0:
        t = 1
        lezer = c.create_rectangle(
            x - 2, y-25, x + 2, y, fill='red')
        for _ in range(200):
            c.move(lezer, 0, -3)
            window.update()
            t = 1
            sleep(0.01)
        c.delete(lezer)
    t = 0


window = Tk()
window.title('シューティングゲーム')


c = Canvas(window, height=winYsz, width=winXsz, bg='blue')
c.pack()
# while True:

ship = c.create_polygon(
    winXsz/2, winYsz-fightYsz-spaceYsize,
    (winXsz-fighterXsize)/2, winYsz - fightYsz + fightHeadXsz - spaceYsize,
    winXsz/2, winYsz-spaceYsize,
    (winXsz+fighterXsize)/2, winYsz - fightYsz + fightHeadXsz - spaceYsize,
    fill='yellow')
# while True:
c.bind_all('<KeyPress-d>', right)
c.bind_all('<KeyPress-a>', left)
c.bind_all('<KeyPress-w>', up)
c.bind_all('<KeyPress-s>', down)

c.bind_all('<KeyPress-Right>', right)
c.bind_all('<KeyPress-Left>', left)
c.bind_all('<KeyPress-Up>', up)
c.bind_all('<KeyPress-Down>', down)
c.bind_all('<KeyPress-space>', beem)
