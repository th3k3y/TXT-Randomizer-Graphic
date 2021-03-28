#Importing required modules.

from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import random

#Defining the main fonction.

def process():
	filename = filedialog.askopenfilename(initialdir="/", title="Select Your File", filetypes=[("TEXT FILES", ".txt")])
	lines = open(filename).readlines()
	random.shuffle(lines)
	open(filename, 'w').writelines(lines)
	messagebox.showinfo("Success.", "Your file has been successfully shuffled !")

#Creating the window.

window = Tk()
window.title("TEXT RANDOMIZER")
window.geometry("150x150")
window.config(bg = "#23272a")
window.iconbitmap("assets/icon.ico")
window.resizable(width=False, height=False)

#Creating the button.

randomize_btn = PhotoImage(file='assets/btn.png')
btn = Button(image=randomize_btn, bg="#23272a", activebackground="#23272a", borderwidth=0, padx=50, pady=50, cursor="hand2", width=120, command=process)
btn.pack(pady=20)

window.mainloop()
