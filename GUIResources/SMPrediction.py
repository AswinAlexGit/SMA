from tkinter import *
import tkinter.messagebox
import MainScripts

def smp():
    root = Tk()
    root.title("Asset Information")

    canvas = Canvas(root, height=250, width=500, bg='#1ABC9C')

    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        x = MainScripts.AI(inp)
        epoch = itr.get(1.0, "end-1c")

        if x != []:
            y=MainScripts.stockpre(inp, int(epoch))
            tkinter.messagebox.showinfo("Prediction", f'{x[0]}, {y}')

        else:
            tkinter.messagebox.showinfo("Asset Information", "Asset not found!")

    l = Label(root, text="Asset Symbol")
    l.config(font=("Courier", 14))
    l.pack()

    inputtxt = Text(root, height=1, width=20)

    inputtxt.pack()

    l2 = Label(root, text="Number of Epochs")
    l2.config(font=("Courier", 14))
    l2.pack()

    itr = Text(root, height=1, width=20)

    itr.pack()

    # Button Creation
    Button(root, text="Submit", command=printInput).pack()

    canvas.pack()

    root.mainloop()