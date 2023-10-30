from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton = Button(frame, text='RED', fg='RED')
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text='Green', fg='Green')
greenbutton.pack(side=LEFT)

brownbutton = Button(frame, text='Brown', fg='Brown')
brownbutton.pack(side=RIGHT)

bluebutton = Button(frame, text='Blue', fg='Blue')
bluebutton.pack(side=RIGHT)

purplebutton = Button(frame, text='Purple', fg='Purple')
purplebutton.pack(side=RIGHT)

mainloop()