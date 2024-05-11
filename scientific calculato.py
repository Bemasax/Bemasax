
import tkinter as tk
from math import *

def evaluate_expression():
    try:
        result = eval(expression.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def clear_expression():
    expression.set("")

# Create the main window
window = tk.Tk()
window.title("Bema Scientific Calculator")

# Create the expression entry field
expression = tk.StringVar()
expression_entry = tk.Entry(window, textvariable=expression)
expression_entry.pack()

# Create the buttons
button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "sin", "cos", "tan", "sqrt",
    "log", "exp", "pi", "clear"
]

for i, button_text in enumerate(buttons):
    button = tk.Button(button_frame, text=button_text, width=5)
    button.grid(row=i // 4, column=i % 4)
    if button_text == "=":
        button.config(command=evaluate_expression)
    elif button_text == "clear":
        button.config(command=clear_expression)
    else:
        button.config(command=lambda text=button_text: expression.set(expression.get() + text))

# Create the result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the main loop
window.mainloop()
