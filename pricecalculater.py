import tkinter

def computePrice():
    totalprice = int(priceperitem_entry.get()) * int (numberofitems_entry.get())
    totalprice_entry.insert(0, string=str(totalprice))
    # 0 means insert at the very start of the entry
window = tkinter.Tk()
window.geometry('600x400')
priceperitem_label = tkinter.Label(window, text = "Price per item")
priceperitem_entry = tkinter.Entry(window)
numberofitems_label = tkinter.Label(window, text = "Number of items")
numberofitems_entry = tkinter.Entry(window)
totalprice_label = tkinter.Label(window, text = "Total price:")
totalprice_entry = tkinter.Entry(window)
calculate_button = tkinter.Button(window, text="Calculate total", command=computePrice)

# numberofitems_label.pack()
# numberofitems_entry.pack()
# totalprice_label.pack()
# totalprice_entry.pack()
# pack() layout
# totalprice_label.pack(side="left")
# totalprice_entry.pack(side="right")
# calculate_button.pack(fill="x") # fill the button the width of the window


# place() layout, using absolute positioning, least popular
# priceperitem_label.place(x=0, y=0)
# priceperitem_entry.place(x=0, y=50)

# widgets = [priceperitem_label, priceperitem_entry, numberofitems_entry,
#            totalprice_label, totalprice_entry, calculate_button]

# for i in range(len(widgets)):
#     widgets[i].place(x=0, y=i*30)

#  grid layout
priceperitem_label.grid(row=0, column=0)
priceperitem_entry.grid(row=0, column=1)
numberofitems_label.grid(row=1, column=0)
numberofitems_entry.grid(row=1, column=1)
totalprice_label.grid(row=2, column=0)
totalprice_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)

window.mainloop()