from tkinter import *

layout = Tk()
layout.title("Aplikasi Kalkulator")
layout.geometry('400x200')

label = Label(layout, text="Masukan Angka Pertama : ",anchor="e")
label.grid(column=0, row=0)

nilai1 = Entry(layout, width=10)
nilai1.grid(column=1, row=0)

label2 = Label(layout, text="Masukan Angka Kedua : ", anchor="e")
label2.grid(column=0,row=1)

nilai2 = Entry(layout, width=10)
nilai2.grid(column=1,row=1)

label3 = Label(layout, text="Hasil : ", anchor="e",width=25)
label3.grid(column=0, row=2)

hasil = Label(layout, text="0", anchor="w",width=10)
hasil.grid(column=1, row=2)

def tambah():
    hasil.configure(text=int(nilai1.get())+int(nilai2.get()))

def kurang():
    hasil.configure(text=int(nilai1.get())-int(nilai2.get()))

btn = Button(layout, text="Tambah", command=tambah)
btn.grid(column=0, row=3)

btn = Button(layout, text="Kurang", command=kurang)
btn.grid(column=0, row=4)

layout.mainloop()