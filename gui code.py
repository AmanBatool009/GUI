print ('Hello World!')
import tkinter as tk

window=tk.Tk()

window.title("My first GUI app!")
window.geometry("400x200")

label=tk.Label(window, text="Hello, Tkinter!", bg='blue', font=("Arial",12))
label2=tk.Label(window, text="Hello Muqadas!", fg='Maroon', font=("Times new roman", 16))
label3=tk.Label(window, text="Hello Mamduha!", bg='red', font=("Arial", 14))
label4=tk.Label(window, text="Hello Mehar!", fg='purple', font=("Times new roman", 10))
label5=tk.Label(window, text="Hello Musabbiha!", bg='pink', font=("Calibri", 11))
label.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
window.mainloop()
