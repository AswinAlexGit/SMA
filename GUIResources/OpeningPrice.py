from tkinter import *
import tkinter.messagebox
import MainScripts

def op():
    root = Tk()
    root.title("Asset Information")

    canvas= Canvas(root, height= 250, width=500, bg='#1ABC9C')

    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        x=MainScripts.AI(inp)

        if x!=[]:
            tkinter.messagebox.showinfo("Asset Information", f'Name: {x[0]} \nMarket Price: {x[1]} \nPrevious Close Price: {x[2]}')
        else:
            tkinter.messagebox.showinfo("Asset Information","Asset not found!")

    l = Label(root, text="Asset Symbol")
    l.config(font=("Courier", 14))
    l.pack()

    inputtxt = Text(root, height=1, width=20)

    inputtxt.pack()

    # Button Creation
    Button(root,text="Submit",command=printInput).pack()
    canvas.pack()

    root.mainloop()