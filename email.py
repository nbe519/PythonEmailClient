#Noah Eaton
#Exploring Computer Science
#Email Client
#An email application which will take the subject, who it is to and 
#the time and tell the user that the email has been sent. 

#Import the module
from tkinter import *
import tkinter.messagebox
from tkinter import font
import datetime
import webbrowser

#Pull the current time but only the hour and minute
time = datetime.datetime.time(datetime.datetime.now())
time = time.strftime("%I:%M %p")
time = str(time)

#A function for the button in which when clicked will run through the following code
def sendEmail(sent,subject):
	#collect the math problem then change it into an integer
	math = entMath.get()
	math = int(math)
	#If the users answer is 4 and their is a sender present, send the message and clear the text boxes
	if math == 2 + 2 and len(entSend.get()) > 0:
		robotlbl.configure(text="You are not a robot!")
		#Pull a pop-up screen which tells the user that the message sent
		tkinter.messagebox.showinfo(title="Email Sent", message="Your email with the subject, %s, has been sent to %s at %s " %(sent, subject, time))
		#Clear the text fields 
		entSend.delete(0, 'end')
		entsub.delete(0, 'end')
		entComp.delete(0, 'end')
		entMath.delete(0, 'end')
	#If the user has  an incorrect answer or has no sender, fix the user fields
	else:
		robotlbl.configure(text="Email could not sent, make sure every field is filled out and filled correctly.")
url = 'https://www.gmail.com'
new = 1
def openGmail():
	button(webbrowser.open(url, new=new))

#Create the tkinter window
window = Tk()
window.title("Nmail")
window.configure(bg="gray")
window.geometry("500x775")

#bring helvetica font into tkinter
appHighlightFont = font.Font(family='Helvetica', size=12)

#Email Title/Header
title = Label(window, text="Welcome to ", bg="gray")
title.config(font=('Helvetica', 32))
title.grid(row=0, column=30)
title.pack()

#Add an image below the title
imgpath = r"NMail.gif"
img = PhotoImage(file=imgpath)
photoLabel = Button(window, image=img, command= lambda: Button(webbrowser.open(url, new=new)))
photoLabel.pack()

#Sender Label
lblS = Label(window, text="To:", bg="gray")
lblS.grid(row=1, column=0)
lblS.pack()

#Entry for Sender
entSend = Entry(window,relief=SUNKEN, bd=4)
entSend.configure(font=appHighlightFont)
entSend.grid(row=3, column=0)
entSend.pack()

#Label for the subject
lblsub = Label(window, text="Subject: ", bg="gray")
lblsub.grid(row=4, column=0)
lblsub.pack()

#Entry box for subject
entsub = Entry(window, relief=SUNKEN, bd=4)
entsub.grid(row=1, column=1)
entsub.configure(font=appHighlightFont)
entsub.pack()

#Label for email box
lblCompose = Label(window, text="Compose Email Below", bg="gray")
lblCompose.grid(row=5, column=0)
lblCompose.pack()

#Text box for email
entComp = Text(window, relief=SUNKEN, bd=8)
entComp.configure(font=appHighlightFont)
entComp.pack()

#Math problem
lblMath = Label(window, text="To prove you are not a robot, what is 2 + 2", bg="gray")
lblMath.grid(row=6, column=0)
lblMath.pack()

entMath = Entry(window, relief=SUNKEN, bd=4)
entMath.pack()

#The label which tells the user if they are a robot 
robotlbl = Label(window, bg="gray")
robotlbl.pack()

#A button which will activate the function at line 20
btn = Button(window, text="Submit", command=(lambda: sendEmail(entsub.get(), entSend.get())))
btn.pack()

#Draw the scene
window.mainloop()