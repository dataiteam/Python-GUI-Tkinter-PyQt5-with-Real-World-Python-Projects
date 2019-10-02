import tkinter as tk
from tkinter import ttk 

window = tk.Tk()# top level window
window.geometry("500x450") # window size x*y

def buttonFunction():
    print("here")
    # radio button
    m = method.get()
    if m =="1":
        print("method1")
    elif m =="2":
        print("method2")
    else:
        print("method1 & method2")
    
    # combobox
    print(problem.get())
    
    # checkButton
    value = save_var.get()
    if value == 1:
        print("Save__")
    else:
        print("not save")
        
button = tk.Button(window, text = "button", activebackground = "red", bg = "black",
                    fg = "white", activeforeground = "black",
                    height = 15, width = 50, command = buttonFunction)

button.grid(row = 0, column = 0, pady = 15)

# radio button
method = tk.StringVar()
tk.Radiobutton(window, text = "method1: ", value = "1", activebackground = "red",
               bg = "green",height = 5, width = 5,borderwidth = 15,variable = method).grid(row=1,column=0)

tk.Radiobutton(window, text = "method2: ", value = "2", variable = method).grid(row=1,column=1, pady=15)

# comboBox
problem = tk.StringVar()
comboBox = ttk.Combobox(window, textvariable = problem, values = ("1","2","3"), state= "readonly")
comboBox.grid(row=2,column=0, pady=15)

def checkButtonFunction():
    print("save")

# checkButton
save_var = tk.IntVar()
save_var.set(0)
c_button = tk.Checkbutton(window, text = "Save", variable = save_var, font = "Times 25", activebackground = "green",
                          activeforeground = "white",
                          bg = "yellow", command = checkButtonFunction)
c_button.grid(row=2,column=1, pady=15)


















window.mainloop()