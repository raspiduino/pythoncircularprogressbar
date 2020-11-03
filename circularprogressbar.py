# Circular progressbar for Tkinter (Python)
# Copyright @raspiduino on github
# Date created 2/11/2020

# Import tkinter

try:
    import Tkinter as tk # For Python 2
except ImportError:
    import tkinter as tk # For Python 3

class CircularProgressBar():
    '''
    Circular LoadBar class
    Usuage: myloadbar = CircularProgressBar(root, x, y, r1, r2, percent=0, color1=green, color2=white, color3=white)
    ------------------
    root: root windows
    x       : x location of the loadbar's center point
    y       : y location of the loadbar's center point
    (About 3 circles, please see the repo's note)
    r1      : radius of the first circle
    r2      : radius of the second circle
    percent : original percent of the loadbar
    color1  : color of the first circle (default is green)
    color2  : color of the second circle (default is white)
    color3  : color of the third circle (default is white)
    '''
    def __init__(self, root, x, y, r1, r2, percent=0, color1="green", color2="white", color3="white"):
        self.x = x # x location of the loadbar's center point
        self.y = y # y location of the loadbar's center point
        self.r1 = r1 # Radius of the first circle
        self.r2 = r2 # Radius of the second circle
        self.percent = percent # Load percent
        self.degree = self.percent*3.6 # Convert percent to degree
        self.color1 = color1 # Color of the first circle
        self.color2 = color2 # Color of the second circle
        self.color3 = color3 # Color of the third circle
        # Create canvas
        self.canvas = tk.Canvas(root, width=self.r1, height=self.r1)
        self.canvas.pack(fill="both", expand=True)
        self.c3 = self.canvas.create_oval((x-r1/2), (y-r1/2), (x+r1/2), (y+r1/2), fill=self.color3) # Create circle 3
        self.c1 = self.canvas.create_arc((x-r1/2), (y-r1/2), (x+r1/2), (y+r1/2), start=0, extent=self.degree, fill=self.color1) # Create circle 1
        self.c2 = self.canvas.create_oval((x-r2/2), (y-r2/2), (x+r2/2), (y+r2/2), fill=self.color2) # Create circle 2
    def change(self, newpercent):
        '''
        Change the load percent
        Usuage: myloadbar.change(yournewpercent)
        '''
        self.percent = newpercent
        self.degree = self.percent*3.6
        self.canvas.itemconfigure(self.c1, extent=self.degree)
