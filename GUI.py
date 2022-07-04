import tkinter.messagebox

import GUIResources
#import Login
from tkinter import *

root=Tk()
root.geometry("1280x720")

global Req_Image, Login_Image, img1, img3, fd_flag
Req_Image= PhotoImage(file="GUIResources/Images/RequirementsBase.png")
Login_Image= PhotoImage(file='GUIResources/Images/LoginBase.png')
img1 = PhotoImage(file='GUIResources/Images/LoginButton.png')
img3 = PhotoImage(file='GUIResources/Images/RequirementsButton.png')
fd_flag=0

def LoginButtonMain():
    global Login_Image
    my_canvas.create_image(0, 0, image=Login_Image, anchor='nw')
    # Login Button Main Window

    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=LoginButton,
        relief="flat").place(x=655, y=318)
    print("Done")

def LoginButton():
    global fd_flag
    x=GUIResources.auth()
    fd_flag=1
    tkinter.messagebox.showinfo("Login", f'Login Successful! Welcome {x[1]}.')

def RequirementsMain():
    global Req_Image
    my_canvas.create_image(0, 0, image=Req_Image, anchor='nw')
    # Requirements Button Main Window

    b1 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=RequirementsButton,
        relief="flat").place(x=655, y=318)
    print("Done")

def RequirementsButton():
    tkinter.messagebox.showinfo("Requirements", f'Requirements installed successfully!')

def GuideMain():
    # global Guide_Image
    # my_canvas.create_image(0, 0, image=Guide_Image, anchor='nw')
    # # Requirements Button Main Window
    tkinter.messagebox.showinfo("Guide", """Login: Use this category to log in. You need to log in to use the essential features.
                                \nOpening Price: Use this category to view the current opening price of the asset.
                                \nHistorical Data: Use this category to view the history of the asset. This is represented graphically.
                                \nStock Market Clustering: Use this category to cluster companies. Number of clusters can be defined by the user.
                                \nStock Market Prediction: Use this category for predicting the market price for the following day.
                                \nRequirements: Use this category to install all the necessary requirements for the program. This is an essentila step when running this program for the first time.""")

def CreditsButton():
    tkinter.messagebox.showinfo("Credits:", f'Project made by: \nAswin P. Alex\nNatasha Sanjeev\n Mrithula S\n Devika Raj')

def OpeningPriceButton():
    global fd_flag
    if fd_flag==0:
        tkinter.messagebox.showinfo("Alert!",f'Please Log in inorder to use this function')
    else:
        GUIResources.op()

def HistoricalDataButton():
    global fd_flag
    if fd_flag==0:
        tkinter.messagebox.showinfo("Alert!",f'Please Log in inorder to use this function')
    else:
        GUIResources.hd()

def StockMarketClusteringButton():
    global fd_flag
    if fd_flag==0:
        tkinter.messagebox.showinfo("Alert!",f'Please Log in inorder to use this function')
    else:
        GUIResources.smc()

def StockMarketPredectionButton():
    global fd_flag
    if fd_flag==0:
        tkinter.messagebox.showinfo("Alert!",f'Please Log in inorder to use this function')
    else:
        GUIResources.smp()

#Background Image
bg = PhotoImage(file="GUIResources/Images/Base.png")

#Window Title
root.title("Stock Market Assistant")

#Background using canvas

my_canvas= Canvas(root, width=1280, height= 720)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=Login_Image, anchor='nw')

#Login Button Sidebar
img0 = PhotoImage(file='GUIResources/Images/Login.png')
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = LoginButtonMain,
    relief = "flat").place(x=2, y=60)

#Login Button Main Window, the reason this is here is because this is the first window that appears
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = LoginButton,
    relief = "flat").place(x=655, y=318)

#Requirements Sidebar
img2 = PhotoImage(file='GUIResources/Images/Requirements.png')
b0 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = RequirementsMain,
    relief = "flat").place(x=2, y=362)

#Guide Sidebar
img4 = PhotoImage(file='GUIResources/Images/Guide.png')
b0 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = GuideMain,
    relief = "flat").place(x=2, y=422)

#Guide Sidebar
img5 = PhotoImage(file='GUIResources/Images/Credits.png')
b0 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = CreditsButton,
    relief = "flat").place(x=2, y=482)

#Guide Opening Price
img6 = PhotoImage(file='GUIResources/Images/OpeningPriceButton.png')
b0 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = OpeningPriceButton,
    relief = "flat").place(x=2, y=122)

#Guide Historical Data
img7 = PhotoImage(file='GUIResources/Images/HistoricalDataButton.png')
b0 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = HistoricalDataButton,
    relief = "flat").place(x=2, y=182)

#Guide Stock Market Clustering
img8 = PhotoImage(file='GUIResources/Images/StockMarketClusteringButton.png')
b0 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = StockMarketClusteringButton,
    relief = "flat").place(x=2, y=242)

#Guide Stock Market Prediction
img9 = PhotoImage(file='GUIResources/Images/StockMarketPredectionButton.png')
b0 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = StockMarketPredectionButton,
    relief = "flat").place(x=2, y=302)

root.mainloop()