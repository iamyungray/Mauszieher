import tkinter as tk
import pyautogui


class MouseDrag:
    def __init__(self, master):
        self.master = master
        master.title("Mauszieher")

        self.speed = 1

        self.slider = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL, label="Geschwindigkeit:",
                               command=self.set_speed)
        self.slider.pack()

        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.canvas.bind("<Button-1>", self.start_drag)

    def start_drag(self, event):
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)
        self.drag_start = event.y

        pyautogui.mouseDown(button='left')

    def drag(self, event):
        distance = (event.y - self.drag_start) * self.speed
        pyautogui.move(0, distance, duration=0.25)
        self.drag_start = event.y

    def stop_drag(self, event):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        pyautogui.mouseUp(button='left')

    def set_speed(self, value):
        self.speed = int(value)


root = tk.Tk()
mouse_drag = MouseDrag(root)
root.mainloop()
