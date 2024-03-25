import tkinter



window = tkinter.Tk()
def hello():
    print(textentry.get())    

window.title("Tkinter App")
window.geometry('600x400')
# window is the parent of the label

frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text = "Label", bg = "purple", fg = "white", width = 50)
label.pack()
textentry = tkinter.Entry(window, bg = "light green", width = 50, show="*")
textentry.pack()

button = tkinter.Button(frame, text = 'Hello World', bg = "#fdbce1", activebackground= "red", command = hello)
button.pack()
print("hi")


window.mainloop()

