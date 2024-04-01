# WhiteCards.py
from tkinter import *

root = Tk()
root.title("White Cards")
root.configure(background="grey")
root.geometry("1000x600")
root.maxsize(1000, 600)

Question = Label(root, text="Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant retarded question")
Question.pack(side="top", anchor="nw", padx=40, pady=20)
Question.config(font=("Font", 20))
# wrap text
# change color

statusA = IntVar()
answerA = Checkbutton(root, text="Answer A", variable=statusA)
answerA.pack(side="top", anchor="nw", padx=70, pady=12)
answerA.config(font=("Font", 14))

statusB = IntVar()
answerB = Checkbutton(root, text="Answer B", variable=statusB)
answerB.pack(side="top", anchor="nw", padx=70, pady=12)
answerB.config(font=("Font", 14))

statusC = IntVar()
answerC = Checkbutton(root, text="Answer C", variable=statusC)
answerC.pack(side="top", anchor="nw", padx=70, pady=12)
answerC.config(font=("Font", 14))

statusD = IntVar()
answerD = Checkbutton(root, text="Answer D", variable=statusD)
answerD.pack(side="top", anchor="nw", padx=70, pady=12)
answerD.config(font=("Font", 14))

statusE = IntVar()
answerE = Checkbutton(root, text="Answer E", variable=statusE)
answerE.pack(side="top", anchor="nw", padx=70, pady=12)
answerE.config(font=("Font", 14))

statusF = IntVar()
answerF = Checkbutton(root, text="Answer F", variable=statusF)
answerF.pack(side="top", anchor="nw", padx=70, pady=12)
answerF.config(font=("Font", 14))

def submit():
    print("Answer Submited")

submit_button = Button(root, text="Done", height=2, width=5, command=submit)
submit_button.pack(side="bottom", anchor="se", padx=20, pady=20)

Count = Label(root, text="1/20")
Count.pack(side="bottom", anchor="s", padx=30)
Count.config(font=("Font", 18))


root.mainloop()


'''
activebackground & activeforeground -- sets the background or foreground colors when the cursor is over the button
bd -- sets the border width of button in pixels
bg & fg -- sets the background and foreground colors
font -- chooses the text font for the button
height & width -- sets height and width sizes
image -- uses an image on the button rather than text

# select image for on button
on_button_photo = PhotoImage(file="onButton.gif")
photo = on_button_photo.subsample(10,10)
turn_on = ttk.Button(root, image=photo, command=turnOnTV)
turn_on.pack()

side -- specifies the general location of the widget in the window, arguments are 'top', 'bottom', 'left', 'right' (default is 'top').
fill -- which directions you want the widget to fill in the parent window, can choose 'x', 'y' directions, or 'both'. 
padx, pady -- the number of pixels surrounding the widget to create a padding between other widgets, for horizontal or vertical padding.
ipadx, ipady -- how many pixels to use for padding inside the widget, also for horizontal or vertical padding
expand -- set to True if you want the widget to stretch if the parent window expands. Default is False. 
anchor -- where the widget is placed in the parent widget, specified by  'n', 's', 'e', 'w', or some combination of them. Default is 'center'.
text = Label(root, text="Nothing will work unless you do.")
text.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

image = PhotoImage(file="025.gif")
img = Label(root, image=image)
img.pack()
'''