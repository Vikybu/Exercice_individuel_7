import random

list_colors = ['blue', 'red', 'yellow', 'green', 'orange', 'violet', 'white', 'black']
result_guess = False
nb_try = 1
remaining_try = 12
code_length = 4

def generating_code():
    code = []
    for i in range(code_length):
        random_number = random.randint(0, 7)
        code.append(list_colors[random_number])
    return code


def colors_verification(nb_try):
    print(f'This is your {nb_try} guess')
    code_guess = []
    i=1
    while len(code_guess) < code_length:
        color = input(f'What color is in {i} place ? ')
        if color not in ['blue', 'red', 'yellow', 'green', 'orange', 'violet', 'white', 'black']:
            print('Please choose the following colors : blue, red, yellow, or green.')
        else:
            code_guess.append(color)
            i += 1
    return code_guess



def code_verification(code, code_guess):
    print(code)
    print(code_guess)
    for i in range(code_length):
        if code[i] == code_guess[i]:
            print(f'Place {i+1} : correct')           
        else : 
            print(f'Place {i+1} : wrong')
    return code == code_guess
    


def end_game(code, result_guess, nb_try, remaining_try):
    while result_guess != True:
        for i in range(remaining_try, 0, -1):
            remaining_try -= 1
            if remaining_try >0: 
                print(f'This code is wrong, please try again. You have {remaining_try} tries left.')
                nb_try = nb_try + 1
                code_guess = colors_verification(nb_try)
                result_guess = code_verification(code, code_guess)
                if result_guess == True:
                    break
            else:
                print('You have no tries left. You lost you looser !')
    print(f"Well done ! You've cracked the code in {nb_try} tries!")


def main():
    code = generating_code()
    code_guess = colors_verification(nb_try)
    result_guess = code_verification(code, code_guess)
    end_game(code, result_guess, nb_try, remaining_try)

main()