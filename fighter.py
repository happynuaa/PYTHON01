from tkinter import Tk, Canvas
from time import sleep
from threading import (Event, Thread)

WX = 1260
WY = 720
TY = 4
TX = 20
FY = 50
FX = 50
FH = 40
SPX = 20


class Fighter():
    def __init__(self, c, ypoz, color, keyRight, keyLeft, keyUp, keyDown, keyShot):
        self.x = SPX
        self.y = WY/2+ypoz
        self.t = 0
        self.c = c
        self.ypoz = ypoz
        self.ship = self.c.create_polygon(
            SPX+FX, self.y,
            SPX+FX-FH, WY/2-FY/2+ypoz,
            SPX, self.y,
            SPX+FX-FH, WY/2+FY/2+ypoz,
            fill=color)

        self.c.bind_all(keyRight, self.right)
        self.c.bind_all(keyLeft, self.left)
        self.c.bind_all(keyUp, self.up)
        self.c.bind_all(keyDown, self.down)
        self.c.bind_all(keyShot, self.beem)

    def right(self, event):
        if self.x < WX/2 - FX:
            self.c.move(self.ship, 10, 0)
            self.x += 10

    def left(self, event):
        if self.x > FX / 2:
            self.c.move(self.ship, -10, 0)
            self.x += -10

    def up(self, event):
        if self.y > FY/2:
            self.c.move(self.ship, 0, -10)
            self.y += -10

    def down(self, event):
        if self.y < WY-FY/2:
            self.c.move(self.ship, 0, 10)
            self.y += 10

    def beem(self, event):
        if self.t <= 0:
            thread = Thread(target=self.beemth)
            thread.start()

    def beemth(self):
        self.t = 20
        lezer = c.create_rectangle(
            self.x+FX, self.y-TY/2, self.x+FX+TX, self.y+TY/2, fill='red')
        for i in range(200):
            if (i <= 20):
                self.t += -1
            c.move(lezer, 6, 0)
            window.update()
            sleep(0.01)
        c.delete(lezer)


if __name__ == "__main__":
    window = Tk()
    window.title('シューティングゲーム')
    c = Canvas(window, height=WY, width=WX, bg='blue')
    c.pack()
    f = Fighter(c, 100, 'yellow', '<KeyPress-d>',
                '<KeyPress-a>', '<KeyPress-w>', '<KeyPress-s>', '<KeyPress-space>')
    f2 = Fighter(c, 200, 'red', '<KeyPress-Right>',
                 '<KeyPress-Left>', '<KeyPress-Up>', '<KeyPress-Down>', '<KeyPress-l>')

    window.mainloop()
