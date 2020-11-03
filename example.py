# Import tkinter module and our module
import circularprogressbar
import tkinter as tk

# Create main window
root = tk.Tk()
root.geometry('720x360')

# Set the varriable
i = 0

# Create loadbar object
myload = circularprogressbar.CircularProgressBar(root, 360, 180, 200, 185, 0, color1="#0099CC", color2="#333366", color3="#A8A8A8")

# Increase the percent
def edit_p1():
	global i
	i += 1
	myload.change(i)
	root.after(10, edit_p1)

root.after(1000, edit_p1)

root.mainloop()
