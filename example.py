import circularloadbar
import tkinter as tk

root = tk.Tk()
root.geometry('720x360')

myload = circularloadbar.CircularLoadBar(root, 360, 180, 200, 150)

i = 0

def edit_p1():
	global i
	i += 1
	myload.change(i)
	root.after(10, edit_p1)

root.after(1000, edit_p1)

root.mainloop()
