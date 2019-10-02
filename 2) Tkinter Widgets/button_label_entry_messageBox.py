import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk() # 
window.geometry("500x450")
window.title("Welcome to first app")

def buttonFunction():
    print("Push button")
    
    # label
    label.config(text = "hello world",
                 fg = "black",
                 bg = "red",
                 font = "Times 25")
    # entry
    value = entry.get()
    print(value)
    label.configure(text = value)
    entry.configure(state = "disabled")

    # message
#    message_box = messagebox.showinfo(title = "info", message = "information")
#    message_box = messagebox.askretrycancel(title = "info", message = "information")
#    message_box = messagebox.askquestion(title = "info", message = "information")
#    message_box = messagebox.askyesnocancel(title = "info", message = "information")
    message_box = messagebox.showerror(title = "info", message = "information")
    print(message_box)
    
# button
button = tk.Button(window, text = "First button", activebackground = "red",
                   bg = "black", fg = "white", activeforeground = "black",
                   height = 15, width = 50,
                   command = buttonFunction)

button.pack()

#label
label = tk.Label(window, text = "Hi World", font = "Times 16", fg = "white", bg = "black",
                 wraplength = 150)

label.pack(side = tk.RIGHT, padx = 25)

# entry

entry = tk.Entry(window, width = 50)
entry.insert(string = "write something only one time",index = 0)
entry.pack(side = tk.LEFT, padx = 25)





















window.mainloop()