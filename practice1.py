import tkinter

def hello():
    print("Hello World")

window = tkinter.Tk()
window.title("Tkinter App")
window.geometry('600x400')
# window is the parent of the label

frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text = "Label")
label.pack()
button = tkinter.Button(frame, text = 'Hello World', command = hello)
button.pack()
print("hi")

window.mainloop()

