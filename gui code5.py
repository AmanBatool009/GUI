import tkinter as tk
window=tk.Tk()
window.title("Button")
window.geometry("200x200")
def change_color():
    background_color=button.cget('bg')
    if background_color=='blue':
        button.config(bg='pink')
    else:
        button.config(bg='blue')
button=tk.Button(window,text="Click me!", command=change_color)
button.pack()

window.mainloop()