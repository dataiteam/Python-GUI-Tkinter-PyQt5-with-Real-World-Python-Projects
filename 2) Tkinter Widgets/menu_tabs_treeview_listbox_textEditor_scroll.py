import tkinter as tk
from tkinter import ttk  

window = tk.Tk()
window.geometry("800x600")


# menu 
def fileFunction():
    print("here")

menubar = tk.Menu(window)
window.config(menu = menubar)

file = tk.Menu(menubar)
edit = tk.Menu(menubar)

menubar.add_cascade(label = "file", menu = file)
menubar.add_cascade(label = "edit", menu = edit)

file.add_command(label = "new file", command =fileFunction )
edit.add_command(label = "undo", command =fileFunction )


# tabs
tabs = ttk.Notebook(window, width = 540, height = 300)
tabs.place(x = 25, y = 25)

tab1 = ttk.Frame(tabs, width = 50, height = 50)
tab2 = ttk.Frame(tabs, width = 50, height = 50)
tab3 = ttk.Frame(tabs, width = 50, height = 50)

tk.Label(tab1, text = "tab1").pack()
tk.Label(tab2, text = "tab2").pack()
#tk.Label(tab3, text = "tab3").grid()

tabs.add(tab1, text = "treeview")
tabs.add(tab2, text = "list box")
tabs.add(tab3, text = "text editor")

# tree view
treeview = ttk.Treeview(tab1)
treeview.place(x = 5, y = 5)

treeview.insert("","0","item1", text = "Spain")
treeview.insert("item1","1","item2", text = "Madrid")
treeview.insert("","2","item3", text = "France")
treeview.insert("item3","3","item4", text = "Paris")

def callback(event):
    item = treeview.identify("item",event.x,event.y)
    print(item)
    
treeview.bind("<Double-1>",callback)

# listbox
listBox = tk.Listbox(tab2, selectmode = tk.MULTIPLE)
listBox.insert(0,"Spain")
listBox.insert(1,"France")
listBox.insert(2,"China")

listBox.place(x = 5, y = 5)

def getItem():
    index_list = listBox.curselection()
    print(index_list)
    for each in index_list:
        print(listBox.get(each))

button = tk.Button(tab2, text = "button", command = getItem)
button.place(x = 150, y = 5)

# text editor
textEditor = tk.Text(tab3, width = 25, height = 25, wrap = tk.WORD)
textEditor.grid(row = 0, column = 0, padx = 10, pady = 10)

def textFunction():
    print(textEditor.get(1.0, tk.END))
    
button = tk.Button(tab3, text = "save", command = textFunction)
button.grid(row = 0, column = 2, padx = 10, pady = 10)


# scroll
scroll = tk.Scrollbar(tab3, orient = tk.VERTICAL, command = textEditor.yview)
scroll.grid(row = 0, column = 1, sticky = tk.N + tk.S)
textEditor.config(yscrollcomman = scroll.set)


window.mainloop()













