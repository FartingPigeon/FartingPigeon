import random

print("I am a ship engine!")
print("(press enter to continue)")
input()
print("Enter a list of boys names, and a list of girls names and let me do all the work!")
input()

def boys():
    boy_names = []
    print("Please enter up to 10 boy names, if you have less than 10, enter 'Done' to end the list")

    Boy1 = input("Boy 1: ")
    if Boy1 == "Done" or Boy1 == "done":
        print("You have to enter at least 1 name for this to work")

    Boy2 = input("Boy 2: ")
    if Boy2 == "Done" or Boy2 == "done":
        boy_names = [Boy1]
        return boy_names
    
    Boy3 = input("Boy 3: ")
    if Boy3 == "Done" or Boy3 == "done":
        boy_names = [Boy1, Boy2]
        return boy_names 

    Boy4 = input("Boy 4: ")
    if Boy4 == "Done" or Boy4 == "done":
        boy_names = [Boy1, Boy2, Boy3]
        return boy_names

    Boy5 = input("Boy 5: ")
    if Boy5 == "Done" or Boy5 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4]
        return boy_names

    Boy6 = input("Boy 6: ")
    if Boy6 == "Done" or Boy6 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5]
        return boy_names 

    Boy7 = input("Boy 7: ")
    if Boy7 == "Done" or Boy7 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5, Boy6]
        return boy_names

    Boy8 = input("Boy 8: ")
    if Boy8 == "Done" or Boy8 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5, Boy6, Boy7]
        return boy_names

    Boy9 = input("Boy 9: ")
    if Boy9 == "Done" or Boy9 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5, Boy6, Boy7, Boy8]
        return boy_names

    Boy10 = input("Boy 10: ")
    if Boy10 == "Done" or Boy10 == "done":
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5, Boy6, Boy7, Boy8, Boy9]       
    else:
        boy_names = [Boy1, Boy2, Boy3, Boy4, Boy5, Boy6, Boy7, Boy8, Boy9, Boy10]
        return boy_names
            
boy_names = boys()
print(boy_names)
boy_len = len(boy_names)
input()



    
def girls():
    girl_names = []
    print("Please enter up to 10 Girl names, if you have less than 10, enter 'Done' to end the list")

    Girl1 = input("Girl 1: ")
    if Girl1 == "Done" or Girl1 == "done":
        print("You have to enter at least 1 name for this to work")

    Girl2 = input("Girl 2: ")
    if Girl2 == "Done" or Girl2 == "done":
        girl_names = [Girl1]
        return girl_names
    
    Girl3 = input("Girl 3: ")
    if Girl3 == "Done" or Girl3 == "done":
        girl_names = [Girl1, Girl2]
        return girl_names 

    Boy4 = input("Girl 4: ")
    if Boy4 == "Done" or Boy4 == "done":
        girl_names = [Girl1, Girl2, Girl3]
        return girl_names

    Boy5 = input("Girl 5: ")
    if Boy5 == "Done" or Boy5 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4]
        return girl_names

    Boy6 = input("Girl 6: ")
    if Boy6 == "Done" or Boy6 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5]
        return girl_names 

    Boy7 = input("Girl 7: ")
    if Boy7 == "Done" or Boy7 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5, Boy6]
        return girl_names

    Girl8 = input("Girl8: ")
    if Girl8 == "Done" or Girl8 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5, Boy6, Boy7]
        return girl_names

    Girl9 = input("Girl 9: ")
    if Girl9 == "Done" or Girl9 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5, Boy6, Boy7, Girl8]
        return girl_names

    Girl10 = input("Girl 10: ")
    if Girl10 == "Done" or Girl10 == "done":
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5, Boy6, Boy7, Girl8, Girl9]     

    else:
        girl_names = [Girl1, Girl2, Girl3, Boy4, Boy5, Boy6, Boy7, Girl8, Girl9, Girl10]
        return girl_names
            
girl_names = girls()
print(girl_names)
girl_len = len(girl_names)
input() 


def ship():
    global boy_len, girl_len
    ran_boy_num = (random.randint(0,boy_len -1))
    ran_boy = (boy_names[ran_boy_num])
    
    ran_girl_num = (random.randint(0,girl_len -1))
    ran_girl = (girl_names[ran_girl_num])

    print("Imagine " + ran_boy + " and " + ran_girl + " were together")


def LesShip():
    global girl_len
    ran_girl_num1 = (random.randint(0,girl_len -1))
    ran_girl_num2 = (random.randint(0,girl_len -1))

    while ran_girl_num1 == ran_girl_num2:
        ran_girl_num2 = (random.randint(0,girl_len -1))
        if ran_girl_num2 != ran_girl_num2:
            break

    ran_girl1 = (girl_names[ran_girl_num1])
    ran_girl2 = (girl_names[ran_girl_num2]) 
    print("Imagine " + ran_girl1 + " and " + ran_girl2 + " were together")

def GayShip():
    global girl_len
    ran_boy_num1 = (random.randint(0,boy_len -1))
    ran_boy_num2 = (random.randint(0,boy_len -1))

    while ran_boy_num1 == ran_boy_num2:
        ran_boy_num2 = (random.randint(0,boy_len -1))
        if ran_boy_num2 != ran_boy_num2:
            break

    ran_boy1 = (boy_names[ran_boy_num1])
    ran_boy2 = (boy_names[ran_boy_num2]) 
    print("Imagine " + ran_boy1 + " and " + ran_boy2 + " were together")


def RandomShip():
    ran_num = (random.randint(1,3))
    if ran_num == 1:
        ship()
    elif ran_num == 2:
        LesShip()
    elif ran_num == 3:
        GayShip()

def repeat(ship_func):
    print("Press enter for another one, tpye 'switch' to change what type of ship you want, and type 'done' to stop")
    while True:
        ans = input()
        if ans.lower() == 'switch':
            Ask()
        if ans.lower() == 'done':
            break
        ship_func()


def Ask():
    ans2 = input("Would you like a straight couple, lesbian couple, gay couple, or random? (S, L, G, R)")
    if ans2.lower() == 's':
       repeat(ship)
       ship()
       

    elif ans2.lower() == 'l':
        LesShip()
        repeat(LesShip)

    elif ans2.lower() == 'g':
        GayShip()
        repeat(GayShip)

    elif ans2.lower() == 'r':
        RandomShip()
        repeat(RandomShip)
Ask()





    



