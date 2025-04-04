import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Ahoj světe")

root=tk.Tk()
root.title("Moje stránka")

tlacitko=tk.Button(root,text="Klikni",command=show_message)
tlacitko.pack()

root.mainloop()
