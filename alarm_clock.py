from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
from PIL import Image,ImageTk
import datetime
import time
#libraries


def alarm(set_alarm):
    toast = ToastNotifier() #to get notified when the sound plays
    while True:     #infinite loop
        time.sleep(1)
        date = datetime.datetime.now()
        global now
        now = date.strftime("%H:%M:%S")     #storing current time
        print(now)
        #count_down = Label(root,text = now, font=("Cambria",10,"bold")).place(x=220,y=250)
        
        if now == set_alarm:        
            print("Alarm Clock")
            #over = Label(root,text ="Alarm Clock", font=("Cambria",10,"bold")).place(x=220,y=270)
            toast.show_toast("Alarm Clock",duration=1)
            playsound("audio.mp3")

def clock():       #defining the clock function now
    t1=time.strftime('%H:%M:%S %p') #variable to store the currnt time of the computer 

    #here h means hour, m = minutes, s = seconds and p = am/pm
    #now setting the face (graphics) of the clock

    t2=Label(root, text=t1, font=('ds-Digital',60 , 'bold'),fg='#00ff00', bg='black')
    #setting the font type, size, styles, colour and the background colour size-40, bold style

    t2.after(200,clock)
    t2.place(x=400,y=20)        #setting the place of the clock
    t3 = datetime.date.today()      #storing today's date and current time in t3

    #setting the format of the date and storing it in d1
    d1=Label(root, text=t3.day, font=('ds-Digital', 40, 'bold'), fg='#d0fe1d', bg='black').place(x=480,y=430)     #for date 
    d1=Label(root, text=t3.month, font=('ds-Digital', 40, 'bold'), fg='#d0fe1d', bg='black').place(x=580,y=430)   #for month
    d1=Label(root, text=t3.year, font=('ds-Digital', 40, 'bold'), fg='#d0fe1d', bg='black').place(x=670,y=430)   #for year
    
    #decorating the clock to show text like hrs, mins, secs etc.
    date=Label(root, text='Date', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=475,y=500)   #for printing date
    month=Label(root, text='Month', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=570,y=500)   #for printing month
    year=Label(root, text='Year', font=('ds-Digital', 15, 'italic'), fg='#00ff00', bg='black').place(x=720,y=500)   #for printing year

    hour=Label(root, text='Hour', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=410,y=110)   #for printing hour 
    min=Label(root, text='Minutes', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=500,y=110)   #for printing minutes
    sec=Label(root, text='Seconds', font=('ds-Digital', 20, 'italic'), fg='#00ff00', bg='black').place(x=620,y=110)   #for printing seconds


def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.title('Alarm Clock')   #setting title of the clock
root.iconbitmap("icon.ico")   #setting the thumbnail of window

#designate the height and width of the window
win_width = 1280  
win_height = 720

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

x = (window_width/2) - (win_width/2)
y = (window_height/2) - (win_height/2)

root.geometry(f'{win_width}x{win_height}+{int(x)}+{int(y)}') #set the screen size of the clock 

load = Image.open("bg.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render, anchor=CENTER)
img.place(x=0,y=0)
root.configure(background='black')    #setting the background colour of the clock


info = Label(root,text = "(24)Hour  Min   Sec", font=('Cambria',20),fg='#00ff00', bg='black' ).place(x = 500, y=210)
set_time = Label(root,text = "Set Time",relief = "solid",font=("Cambria",15,"bold"), fg='#00ff00', bg='black').place(x=400,y=250)
# count_down = Label(root,text = now, font=("Cambria",10,"bold")).place(x=220,y=250)


# Entry Variables
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "white",width = 8).place(x=530,y=260)
min_E = Entry(root,textvariable = min,bg = "white",width = 8).place(x=610,y=260)
sec_E = Entry(root,textvariable = sec,bg = "white",width = 8).place(x=680,y=260)

submit = Button(root,text = "Set Alarm", font=('Cambria',15),fg='#00ff00', bg='black',width = 15,command = getvalue).place(x =500, y=330)

credit=Label(root, text='Collaborative Project by ', font=('Cambria',20),fg='#00ff00', bg='black').place(x=500,y=570)  #credits 
credit=Label(root, text='Shashwat x Akanksha ', font=('Cambria', 30, 'italic','bold'),fg='#00ff00', bg='black').place(x=440,y=620)  #credits 

clock()
root.mainloop()