# WhiteCards.py
from tkinter import *

root = Tk()
root.title("White Cards")
root.configure(background="grey")
root.geometry("1200x700")
root.maxsize(1200, 700)

Question = Label(root, text="Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", wraplength=1120, justify=LEFT)
Question.pack(side="top", anchor="nw", padx=40, pady=25)
Question.config(font=("Font", 18))

statusA = IntVar()
answerA = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusA, wraplength=1000, justify=LEFT)
answerA.pack(side="top", anchor="nw", padx=70, pady=8)
answerA.config(font=("Font", 15))

statusB = IntVar()
answerB = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks", variable=statusB, wraplength=1000, justify=LEFT)
answerB.pack(side="top", anchor="nw", padx=70, pady=8)
answerB.config(font=("Font", 15))

statusC = IntVar()
answerC = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusC, wraplength=1000, justify=LEFT)
answerC.pack(side="top", anchor="nw", padx=70, pady=8)
answerC.config(font=("Font", 15))

statusD = IntVar()
answerD = Checkbutton(root, text="thisskjdhsakdfhdfkdsfhksdfhskjfhskjdfhsdkjfhsdkjfhsdkjfhsdkjfhsdkjh is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusD, wraplength=1000, justify=LEFT)
answerD.pack(side="top", anchor="nw", padx=70, pady=8)
answerD.config(font=("Font", 15))

statusE = IntVar()
answerE = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusE, wraplength=1000, justify=LEFT)
answerE.pack(side="top", anchor="nw", padx=70, pady=8)
answerE.config(font=("Font", 15))

statusF = IntVar()
answerF = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusF, wraplength=1000, justify=LEFT)
answerF.pack(side="top", anchor="nw", padx=70, pady=8)
answerF.config(font=("Font", 15))

def submit():
    print("Answer Submited")

Count = Label(root, text="1/20")
Count.pack(side="bottom", anchor="s", padx=30, pady=7)
Count.config(font=("Font", 14))

submit_button = Button(root, text="Done", height=2, width=5, command=submit)
submit_button.pack(side="bottom", anchor="se", padx=30)

root.mainloop()
