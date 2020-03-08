from tkinter import Tk, Canvas
from time import sleep


wx = 1260
wy = 720

ty = 4
tx = 30
fy = 50
fx = 50
fh = 40
spx = 20
x = spx
x2 = wx-spx
y = wy/2
y2 = wy/2
t = 0
t2 = 0


def right(event):
    global x
    if x < wx/2 - fx:
        c.move(ship, 10, 0)
        x += 10


def right2(event):
    global x2
    if x2 < wx - fx / 2:
        c.move(ship2, 10, 0)
        x2 += 10


def left(event):
    global x
    if x > fx / 2:
        c.move(ship, -10, 0)
        x += -10


def left2(event):
    global x2
    if x2 > wx / 2 + fx:
        c.move(ship2, -10, 0)
        x2 += -10


def up(event):
    global y
    if y > fy/2:
        c.move(ship, 0, -10)
        y += -10


def up2(event):
    global y2
    if y2 > fy/2:
        c.move(ship2, 0, -10)
        y2 += -10


def down(event):
    global y
    if y < wy-fy/2:
        c.move(ship, 0, 10)
        y += 10


def down2(event):
    global y2
    if y2 < wy-fy/2:
        c.move(ship2, 0, 10)
        y2 += 10


def beem(event):
    global x
    global y
    global t
    if t == 0:
        t = 1
        lezer = c.create_rectangle(
            spx+fx, wy/2-ty/2, spx+fx+tx, wy/2+ty/2, fill='red')
        for _ in range(200):
            c.move(lezer, 6, 0)
            window.update()
            t = 1
            sleep(0.01)
        c.delete(lezer)
    t = 0


def beem2(event):
    global x2
    global y2
    global t2
    if t2 == 0:
        t2 = 1
        lezer2 = c.create_rectangle(
            wx-spx-fx, wy/2-ty/2, wx-spx-fx-tx, wy/2+ty/2, fill='red')
        for _ in range(200):
            c.move(lezer2, -6, 0)
            window.update()
            t2 = 1
            sleep(0.01)
        c.delete(lezer2)
    t2 = 0


window = Tk()
window.title('シューティングゲーム')


c = Canvas(window, height=wy, width=wx, bg='blue')
c.pack()
# while True:

ship = c.create_polygon(
    spx+fx, wy/2,
    spx+fx-fh, wy/2-fy/2,
    spx, wy/2,
    spx+fx-fh, wy/2+fy/2,
    fill='yellow')

ship2 = c.create_polygon(
    wx-fx-spx, wy/2,
    wx-fx-spx+fh, wy/2+fy/2,
    wx-spx, wy/2,
    wx-fx-spx+fh, wy/2-fy/2,
    fill='green')

# while True:
c.bind_all('<KeyPress-d>', right)
c.bind_all('<KeyPress-a>', left)
c.bind_all('<KeyPress-w>', up)
c.bind_all('<KeyPress-s>', down)
c.bind_all('<KeyPress-space>', beem)
c.bind_all('<KeyPress-Right>', right2)
c.bind_all('<KeyPress-Left>', left2)
c.bind_all('<KeyPress-Up>', up2)
c.bind_all('<KeyPress-Down>', down2)
c.bind_all('<KeyPress-j>', beem2)
