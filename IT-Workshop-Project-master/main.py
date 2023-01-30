import random
from tkinter import *


window = Tk()
window.geometry("1000x700")
window.resizable(0,0)
window['background'] = '#226300'
window.title("Scissor paper Rock game")


wlcm_label = Label(window, text="Welcome to Scissor paper Rock game ...", font=("Arial Bold", 20), bg='#226300', fg='white').pack()


starting_label = Label(window, text="Enter how many rounds you want to play >>>",font=("Arial Bold", 13), bg='#226300', fg='white')
starting_label.place(x=285, y=40)

txt = Entry(window, width=5)          # Enter here the no of rounds you want to play
txt.place(x=655, y=41)


count_you = 0                         # initially scores of both Human player and Bot is 0
count_bot = 0


# scissor function runs when we click 'Scissor button' during game
def scissor():
   global count_you
   global count_bot
   global k
   global num

   if k > 0:                                    # indirectly it is working as a loop, so that player can play only 'k' no of rounds
    # human = 1
    bot = random.randint(1,3)

    if bot == 1 :                               # all cases, if Human player chooses Rock 
        icon_1_label.configure(image=icon_5)
        icon_2_label.configure(image=icon_6)
        count_you = count_you
        count_bot = count_bot
        
    elif bot == 2 :
        icon_1_label.configure(image=icon_3)
        icon_2_label.configure(image=icon_6)
        count_you = count_you + 1
        count_bot = count_bot
    elif bot == 3 :
        icon_1_label.configure(image=icon_1)
        icon_2_label.configure(image=icon_6)       
        count_you = count_you
        count_bot = count_bot + 1
    k = k - 1 

    string = " BOT | YOU \n" + str(count_bot) + "   |   " + str(count_you)      
    ScoreBoard_label.configure(text=string)                                     # updating scores in score board
    
    round_count = num - k
    string2 = "  Round " + str(round_count) + "  "
    round_label.configure(text=string2)                                         # updating round number
    
    if (round_count == num):        # if all rounds are done displays the game result through calling "Endgame_msg()" function
        EndGame_msg()
    
    print(count_bot)                # for testing if codes are working properly or not, print the scores and round numbers (in reverse order) in terminal
    print(count_you) 
    print(k)


# paper function runs when we click 'Paper button' during game
def paper():
   global count_you
   global count_bot
   global k
   global num

   if k > 0:
    # human = 2
    bot = random.randint(1,3)

    if bot == 1 :
        icon_1_label.configure(image=icon_5)
        icon_2_label.configure(image=icon_4)
        count_you = count_you
        count_bot = count_bot + 1
    elif bot == 2 :
        icon_1_label.configure(image=icon_3)
        icon_2_label.configure(image=icon_4)
        count_you = count_you
        count_bot = count_bot
    elif bot == 3 :
        icon_1_label.configure(image=icon_1)
        icon_2_label.configure(image=icon_4)
        count_bot = count_bot
        count_you = count_you + 1
    k = k - 1
    string = " BOT | YOU \n" + str(count_bot) + "   |   " + str(count_you)
    ScoreBoard_label.configure(text=string)
    round_count = num - k
    string2 = "  Round " + str(round_count) + "  "
    round_label.configure(text=string2)

    if (round_count == num):
        EndGame_msg()

    print(count_bot)    
    print(count_you)
    print(k)


# rock function runs when we click 'Rock button' during game
def rock():
   global count_you
   global count_bot
   global k
   global num

   if k > 0:        
    # human = 3
    bot = random.randint(1,3)

    if bot == 1 :                               
        icon_1_label.configure(image=icon_5)
        icon_2_label.configure(image=icon_2)
        count_you = count_you + 1
        count_bot = count_bot 
    elif bot == 2 :
        icon_1_label.configure(image=icon_3)
        icon_2_label.configure(image=icon_2)
        count_you = count_you
        count_bot = count_bot + 1
    elif bot == 3 :
        icon_1_label.configure(image=icon_1)
        icon_2_label.configure(image=icon_2)
        count_bot = count_bot
        count_you = count_you
    k = k - 1
    string = " BOT | YOU \n" + str(count_bot) + "   |   " + str(count_you)
    ScoreBoard_label.configure(text=string)
    round_count = num - k
    string2 = "  Round " + str(round_count) + "  "
    round_label.configure(text=string2)
    
    if (round_count == num):
        EndGame_msg()
    
    print(count_bot)    
    print(count_you)
    print(k)



# clicked function runs when we click 'START button' to start the game
def clicked():
    global k
    global num
    k = txt.get()                               # getting total number of rounds, and storing in a global variable 'k' first
    k = int(k)
    num = k                                     # data of 'k' is also saved to another global variable 'num' 
    
    start_btn.configure(text="Started ...")     # start button name changes to "Started ..." after starting the game
    start_btn.place(x=445, y=72)
    
    scissor_btn.configure(command=scissor)      # Allowing Scissor, Paper and Rock button to call their respective 'click event functions'
    paper_btn.configure(command=paper)          # Those functions are restricted to not run before START button is clicked 
    rock_btn.configure(command=rock)
    
    print("game going on")                      # tests if START button is working or not 
        

# function runs to display the result of game and "Click to continue ..." button
def EndGame_msg():
    global count_you
    global count_bot

    if (count_you > count_bot):
        result_msg_label.configure(text="    🎊 Congratulations 🎊\n      You won the game ")       # game results setting to display on screen
    elif(count_bot > count_you):
        result_msg_label.configure(text="❗Oops❗\n     you loose the game ...     ")    
    else:
        result_msg_label.configure(text="        🤝🏻 Match Draw 🤝🏻            ")    
    
    continue_btn.configure(text= "Click to continue ..." , command=Game_Reset)                       # "Click to continue ..." button appears after result
    continue_btn.place(x=416, y=230)


# function to restart game
def Game_Reset():
    global count_you
    global count_bot

    start_btn.configure(text="Play Again")                                       # After resetting, START button is named as 'Play Again'
    start_btn.place(x=440, y=72)

    count_bot = 0                                                                # resetting scores to 0
    count_you = 0
    string = " BOT | YOU \n" + str(count_bot) + "   |   " + str(count_you)
    ScoreBoard_label.configure(text=string)

    icon_1_label.configure(image=icon_1)                                         # resetting the rock images for both BOT and Human Player
    icon_2_label.configure(image=icon_2)

    continue_btn.configure(text= "" )
    continue_btn.place(x=350, y=700)                                             # hiding "Click to continue ..." button

    result_msg_label.configure(text="")                                          # 'message result' and 'Round no' is resetting to reset screen
    round_label.configure(text="")



start_btn = Button(window, text="START", font=("Arial Bold", 15), command=clicked)                          # START button to start the game
start_btn.place(x=460, y=72)


icon_1 = PhotoImage(file=r"./logos/rock.png")                                                               # All Scissor, paper and Rock logos
icon_2 = PhotoImage(file=r"./logos/rock right.png")
icon_3 = PhotoImage(file=r"./logos/paper.png")
icon_4 = PhotoImage(file=r"./logos/paper right.png")
icon_5 = PhotoImage(file=r"./logos/scissor.png")
icon_6 = PhotoImage(file=r"./logos/scissor right.png")


computer_label = Label(window, text="BOT", font=("Arial Bold", 30), bg='#226300')                           # BOT logo at left side
computer_label.place(x=130, y=180)
icon_1_label = Label(window, image=icon_1, bg='#226300')
icon_1_label.pack(side="left")


round_label = Label(window, text="    ", font=("Arial Bold", 22), fg="yellow", bg='#226300')                # displays 'Round X'
round_label.place(x=420, y=290)
ScoreBoard_label = Label(window, text=" BOT | YOU \n0   |   0", font=("Arial Bold", 20), fg="blue")         # displays Score Board
ScoreBoard_label.place(x=420, y=330)


result_msg_label = Label(window, text="", font=("Arial Bold", 15), fg="yellow", bg='#226300')               # displays match win / loss / draw
result_msg_label.place(x=370, y=420)


continue_btn = Button(window, text="", font=("Arial Bold", 10), width=20, bg='#226300')                     # after finishing match display "Click to continue ..." button 
continue_btn.place(x=310, y=700)    # initially disappeared button, y=700, which is edge of the game box 
# continue_btn.place(x=418, y=230)  <--- actual position of button


human_label = Label(window, text="YOU", font=("Arial Bold", 30), bg='#226300')                              # Human player logo at right side
human_label.place(x=775, y=180)
icon_2_label = Label(window, image=icon_2, bg='#226300')
icon_2_label.pack(side="right")


scissor_btn = Button(window, text="SCISSOR",font=("Arial Bold", 15), width=9)                               # Scissor, Paper and Rock button to choose manually
scissor_btn.place(x=330-14, y=600)
paper_btn = Button(window, text="PAPER",font=("Arial Bold", 15), width=9)
paper_btn.place(x=458-14, y=600)
rock_btn = Button(window, text="ROCK",font=("Arial Bold", 15), width=9)
rock_btn.place(x=585-14, y=600)


window.mainloop()
