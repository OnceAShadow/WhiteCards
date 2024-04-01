# WhiteCards.py
from tkinter import *

root = Tk()
root.title("White Cards")
root.configure(background="grey")
root.geometry("1000x600")
root.maxsize(1000, 600)

Question = Label(root, text="Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant retarded question")
Question.pack(side="top", anchor="nw", padx=40, pady=25)
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

Count = Label(root, text="1/20")
Count.pack(side="bottom", anchor="s", padx=30, pady=10)
Count.config(font=("Font", 18))

submit_button = Button(root, text="Done", height=2, width=5, command=submit)
submit_button.pack(side="bottom", anchor="se", padx=30)





root.mainloop()

