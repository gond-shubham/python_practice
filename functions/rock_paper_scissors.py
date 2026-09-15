def system_generate():
    L=['rock', 'paper', 'scissor']
    import random
    a=random.randint(0,2)
    return L[a]

def user_input():
    print("select any one rock/paper/scissor ")
    opt = input("enter :")
    return opt

def game():
    system_points =0
    user_points = 0
    n= int(input("enter the no of rounds:"))
    i =0
    while i <n:
        system = system_generate()
        user= user_input()
        if user == 'rock':
            if system == 'paper':
                system_points+=1
            else:
                user_points += 1
            i += 1
        elif user == 'paper' :
            if system == 'scissor':
                system_points += 1
            else:
                user_points += 1
            i += 1
        elif user == 'scissor':
            if system == 'rock':
                system_points += 1
            else:
                user_points += 1
            i += 1
        else:
            print("invalid input")
            continue
    return (system_points, user_points)


def r_p_s():
    a,b = game()
    if a>b:
        print(f'the system won the match with {a} points')
    else:
        print(f'the user won the match with {b} points')

r_p_s()











