from tkinter import *
 scrollbar = Scrollbar(layout)
scrollbar.pack(side=RIGHT, fill=Y)
myList = Listbox(layout, yscrollcommand=scrollbar.set)
for line in range(300):
    myList.insert(END, 'List Data Ke'+ str(line))
myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview)
mainloop()