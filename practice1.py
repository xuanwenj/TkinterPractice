def hello():
    print("Hello World")

import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text = 'Hello World', command = hello)
button.pack()

window.mainloop()
