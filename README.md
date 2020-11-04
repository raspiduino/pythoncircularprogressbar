# Python circular progressbar
Tkinter circular progressbar for Python 2 &amp; 3
## Usage
![alt](https://raw.githubusercontent.com/raspiduino/pythoncircularprogressbar/main/config.png)
```python
myloadbar = CircularLoadBar(root, x, y, r1, r2, percent=0, color1=green, color2=white, color3=white
```
|Argument|Info|
|--------|----|
|root|The root windows id (you have created using root = tkinter.Tk())|
|x|The x location of the progressbar's center|
|y|The y location of the progressbar's center|
|r1|Described in the picture (radius of the first circle)|
|r2|Described in the picture (radius of the second circle)|
|percent|The startup percent (default is 0%)|
|color1|Color of the first circle (default is green)|
|color2|Color of the second circle (default is white)|
|color3|Color of the third circle (default is white)|

<p>Example: (example.py)</p><br>

```python
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
```

## Why made this?
<p>For a simple reason: There is no 'default' circular progress bar in Python Tkinter, so I wanted to make this.</p>

## License
<p>Under <a href="https://github.com/raspiduino/pythoncircularprogressbar/blob/main/LICENSE">GNU LGPL-v2.1</a></p>
