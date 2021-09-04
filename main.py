from tkinter import *
from tkinter.ttk import *
import time

def fire():
    max_fuel = 100
    fuel = 0
    speed = 1
    while(fuel<max_fuel):
        time.sleep(0.05)
        bar['value']+=(speed/max_fuel)*100
        fuel+=speed
        percent.set(str(int((fuel/max_fuel)*100))+"%")
        text.set(str(fuel)+"/"+str(max_fuel)+" max_fuel completed")
        window.update_idletasks()
    while (fuel==max_fuel):
        canvas.move(my_image,0,yVelocity)
        window.update()
        time.sleep(0.00001)
            

        



window = Tk()
WIDTH = 500
HEIGHT = 700
xVelocity = 1
yVelocity = -1
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
background_p = PhotoImage(file='space.png')
background = canvas.create_image(0,0,image=background_p,anchor=NW)
photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(250,425,image=photo_image)
image_width = photo_image.width()
image_height = photo_image.height()
button = Button(text="launch",command=fire)
button.place(x=200,y=620)
percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.place(x=100,y=570)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

window.mainloop()
