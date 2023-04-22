"""
21/04/2023
URL Shortener Using Python --------------- Created By Dinesh Singh
"""
from tkinter import *
import pyshorteners

#Method for shorting Given URL
def url_shortener():
    global url,shorty,short_url
    if short_url.get():
        short_url.set("")
    if url.get():
        short_url.set(pyshorteners.Shortener().tinyurl.short(url.get()))

#Initializing app window
app_window = Tk()
app_window.geometry("400x300")
app_window.resizable(False,False)
app_window.iconbitmap("appicon.ico")
app_window.title("URL Shortener")

#Background image 
bg_img = PhotoImage(file="bgimg.png")

#background canvas
bg_canvas = Canvas(app_window,width=400,height=300)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img)

#Frame for packing all the widgets
main_frame = Frame(bg_canvas,height=200,width=300,bg="#F6F1F4")
main_frame.pack(pady=50)

#Necessary variable initialization
url = StringVar()
url.set("")
short_url = StringVar()
short_url.set("")

#Label for app title
Label(main_frame,text="URL SHORTENER",font=("Helvetica",24,"bold"),fg="#34282C",bg="snow").place(x=10,y=10)

#Label for Entering URL
Label(main_frame,text="Enter URL",font=("timesnewroman",12,"bold"),bg="snow",fg="#34282C").place(x=10,y=70)

#entry for url
Entry(main_frame,textvariable=url,font=("timesnewroman",12),bg="snow",fg="#34282C",relief=RAISED).place(x=100,y=70)

#Button to get shorten url
Button(main_frame,text="Get Short URL",bg="#34282C",font=("timesnewroman",14,"bold"),fg="white",relief=RAISED,command=url_shortener).place(x=80,y=100)

#Label for URL
Label(main_frame,text="URL ",font=("timesnewroman",12,"bold"),fg="#34282C",bg="snow").place(x=10,y=150)

#from here we get shorten url
short = Entry(main_frame,textvariable=short_url,font=("timesnewroman",12),bg="snow",fg="#34282C",relief=RAISED).place(x=100,y=150)

#Window mainloop
app_window.mainloop()