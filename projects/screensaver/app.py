#-------------------------------------------------------------------------------
# Name:        ScreenSaver
#
# Author:      Enidev911
#-------------------------------------------------------------------------------

import tkinter as tk
from random import randint

class RandomBall:
    def __init__(self, canvas, scr_w, scr_h):
        self.canvas = canvas
        self.scr_w = scr_w
        self.scr_h = scr_h

        self.xpos = randint(70, int(self.scr_w - 70))
        self.ypos = randint(70, int(self.scr_h - 70))

        self.dx = randint(6, 12)
        self.dy = randint(6, 12)

        self.radius = randint(40, 70)

        self.color = f"#{randint(0,255):0>2x}{randint(0,255):0>2x}{randint(0,255):0>2x}"
        # Convert hex with 2 char and fill with zero

    def create_ball(self):
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        self.xpos += self.dx
        self.ypos += self.dy

        if self.xpos > self.scr_w - self.radius or self.xpos <= self.radius:
            self.dx = -self.dx

        if self.ypos > self.scr_h - self.radius or self.ypos <= self.radius:
            self.dy = -self.dy

        self.canvas.move(self.item, self.dx, self.dy)

class ScreenSaver:

    def __init__(self, master, num_balls):
        self.master = master
        self.master.overrideredirect(1)
        self.master.attributes('-alpha', 0.6)
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.balls = []

        self.master.geometry(f"{w}x{h}+0+0")
        self.master.bind("<Any-KeyPress>", self.quit)
        self.master.bind("<Any-Button>", self.quit)
        self.master.bind("<Motion>", self.quit)

        self.canvas = tk.Canvas(self.master, width=w, height=h, bg='#222334')
        self.canvas.pack()

        for i in range(num_balls):
            ball = RandomBall(self.canvas, scr_w=w, scr_h=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()

    def run_screen_saver(self):

        for ball in self.balls:
            ball.move_ball()

        self.master.after(20, self.run_screen_saver)


    def quit(self, event):
        self.master.destroy()

if __name__ == '__main__':
    w = tk.Tk()
    ScreenSaver(w, 18)
    w.mainloop()