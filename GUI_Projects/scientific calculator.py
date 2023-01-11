"""
This is a Scientific Calculator created with the Tkinter Module

Aside the Tkinter Module; we used the math module and a manually created library; scientific_calc_library_trig_degrees
"""
# First we import our Modules

# This is the Tkinter Module; responsible for our Graphic User Interface (GUI)
from tkinter import *

# This library contains different functions.
# These functions hold some Trigonometry functions...we will explain what this library does at the end of this Code.
from scientific_calc_library_trig_degrees import *

# This is a Math module that is used for several Mathematical operations including Trig functions, and many others.
from math import *

# Here, we initialize the Tk() object.
# This is responsible for the display of our GUI
root = Tk()

# You may want to skip this block of code and come back to it when you're done with the rest...

# This compute function runs whenever we click on the Solve button.


def compute():
	# We use the try and except just In case the user inputs a wrong operation.
	try:
		# The first thing to get the user's input; qf.get()
		# Then evaluate this input eval(user_input)
		answer = eval(qf.get())
		# to make the answer we got show in the answer field; we need to reconfigure the text.
		af.configure(text=f"Ans: {answer}")
	except:
		# In case the user inputs a wrong expression...we want this to display.
		af.configure(text="Invalid input")

# Creating our Fields...

# af(answer field) is the Field that displays our answer
# Our fields like Label, Button... takes in several parameters
# the most important is the "root", not necessarily "root"
# it should be whatever we initialized Tk() as.
# Taking root as the Parameters means, we want the Label to be inside the root Frame.


af = Label(root, text="Ans: ")
# .pack() is what makes the field appear on the screen; we have others like .grid()...
af.pack()

# qf(question field) is an Input Field where we input our Expressions.
qf = Entry(root)
qf.pack()

# This is a button; onclick helps us compute the expression and displays the result in the answer Field.

# command = compute; this means, run the compute function once the button is clicked.
solve = Button(root, text="Solve", command=compute)
solve.pack()

# Remember we initialized root as our Tkinter Object from the start.
# Doing this only makes us run the Code once, like...the User Interface closes just immediately after it's opened.
# The only way to make this UI keep running is if it's in a loop, "a keep running" loop.
# and that why the .mainloop() does, it makes the UI keep running.
root.mainloop()

"""
trig functions in Python returns its values in Radians...with the scientific_calc_library_trig_degrees we created;
we've converted the values to Degrees.

Meaning, Cos(x) will take x as a number in degrees
while cos(x) will take x as a number in radian...this is using the ordinary math module.

Check the scientific_calc_library_trig_degrees.py in this same directory for the code.
"""
