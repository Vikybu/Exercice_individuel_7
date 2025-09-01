import tkinter
import random

list_colors = ['blue', 'red', 'yellow', 'green', 'orange', 'violet', 'grey', 'brown']
code_length = 4
current_index = {"value": 0}
count = 0

def draw_game():
    start_row = 15
    list_button = []
    for colors in range(len(list_colors)):
        list_button.append(tkinter.Button(root, text=list_colors[colors], bg=list_colors[colors], font=('Arial', 12), width=5, height=1, command=lambda a=list_colors[colors]: click_color(a)))
    for i in range(4):
        for j in range(2):
            list_button[(2*i) + j].grid(row= start_row + j, column=i)

    button_start = tkinter.Button(root, text = 'Start the game', font=('Arial', 12), command=generating_code)
    button_start.grid(row = 18, column=0)

    button_validation = tkinter.Button(root, text = 'Verify the combinaison', font=('Arial', 12), command=code_verification)
    button_validation.grid(row = 18, column=1)



def generating_code():
    code = []
    for i in range(code_length):
        random_number = random.randint(0, 7)
        code.append(list_colors[random_number])
    print(code)
    return code



def create_empty_table():
    rows, cols = 12, 4
    start_row = 3
    cells = []
    for j in range(rows):
        row_cells = []
        for i in range(cols):
            lbl = tkinter.Label(root, text="", width=5, height=1, relief="solid")
            lbl.grid(row=start_row + j, column=i, padx=5, pady=5)
            row_cells.append(lbl)
        cells.append(row_cells)
    return cells



def click_color(a):
    global count
    if count <4:

        count += 1
        
        print(count)
        rows, cols = 12, 4
        total_cells = rows*cols
        index = current_index["value"]

        if index < total_cells:
            r = index //cols
            c = index % cols
            table[r][c]['bg'] = a
            current_index["value"] += 1
    
    return table

        
def code_verification():
    for i in range(code_length):
        if code[i] == table[i]:
            text = tkinter.Text("Correct" )   
            text.pack() 
        else : 
            text = tkinter.Text("Wrong" ) 
            text.pack()    
    return code == table

# Stockages


#creer la fenetre du jeu
root = tkinter.Tk()

root.title('Mastermind')
root.minsize(500, 800)
draw_game()
table = create_empty_table()
code = generating_code()
root.mainloop()

