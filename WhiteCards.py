# WhiteCards.py
from tkinter import *

root = Tk()
root.title("White Cards")
root.configure(background="grey")
root.geometry("1000x600")
root.maxsize(1000, 600)

Question = Label(root, text="Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", wraplength=920)
Question.pack(side="top", anchor="nw", padx=40, pady=20)
Question.config(font=("Font", 18))
# wrap text
# change color

statusA = IntVar()
answerA = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusA, wraplength=860)
answerA.pack(side="top", anchor="nw", padx=60, pady=7)
answerA.config(font=("Font", 14))

statusB = IntVar()
answerB = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks", variable=statusB, wraplength=860)
answerB.pack(side="top", anchor="nw", padx=60, pady=7)
answerB.config(font=("Font", 14))

statusC = IntVar()
answerC = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusC, wraplength=860)
answerC.pack(side="top", anchor="nw", padx=60, pady=7)
answerC.config(font=("Font", 14))

statusD = IntVar()
answerD = Checkbutton(root, text="thisskjdhsakdfhdfkdsfhksdfhskjfhskjdfhsdkjfhsdkjfhsdkjfhsdkjfhsdkjh is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusD, wraplength=860)
answerD.pack(side="top", anchor="nw", padx=60, pady=7)
answerD.config(font=("Font", 14))

statusE = IntVar()
answerE = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusE, wraplength=860)
answerE.pack(side="top", anchor="nw", padx=60, pady=7)
answerE.config(font=("Font", 14))

statusF = IntVar()
answerF = Checkbutton(root, text="this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant questionAsk a Question? Ask a Question? this is a very very vyer aflajlkgjalk long question that I need to ask to check what it looks like when there is a giant question", variable=statusF, wraplength=860)
answerF.pack(side="top", anchor="nw", padx=60, pady=7)
answerF.config(font=("Font", 14))


def submit():
    print("Answer Submited")

Count = Label(root, text="1/20")
Count.pack(side="bottom", anchor="s", padx=30, pady=7)
Count.config(font=("Font", 14))

submit_button = Button(root, text="Done", height=2, width=5, command=submit)
submit_button.pack(side="bottom", anchor="se", padx=30)





root.mainloop()

