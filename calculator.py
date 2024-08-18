import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create and position the entry field
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create and position the number buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda x=button: button_click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create and position the clear button
tk.Button(window, text="Clear", padx=20, pady=20, command=clear).grid(row=row, column=col, columnspan=2)

# Start the GUI event loop
window.mainloop()