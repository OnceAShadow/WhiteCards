# WhiteCards.py
from tkinter import *

# Window
root = Tk()
root.title("White Cards")
root.configure(background="grey")
root.geometry("1200x700")
root.maxsize(1200, 700)

# Variables
test = {}
totalQuestions = 0
currentQuestion = 1
rightAnswers = 0
partsCount = 0
wasRightAnswer = False

statusA = IntVar()
statusB = IntVar()
statusC = IntVar()
statusD = IntVar()
statusE = IntVar()
statusF = IntVar()
statusG = IntVar()


# Read file to array (?# = Question, !# = Possible Answers, @# = Right Answers)
file = open("test.wc", "r")
for line in file:

    line = line.lstrip()
    line = line.rstrip()
    newLine = line.split("#")
    
    if len(newLine) == 2:
        if newLine[0] == "?":
            totalQuestions += 1
            partsCount = 0
            test[totalQuestions, partsCount] = newLine[1]

        elif newLine[0] == "!" or newLine[0] == "@":
            partsCount += 1
            test[totalQuestions, partsCount] = line
    

def createNextQuestion():
    Question = Label(root, text=test[currentQuestion, 0], wraplength=1120, justify=LEFT)
    Question.pack(side="top", anchor="nw", padx=30, pady=25)
    Question.config(font=("Font", 18))

    if test.get((currentQuestion, 1)) != None:
        tempText = test[currentQuestion, 1].split("#")[1]
        answerA = Checkbutton(root, text=tempText, variable=statusA, wraplength=1000, justify=LEFT)
        answerA.pack(side="top", anchor="nw", padx=70, pady=8)
        answerA.config(font=("Font", 15))

    if test.get((currentQuestion, 2)) != None:
        tempText = test[currentQuestion, 2].split("#")[1]
        answerB = Checkbutton(root, text=tempText, variable=statusB, wraplength=1000, justify=LEFT)
        answerB.pack(side="top", anchor="nw", padx=70, pady=8)
        answerB.config(font=("Font", 15))

    if test.get((currentQuestion, 3)) != None:
        tempText = test[currentQuestion, 3].split("#")[1]
        answerC = Checkbutton(root, text=tempText, variable=statusC, wraplength=1000, justify=LEFT)
        answerC.pack(side="top", anchor="nw", padx=70, pady=8)
        answerC.config(font=("Font", 15))

    if test.get((currentQuestion, 4)) != None:
        tempText = test[currentQuestion, 4].split("#")[1]
        answerD = Checkbutton(root, text=tempText, variable=statusD, wraplength=1000, justify=LEFT)
        answerD.pack(side="top", anchor="nw", padx=70, pady=8)
        answerD.config(font=("Font", 15))

    if test.get((currentQuestion, 5)) != None:
        tempText = test[currentQuestion, 5].split("#")[1]
        answerE = Checkbutton(root, text=tempText, variable=statusE, wraplength=1000, justify=LEFT)
        answerE.pack(side="top", anchor="nw", padx=70, pady=8)
        answerE.config(font=("Font", 15))

    if test.get((currentQuestion, 6)) != None:
        tempText = test[currentQuestion, 6].split("#")[1]
        answerF = Checkbutton(root, text=tempText, variable=statusF, wraplength=1000, justify=LEFT)
        answerF.pack(side="top", anchor="nw", padx=70, pady=8)
        answerF.config(font=("Font", 15))

    if test.get((currentQuestion, 7)) != None:
        tempText = test[currentQuestion, 7].split("#")[1]
        answerG = Checkbutton(root, text=tempText, variable=statusG, wraplength=1000, justify=LEFT)
        answerG.pack(side="top", anchor="nw", padx=70, pady=8)
        answerG.config(font=("Font", 15))
        answerG.pack_forget()

    # Bottom Info
    questionCounter = str(currentQuestion) + "/" + str(totalQuestions)
    Count = Label(root, text=questionCounter)
    Count.pack(side="bottom", anchor="s", padx=30, pady=7)
    Count.config(font=("Font", 14))

    # Submit Button
    submit_button = Button(root, text="Done", height=3, width=8, command=validateAnswer)
    submit_button.pack(side="bottom", anchor="se", padx=30)


def clearCard():
    for child in root.winfo_children():
        child.destroy() 

    statusA.set(0)
    statusB.set(0)
    statusC.set(0)
    statusD.set(0)
    statusE.set(0)
    statusF.set(0)
    statusG.set(0)


def showAnswer():
    answerText = "True" if wasRightAnswer else "False"
    AnswerLabel = Label(root, text=answerText, wraplength=1120, justify=LEFT)
    AnswerLabel.pack(side="top", anchor="nw", padx=60, pady=25)
    AnswerLabel.config(font=("Font", 18))

    totalText = str(rightAnswers) + " / " + str(currentQuestion)
    TotalSoFar = Label(root, text=totalText, wraplength=1120, justify=LEFT)
    TotalSoFar.pack(side="top", anchor="nw", padx=60, pady=10)
    TotalSoFar.config(font=("Font", 18))

    questionCounter = str(currentQuestion) + "/" + str(totalQuestions)
    Count = Label(root, text=questionCounter)
    Count.pack(side="bottom", anchor="s", padx=30, pady=7)
    Count.config(font=("Font", 14))

    submit_button = Button(root, text="Next Question", height=3, width=8, command=continueTest)
    submit_button.pack(side="bottom", anchor="se", padx=30)


def validateAnswer():
    global wasRightAnswer
    wasRightAnswer = True

    if test.get((currentQuestion, 1)) != None:
        if test[currentQuestion, 1].split("#")[0] == "!" and statusA.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 1].split("#")[0] == "@" and statusA.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 2)) != None:
        if test[currentQuestion, 2].split("#")[0] == "!" and statusB.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 2].split("#")[0] == "@" and statusB.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 3)) != None:
        if test[currentQuestion, 3].split("#")[0] == "!" and statusC.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 3].split("#")[0] == "@" and statusC.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 4)) != None:
        if test[currentQuestion, 4].split("#")[0] == "!" and statusD.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 4].split("#")[0] == "@" and statusD.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 5)) != None:
        if test[currentQuestion, 5].split("#")[0] == "!" and statusE.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 5].split("#")[0] == "@" and statusE.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 6)) != None:
        if test[currentQuestion, 6].split("#")[0] == "!" and statusF.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 6].split("#")[0] == "@" and statusF.get() == 0:
            wasRightAnswer = False

    if test.get((currentQuestion, 7)) != None:
        if test[currentQuestion, 7].split("#")[0] == "!" and statusG.get() == 1:
            wasRightAnswer = False
        if test[currentQuestion, 7].split("#")[0] == "@" and statusG.get() == 0:
            wasRightAnswer = False

    if wasRightAnswer == True:
        global rightAnswers
        rightAnswers += 1

    clearCard()
    showAnswer()


def showResults():
    print(str(rightAnswers) + "/" + str(totalQuestions))


def continueTest():
    global currentQuestion
    print(rightAnswers, "/", currentQuestion, "/", totalQuestions)
    currentQuestion += 1

    clearCard()
    if currentQuestion > totalQuestions:
        showResults()
    else: 
        createNextQuestion()


# Start Of Test
print("TotalQuestion: ", totalQuestions)
print("currentQuestion: ", currentQuestion)

createNextQuestion()
root.mainloop()

