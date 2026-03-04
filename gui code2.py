import tkinter as tk

def button_click():
    print("button clicked")
    print("you entered:", entry.get())

window=tk.Tk()
window.title("New Window!")
window.geometry("400x200")

button=tk.Button(window, text="click me", bg='pink', fg='maroon', command=button_click)
label=tk.Label(window, text="Hello, Aman!", bg='pink', fg='maroon', font=("Times new roman",14))
entry= tk.Entry (window,width=30)
button.pack()
label.pack()
entry.pack()

button.config(bg='grey')
print('You typed',entry.get())
label.config(bg='sky blue')
window.mainloop()