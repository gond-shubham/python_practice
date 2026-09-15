def game_level():
    while True:
        print("choose the game level 'easy/medium/hard' ")
        level = input("enter the game level: ")
        if level in ["easy", "hard", "medium"]:
            return level
        else:
            print("enter the valid type")


def number_generator():
    option = game_level()
    import random
    match option:
        case "easy":
            return random.randint(1,10)
        case "medium":
            return random.randint(1,20)
        case "hard":
            return random.randint(1,30)

def number_guessing():
    num = int(input("Guess the number: "))
    return num

def guessing_logic():
    generated_num = number_generator()

    while True:
        guessing_num = number_guessing()
        if generated_num > guessing_num:
            print("Too low")
        elif generated_num< guessing_num:
            print("Too high")
        else:
            print(f'the number {guessing_num} is corret')
            break
    return

guessing_logic()



