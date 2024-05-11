import tkinter as tk
import time
import math

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    hour, minute, second = current_time.split(':')

    # Calculate the angles for hour, minute, and second hands
    hour_angle = (int(hour) % 12) * 30 + int(minute) * 0.5
    minute_angle = int(minute) * 6
    second_angle = int(second) * 6

    # Update the clock hands
    canvas.delete('all')
    draw_clock_face()
    draw_clock_hand(hour_angle, 80, 6)
    draw_clock_hand(minute_angle, 120, 4)
    draw_clock_hand(second_angle, 140, 2)

    root.after(1000, update_clock)

def draw_clock_face():
    canvas.create_oval(50, 50, 250, 250, width=2)

def draw_clock_hand(angle, length, width):
    x = 150 + length * math.sin(math.radians(angle))
    y = 150 - length * math.cos(math.radians(angle))
    canvas.create_line(150, 150, x, y, width=width)

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

update_clock()

root.mainloop()