from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(labe='About')

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Tool Window')
viewmenu.add_command(label='Appearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Definition')
viewmenu.add_command(label='Quick Type Definition')
viewmenu.add_command(label='Parameter')
viewmenu.add_command(label='Type Info')
viewmenu.add_command(label='Context Info')
mainloop()
