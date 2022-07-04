from tkinter import *
import tkinter.messagebox
import MainScripts

def hd():
    root = Tk()
    root.title("Historical Data")
    canvas= Canvas(root, height= 500, width=500, bg='#1ABC9C')

    def printInput():
        aname_t = aname.get(1.0, "end-1c")
        per_t = per.get(1.0, "end-1c")
        inte_t = inte.get(1.0, "end-1c")

        x=MainScripts.AI(aname_t)

        if x!=[]:
            MainScripts.HDS(aname_t, per_t, inte_t)

        else:
            tkinter.messagebox.showinfo("Historical Data", "Asset not found!")

    l1 = Label(root, text="Asset Symbol")
    l1.config(font=("Courier", 14))
    l1.pack()

    aname = Text(root, height=1, width=10)
    aname.pack()

    l2 = Label(root, text="Period")
    l2.config(font=("Courier", 14))
    l2.pack()

    per = Text(root, height=1, width=10)
    per.pack()

    l3 = Label(root, text="Interval")
    l3.config(font=("Courier", 14))
    l3.pack()

    inte = Text(root, height=1, width=10)
    inte.pack()

    # Button Creation
    Button(root,text="Submit",command=printInput).pack()

    l4 = Label(root, text="Valid Periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y \n "
                          "Valid Intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo")
    l4.config(font=("Courier", 10))
    l4.pack()

    canvas.pack()

    root.mainloop()