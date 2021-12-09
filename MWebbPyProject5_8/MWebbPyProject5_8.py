import tkinter as tk
import tkinter.font as tkFont

#create tkinter object #initilaize interface
app = tk.Tk()

#set app title
app.winfo_toplevel().title("Python GUI Example")

#set obj size
app.geometry("640x480")

#create font to use in app
fontStyle = tkFont.Font(family="Tahoma", size=24)

#create a label
labelExample = tk.Label(app, text="The system is idle", font=fontStyle)




def systemOn():
    
    #change the label text
    labelExample.config(text="System Running.")
   



def systemOff():
    
    #change the label text
    labelExample.config(text="System Off.")
   


#create a virtual image to be used for sizing the buttons in pixels instead of text units
pixelVirtual = tk.PhotoImage(width=1,height=1)

#put the label in the app using pack example (TOP, BOTTOM, LEFT, RIGHT)
labelExample.pack(side=tk.TOP)

#button example - what window, button text, bkgd color, foreground color, use virtual image for sizing, width, height, compond ="c" to show text
buttonExample1=tk.Button(app, text="System On", bg="green", fg="white", image=pixelVirtual, width=200, height=100,compound="c", command = systemOn)
                                                                        #we will come back later and associate this with a command^

#since we virtual image, we can give this a pixel loc on the screen 
buttonExample1.place(x=100,y=400)

#create a second button
buttonExample2=tk.Button(app, text="System Off", bg="red", fg="white", image=pixelVirtual, width=200, height=100,compound="c", command = systemOff)

#second button, we can give this a pixel loc on the screen further down the screen
buttonExample2.place(x=340,y=400)


#create a minimal exit button (TOP, BOTTOM, LEFT, RIGHT)
buttonExample4=tk.Button(app, text ="EXIT", bg = 'black',fg = 'white',command = app.quit)
buttonExample4.pack(side=tk.TOP)         #see, we tied this to a command^


#label at the top, exit at the bottom, and three buttons
#we PACK those two because we always want them to be AT THAT POSITION within the app

app.mainloop()