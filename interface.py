import tkinter
import random

list_colors = ['blue', 'red', 'yellow', 'green', 'orange', 'violet', 'grey', 'brown']
code_length = 4
current_index = {"value": 0}
attempt = 1
count = 0
click = 1
table = []
feedback_table = []
code = []


def draw_game():
    global game_frame
    game_frame = tkinter.Frame(root)
    game_frame.pack(pady=20)

    button_frame = tkinter.Frame(game_frame)
    button_frame.grid(row=0, column=9, rowspan=10, padx=20) 

    list_button = []
    for idx, color in enumerate(list_colors):
        b = tkinter.Button(button_frame, text=color, bg=color, font=('Arial', 12),
                           width=5, height=1, command=lambda a=color: click_color(a))
        b.grid(row=idx//2, column=idx%2, padx=2, pady=2)
        list_button.append(b)

    control_frame = tkinter.Frame(game_frame)
    control_frame.grid(row=10, column=9, columnspan=4, pady=10)

    button_validation = tkinter.Button(control_frame, text='Verify', font=('Arial', 12), command=code_verification)
    button_validation.grid(row=10, column=9, padx=10)


def generating_code():
    code = []
    for i in range(code_length):
        random_number = random.randint(0, 7)
        code.append(list_colors[random_number])
    print(code)
    return code

def create_empty_table():
    rows, cols = 12, code_length
    main_cells, feedback_cells = [], []

    for j in range(rows):
        row_cells, fb_row = [], []
        for i in range(cols):
            lbl = tkinter.Label(game_frame, text="", width=5, height=2, relief="solid", bg="white")
            lbl.grid(row=j, column=i, padx=5, pady=5)
            row_cells.append(lbl)
        main_cells.append(row_cells)

        for k in range(cols):
            fb = tkinter.Label(game_frame, text="", width=2, height=1, relief="solid", bg="lightgrey")
            fb.grid(row=j, column=cols + k, padx=2, pady=5)
            fb_row.append(fb)
        feedback_cells.append(fb_row)

    return main_cells, feedback_cells


def add_a_row(position):
    new_row = []
    for col in range(4):
        lbl = tkinter.Label(root, text="", width=5, height=2, relief="solid", bg="white")
        lbl.grid(row=position -1, column=col, padx=5, pady=5)  # 👈 position fixe
        new_row.append(lbl)

    table.append(new_row)  # 👈 on ajoute seulement à la fin



def click_color(a):
    global count
    if count < code_length:
        table[click][count]['bg'] = a
        count += 1

        
def code_verification():
    global count, click, attempt
    print(attempt)
    if attempt <= 12:
        guess = [table[click][i].cget("bg") for i in range(code_length)]
        print(guess)

        tmp_code = code.copy()
        tmp_guess = guess.copy()
        feedback = []

        for i in range(code_length):
            if tmp_guess[i] == tmp_code[i]:
                feedback.append("black")
            elif tmp_guess[i] and tmp_guess[i] in tmp_code:
                feedback.append("grey")
                tmp_code[tmp_code.index(tmp_guess[i])] = None
            else:
                feedback.append("white")

        for i, color in enumerate(feedback):
            feedback_table[click][i]['bg'] = color
        
        if feedback == ['black','black', 'black', 'black']:
            win_the_game()

        if attempt == 12 and feedback != ['black','black', 'black', 'black'] :
            loose_the_game()

        click += 1
        count = 0
        attempt += 1

    else:
        loose_the_game()

def win_the_game():
    global end_game_frame, attempt
    game_frame.destroy()

    end_game_frame = tkinter.Frame(root)
    end_game_frame.pack(pady=10)

    txt = tkinter.Text(end_game_frame, font="Arial 20", wrap="word", width=30, height=1)
    txt.pack()
    txt.insert("1.0", "Well done! You cracked the code !\n")

    button_restart = tkinter.Button(end_game_frame, text='Restart the game', font=('Arial', 12), command=restart_the_game)
    button_restart.pack(pady=10)

    attempt = 0


def loose_the_game():
    global end_game_frame, attempt
    game_frame.destroy()

    end_game_frame = tkinter.Frame(root)
    end_game_frame.pack(pady=10)

    txt = tkinter.Text(end_game_frame, font="Arial 20", wrap="word", width=35, height=1)
    txt.pack()
    txt.insert("1.0", "You didn't cracked the code you Loosers !\n")

    button_restart = tkinter.Button(end_game_frame, text='Restart the game', font=('Arial', 12), command=restart_the_game)
    button_restart.pack(pady=10)

    attempt = 0

def restart_the_game():
    global table, feedback_table, code, click, count
    click = 0
    count = 0

    end_game_frame.destroy() 

    draw_game()
    table, feedback_table = create_empty_table()
    code = generating_code()



def begin_the_game():
    global table, feedback_table, code, click, count
    click = 0
    count = 0

    welcome_frame.destroy()

    draw_game()
    table, feedback_table = create_empty_table()
    code = generating_code()



# créer la fenêtre
root = tkinter.Tk()
root.title('Mastermind')
root.minsize(800, 800)

welcome_frame = tkinter.Frame(root)
welcome_frame.pack(pady=20)

txt = tkinter.Text(welcome_frame, font="Arial 13", wrap="word", width=80, height=15)
txt.pack()
txt.insert("1.0", "Welcome to Mastermind!\n")
txt.insert("2.0", "A 4-colour code has been randomly generated.\n")
txt.insert("3.0", "The goal is to guess the secret code generated at the start of the game.\n")
txt.insert("4.0", "The code is created randomly by the computer and is composed of 4 colors.\n")
txt.insert("5.0", "You must crack the code in a maximum of 12 attempts. Please note: colours can be used more than once...\n")
txt.insert("6.0", "After each guess, feedback is provided : \n")
txt.insert("7.0", "- A black circle means a correct color in the correct position. \n")
txt.insert("8.0", "- A grey circle means a correct color but in the wrong position \n")
txt.insert("9.0", "- A grey circle means means that color does not appear in the code \n")

button_start = tkinter.Button(welcome_frame, text='Start the game', font=('Arial', 12), command=begin_the_game)
button_start.pack(pady=10)

root.mainloop()

