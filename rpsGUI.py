import random
from tkinter import *

#dictionaries and vars
outcomes = {
    "rock":{"rock":1,"paper":0,"scissors":2}, # tie, lose, win
    "paper":{"rock":2,"paper":1,"scissors":0}, # win, tie, lose
    "scissors":{"rock":0,"paper":2,"scissors":1} #lose, win, tie
}

comp_score = 0
player_score = 0

#Functions
def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"

def outcome_handler(user_choice):
    global comp_score
    global player_score
    random_number = random.randint(1,3)
    computer_choice = converted_outcome(random_number)
    outcome = outcomes[user_choice][computer_choice]

    player_choice_label.config(fg="red",text="Player Choice : "+str(user_choice))
    computer_choice_label.config(fg="green",text="Computer Choice : "+str(computer_choice))

    if outcome      == 2:
        player_score = player_score + 2
        player_score_label.config(text="Player : "+str(player_score))
        outcome_label.config(fg="blue",text="Outcome : Player Won")
    elif outcome    == 0:
        comp_score   = comp_score   + 2
        computer_score_label.config(text="Computer : "+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome : Computer Won")
    elif outcome    == 1:
        player_score = player_score + 1
        comp_score   = comp_score   + 1
        player_score_label.config(text="Player : "+str(player_score))
        computer_score_label.config(text="Computer : "+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome : Draw")

#main screen 
master = Tk()
master.title("Rock, Paper, Scissor")

#set the background color 
#master.configure(background='Yellow')

#libraries
Label(master,text="Rock, Paper, Scissor", font=("calibri",16)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="Please select an option",font=("calibri",12)).grid(row=1,sticky=N)
player_score_label = Label(master,text="Player : 0",font=("calibri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(master,text="Opponent : 0",font=("calibri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label = Label(master,font=("calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(master,font=("calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(master,font=("calibri",12))
outcome_label.grid(row=3,sticky=N)

#Buttons
Button(master,text="Rock",width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(master,text="Paper",width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,pady=5)
Button(master,text="Scissors",width=15,command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,padx=5,pady=5)

#Dummy label 
Label(master).grid(row=5)

master.mainloop()