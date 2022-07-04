from tkinter import *
import tkinter.messagebox
import pandas as pd
import MainScripts

global companies, k
companies={}

def smc():
    root = Tk()
    root.title("Asset Information")

    canvas = Canvas(root, height=250, width=500, bg='#1ABC9C')

    def addinp():
        global companies

        inp = inputtxt.get(1.0, "end-1c")
        x = MainScripts.AI(inp)

        if x != []:
            tkinter.messagebox.showinfo("Asset Added", f'Name: {x[0]}')
            companies[x[0]]=inp

        else:
            tkinter.messagebox.showinfo("Asset Information", "Asset not found!")

    def checkinp():
        global companies
        tkinter.messagebox.showinfo("Company Information", f'{companies}')

    def clearlst():
        global companies
        companies={}
        tkinter.messagebox.showinfo("Alert!", f'Cleared!')

    def definp():
        global companies
        companies= {
        'Amazon':'AMZN',
        'Apple':'AAPL',
        'Walgreen':'WBA',
        'Northrop Grumman':'NOC',
        'Boeing':'BA',
        'Lockheed Martin':'LMT',
        'McDonalds':'MCD',
        'Intel':'INTC',
        'IBM':'IBM',
        'Texas Instruments':'TXN',
        'MasterCard':'MA',
        'Microsoft':'MSFT',
        'General Electrics':'GE',
        'American Express':'AXP',
        'Pepsi':'PEP',
        'Coca Cola':'KO',
        'Johnson & Johnson':'JNJ',
        'Toyota':'TM',
        'Honda':'HMC',
        'Exxon':'XOM',
        'Chevron':'CVX',
        'Valero Energy':'VLO',
        'Ford':'F',
        'Bank of America':'BAC'}

        tkinter.messagebox.showinfo("Company Information", f'{companies}\n Loaded!\n Use Submit to Perform Clustering')

    def subinp():
        global companies
        global k

        k=clusters.get(1.0, "end-1c")

        if int(k)>len(companies):
            tkinter.messagebox.showinfo("Cluster Error", f'Invalid number of clusters entered!')

        else:
            x=MainScripts.clustering(companies, int(k))

            if x[0]!=0:
                tkinter.messagebox.showinfo("Cluster List", f'{x[1]}')

            else:
                tkinter.messagebox.showinfo("Cluster Error", f'Internal Error Occured')

    l = Label(root, text="Asset Symbol")
    l.config(font=("Courier", 14))
    l.pack()

    inputtxt = Text(root, height=1, width=20)

    inputtxt.pack()

    # Button Creation
    Button(root, text="Add Symbol", command=addinp).pack()
    Button(root, text="Check Company List", command=checkinp).pack()
    Button(root, text="Clear List", command=clearlst).pack()
    Button(root, text="Use Default", command=definp).pack()

    l2 = Label(root, text="Number of clusters")
    l2.config(font=("Courier", 14))
    l2.pack()

    clusters = Text(root, height=1, width=20)
    clusters.pack()

    Button(root, text="Submit", command=subinp).pack()

    canvas.pack()

    root.mainloop()