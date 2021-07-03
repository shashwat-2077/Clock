import datetime
import time
# importing system date and time

# import turtle as tt

from tkinter import* 
from PIL import Image,ImageTk
# importing library

# #setting the bg image

screen = Tk()       #defining screen window

screen.title('Digital Clock')   #setting title of the clock
screen.iconbitmap("D:\\CLASS\\Self\\Clock\\Digital\\pic.png")   #setting the thumbnail of window

#designate the height and width of the window
win_width = 1200    
win_height = 720

window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

x = (window_width/2) - (win_width/2)
y = (window_height/2) - (win_height/2)


screen.geometry(f'{win_width}x{win_height}+{int(x)}+{int(y)}') #set the screen size of the clock 


load = Image.open("D:\\CLASS\\Self\\Clock\\Digital\\bg.png")
render = ImageTk.PhotoImage(load)
img = Label(screen, image=render, anchor=CENTER)
img.place(x=0,y=0)

screen.configure(background='black')    #setting the background colour of the clock


def clock():       #defining the clock function now
    t1=time.strftime('%H:%M:%S %p') #variable to store the currnt time of the computer 

    #here h means hour, m = minutes, s = seconds and p = am/pm
    #now setting the face (graphics) of the clock

    t2=Label(screen, text=t1, font=('ds-Digital',60 , 'bold'),fg='#00ff00', bg='black')
    #setting the font type, size, styles, colour and the background colour size-40, bold style

    t2.after(200,clock)
    t2.place(x=400,y=150)        #setting the place of the clock
    t3 = datetime.date.today()      #storing today's date and current time in t3

    #setting the format of the date and storing it in d1
    d1=Label(screen, text=t3.day, font=('ds-Digital', 40, 'bold'), fg='#d0fe1d', bg='black').place(x=480,y=350)     #for day 
    d1=Label(screen, text=t3.month, font=('ds-Digital', 40, 'bold'), fg='#FF7F50', bg='black').place(x=580,y=350)   #for month
    d1=Label(screen, text=t3.year, font=('ds-Digital', 40, 'bold'), fg='#FF0000', bg='black').place(x=670,y=350)   #for year
    
    #decorating the clock to show text like hrs, mins, secs etc.
    date=Label(screen, text='Date', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=475,y=420)   #for printing date
    month=Label(screen, text='Month', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=570,y=420)   #for printing month
    year=Label(screen, text='Year', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=720,y=420)   #for printing year

    hour=Label(screen, text='Hour', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=410,y=250)   #for printing hour 
    min=Label(screen, text='Minutes', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=500,y=250)   #for printing minutes
    sec=Label(screen, text='Seconds', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=620,y=250)   #for printing seconds

    credit=Label(screen, text='Collaborative Project by ', font=('ds-Digital',20),fg='#00ff00', bg='black').place(x=460,y=550)  #credits 
    credit=Label(screen, text='Shashwat x Akanksha ', font=('ds-Digital', 30, 'italic','bold'),fg='#00ff00', bg='black').place(x=400,y=600)  #credits 



# tt.forward(300)
# tt.left(90)
# tt.forward(300)
# tt.left(90)
# tt.forward(300)
# tt.left(90)
# tt.forward(300)
# tt.left(90)

clock()
screen.mainloop()

