"""
Name: Arushan Arulraj, Krish Shah
Program: MarioGame.py
Description: This code is a re-create of mario odyssey that uses a variety of multiple
choice questions, battles, and other minigames to travel through kingdoms and obtain power
moons so that the user could complete the game.
"""


import os
from time import sleep
import time 
import random
import math

# Used for bolding, colouring, and underlining words later in the code 

class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   UNDER = '\x1B[4m'
   RED = '\033[91m'
   GREEN = '\033[92m'
   

# This variable stores all of the items the user collects throughout the game 
inventory = []

# Running this function will start the game 
def full_game():
    
    # Title screen of the game 
    def game_intro():
        for i in range(5):
            print("")
            print("")
            print("")
            print("  _____                         __  __            _      ")
            print(" / ____|                       |  \/  |          (_)      ")
            print("| (___  _   _ _ __   ___ _ __  | \  / | __ _ _ __ _  ___  ")
            print(" \___ \| | | | '_ \ / _ \ '__| | |\/| |/ _` | '__| |/ _ \  ")
            print(" ____) | |_| | |_) |  __/ |    | |  | | (_| | |  | | (_) | ")
            print("|_____/ \__,_| .__/ \___|_|    |_|  |_|\__,_|_|  |_|\___/  ")
            print("             | |                                         ")
            print("             |_|                                          ")
            print("")
            print("")
            print("  ____      _                          ")
            print(" / __ \    | |                         ")
            print("| |  | | __| |_   _ ___ ___  ___ _   _ ")
            print("| |  | |/ _` | | | / __/ __|/ _ \ | | |")
            print("| |__| | (_| | |_| \__ \__ \  __/ |_| |")
            print(" \____/ \__,_|\__, |___/___/\___|\__, |")
            print("               __/ |              __/ |")
            print("              |___/              |___/")
            print("")
            print("")
            print("")
            print("")
            print("                     ██ ██ ██ ██    ██ ██ ██   ") 
            print("               ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ")
            print("         ██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ")
            print("         ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ░░ ░░ ██") 
            print("      ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ░░ ██ ")
            print("      ██ ▓▓ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██   ") 
            print("   ██ ██ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ ")
            print("   ██ ░░ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ ")
            print("██ ░░ ░░ ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ ")
            print("██ ░░ ░░ ░░ ██ ░░ ░░ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ ")
            print("   ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ░░ ░░ ██ ██ ██   ") 
            print("   ██ ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ██ ▓▓ ██    ")
            print("      ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ▓▓ ██   ") 
            print("   ░░ ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ▓▓ ██       ")
            print("   ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ██          ")
            print("██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██          ")
            print("██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██          ")
            print("██ ██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ██ ██ ██    ")
            print("   ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██    ")
            print("      ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ██ ")
            print("   ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ██ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ▓▓ ▓▓ ██ ██ ██ ██ ██          ██ ▓▓ ▓▓ ██ ██ ")
            print("██ ▓▓ ▓▓ ██ ██                      ██ ██ ██    ")
            print("   ██ ██                                       ")
            
            time.sleep(.75)
            os.system("clear")
            print("")
            print("")
            print("")
            print("  _____                         __  __            _         ")
            print(" / ____|                       |  \/  |          (_)        ")
            print("| (___  _   _ _ __   ___ _ __  | \  / | __ _ _ __ _  ___   ")
            print(" \___ \| | | | '_ \ / _ \ '__| | |\/| |/ _` | '__| |/ _ \  ")
            print(" ____) | |_| | |_) |  __/ |    | |  | | (_| | |  | | (_) | ")
            print("|_____/ \__,_| .__/ \___|_|    |_|  |_|\__,_|_|  |_|\___/   ")
            print("             | |                                            ")
            print("             |_|                                             ")
            print("")
            print("")
            print("  ____      _                          ")
            print(" / __ \    | |                         ")
            print("| |  | | __| |_   _ ___ ___  ___ _   _ ")
            print("| |  | |/ _` | | | / __/ __|/ _ \ | | |")
            print("| |__| | (_| | |_| \__ \__ \  __/ |_| |")
            print(" \____/ \__,_|\__, |___/___/\___|\__, |")
            print("               __/ |              __/ |")
            print("              |___/              |___/")
            
            print("                     ██ ██ ██ ██    ██ ██ ██   ") 
            print("               ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ")
            print("         ██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ")
            print("         ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ░░ ░░ ██") 
            print("      ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ░░ ██ ")
            print("      ██ ▓▓ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ██ ██ ██   ") 
            print("   ██ ██ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ ")
            print("   ██ ░░ ██ ██ ░░ ░░ ░░ ██ ░░ ██ ░░ ██ ▓▓ ▓▓ ██ ")
            print("██ ░░ ░░ ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ ")
            print("██ ░░ ░░ ░░ ██ ░░ ░░ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ██ ")
            print("   ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ░░ ░░ ██ ██ ██   ") 
            print("   ██ ██ ░░ ░░ ░░ ░░ ██ ██ ██ ██ ██ ▓▓ ██    ")
            print("      ██ ██ ██ ░░ ░░ ░░ ░░ ░░ ██ ▓▓ ▓▓ ██   ") 
            print("   ░░ ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ▓▓ ██       ")
            print("   ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ██ ░░ ░░ ░░ ██ ██          ")
            print("██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██          ")
            print("██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ░░ ░░ ██          ")
            print("██ ██ ██ ▓▓ ▓▓ ▓▓ ▓▓ ██ ░░ ░░ ░░ ██ ██ ██ ██    ")
            print("   ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██    ")
            print("      ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ██ ")
            print("   ██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ██ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ▓▓ ▓▓ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▓▓ ▓▓ ▓▓ ██ ")
            print("██ ▓▓ ▓▓ ██ ██ ██ ██ ██          ██ ▓▓ ▓▓ ██ ██ ")
            print("██ ▓▓ ▓▓ ██ ██                      ██ ██ ██    ")
            print("   ██ ██                                       ")
        
            time.sleep(.75)
            os.system("clear")
    
    # Short description explaining the context of this game
    def description():
        print("Welcome to the remake of Super Mario Odyssey. This game has the similar concept to the real Super Mario Odyssey game but the challenges within the games are very different. The main objective is to save princess peach from bowser, who kidnapped her. ")
        time.sleep(8)
        os.system("clear")
        print()
        print("Before we begin, choose your character!")
        time.sleep(2)
    
    # Lets the user choose their charecter between Mario or Luigi
    def mario_luigi():
        
        print(color.RED +"             ▄████▄▄" + color.END    +   color.GREEN +  "                                     ▄████▄▄ " + color.END)
        print("              ▀█▀▐└─┐                                    ▄▀█▀▐└─┐ ")
        print("             █▄▐▌▄█▄┘                                    █▄▐▌▄█▄┘")        
        print("             └▄▄▄▄─┘                                     └▄▄▄▄─┘ ")   
        print("          ▄███▒██▒███▄                                ▄██████████▄")        
        print("          ▒▒█▄▒▒▒▒▄█▒▒                                ▒▒█▄████▄█▒▒")             
        print("            ▒▒▒▀▀▒▒▒                                    ███▀▀███ ")
        print("          ▄███────███▄                                ▄███────███▄")
        print()
        
        morl = input("Would you like to play as " + color.RED + "Mario" + color.END + " or " + color.GREEN + "Luigi" + color.END + "? (Press Enter to Leave): ").lower()
        # This if statement will run if the user types mario
        if morl == "mario":
            print()
            print("You selected to play as" + color.RED + " Mario!" + color.END)
            print("Let's Get Started!")
            inventory.append("Mario")
            time.sleep(2)
            os.system("clear")
            cap_kingdom()
        # This elif statement will run if the user types luigi    
        elif morl == "luigi":
            print()
            print("You selected to play as" + color.GREEN + " Luigi!" + color.END)
            print("Let's Get Started!")
            inventory.append("Luigi")
            time.sleep(2)
            os.system("clear")
            cap_kingdom()
        # If the user enters nothing, the game will end 
        elif morl == "":
            print()
            print("Thanks for playing! Goodbye!")
            gameover()
        
        # Invalid input will result in asking the user the character question again 
        else:
            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
            print()
            while True:
                morl = input("Would you like to play as " + color.RED + "Mario" + color.END + " or " + color.GREEN + "Luigi" + color.END + "? (Press Enter to Leave): ").lower()
                # Game will begin if user types mario
                if morl == "mario":
                    print()
                    print("You selected to play as" + color.RED + " Mario!" + color.END)
                    print("Let's Get Started!")
                    inventory.append("Mario")
                    time.sleep(4)
                    os.system("clear")
                    cap_kingdom()
                    break
                # Game will begin if user types luigi
                elif morl == "luigi":
                    print()
                    print("You selected to play as" + color.GREEN + " Luigi!" + color.END)
                    print("Let's Get Started!")
                    inventory.append("Luigi")
                    time.sleep(4)
                    os.system("clear")
                    cap_kingdom()
                    break
                
                elif morl == "":
                    print()
                    print("Thanks for playing! Goodbye!")
                    gameover()
                    break
                # Invalid input until user enters a valid phrase
                else:
                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                    print()
                    continue
    # This function takes the user to the first kingdom        
    def cap_kingdom():
        # A list of all the possible math questions that can be asked later to the user
        math1 = ["(49+20)/3", "3*2 + 18", "(43-8)*2", "(4^2) + 36", "18-2+15", "23*3+17", "(98-3)/5", "20+39+21",]
        math2 = ["7*2 +8", "48-35 + 6", "23 + 4 -16"]
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Cap Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        
        print("          ╓▄▄▄     " )
        print("           ╠▓▓▓▓U,          ")
        print("    ,╓╦╦    ▒╢╣╢╣▓▓,         ")      
        print("     ░░▒▒▒╢╢▓╣╫▓▓▓▓╢╢▓@╖     ")
        print("    .╟╣╣▓▓▓╣╢╢╢╢▓╣╣╢╣╣╣@   ")
        print("     ░▒▓█▀▀███▓█████▓╣╣╢╣░  ")
        print("     ░▓█▒▒╢╣╢███▒▒▒▒█▌╣▒▒   ")
        print("     ░▓▌▒▒▓▀▓██▓╬▒▒▒▓▌╣▒  ")
        print("    ░▒█▓╫▓█▓████▓▒▒█▒╣░   ")
        print("    ▒▒╢╢▓███▓▓▓██▓██▓▓▒     ")
        print("  ░ ░░▒▒▒▒▒▀▀▀▀▓▓▓▓▓▓▓▓▓▒,,   ")
        print("    `╙▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣╝╜    ")
        print("         `╙╨╝╝╜╙╙`        ")
        
        print()
        print(color.BOLD + "Welcome to Cap Kingdom! The Kingdom of Many Hats." + color.END)
        time.sleep(1.5)
        print()
        print(color.BOLD +"Cappy: " +color.END+ "Hello! My name is Cappy and I am the leader here in Cap Kingdom.")
        time.sleep(5)
        nickname = input(color.BOLD +"Cappy: " + color.END + "What is your name? ")
        inventory.append(nickname)
        print(color.BOLD + "Cappy: " + color.END + "Okay, "  + nickname + ". I heard about your adventure to defeat Bowser and I am willing to help!")
        time.sleep(5)
        print(color.BOLD + "Cappy: " + color.END + "There is one circumstance though. If you beat me in a quick battle, I will join you in your journey. If you do not, I will not come with you as I will need to protect my kingdom. ")
        time.sleep(9)
        os.system("clear")
        time.sleep(2)
        
        print(" ____        _   _   _   ")   
        print("| __ )  __ _| |_| |_| | ___")
        print("|  _ \ / _` | __| __| |/ _ \ ")
        print("| |_) | (_| | |_| |_| |  __/")
        print("|____/ \__,_|\__|\__|_|\___|")
        print()
        time.sleep(2)
        print(color.BOLD + inventory[0] + "("+ inventory[1] +")" + " vs. " + "Cappy" + color.END)
        
        # Used to select a random question from the previous list to the user
        number1 = random.randrange(0,8)
        number2 = random.randrange(0,3)
        print()
        time.sleep(2)
        # This input statement will ask the user the question
        mathquestion1 = input(color.BOLD + "QUESTION 1: " + color.END + "What does " + math1[number1] + " equal to? ")
        
        # This if statement will run if the user gets the answer correct
        if mathquestion1 == "23" or mathquestion1 == "24" or mathquestion1 == "70" or mathquestion1 == "52" or mathquestion1 == "31" or mathquestion1 == "86" or mathquestion1 == "19" or mathquestion1 == "80":
            print("Correct!")
            print("You did " + color.BOLD + str(random.randrange(30,50)) + color.END + " HP worth of damage to Cappy!")
            print()
            
            print("Cappy tried to punch you but he missed! You remain healthy.")
            print()
            mathquestion2 = input(color.BOLD + "QUESTION 2: " + color.END + "What does " + math2[number2] + " equal to? ")
            # This if statement will run if the user gets the second answer correct
            if mathquestion2 == "22" or mathquestion2 == "19" or mathquestion2 == "11":
                print("Correct!")
                print("You did " + color.BOLD + str(random.randrange(70,90)) + color.END + " HP worth of damage to Cappy!")
                print()
                print(color.BOLD + "Congratulations! You Beat Cappy!" + color.END)
                print()
                print(color.BOLD + "Cappy:" + color.END+ " Good Fight! Since you beat me, I will be joining you on your adventure to defeat Bowser.")
                inventory.append("Cappy")
                print()
                time.sleep(10)
                os.system("clear")
                
                print(color.BOLD + "Cappy:" + color.END + "Hey " + nickname + "! Look at what is over here. It's the odyssey. We can use it to travel." )
                print()
                time.sleep(3)
                print(color.BOLD + "Cappy: " + color.END + "Oh No! It's broken.")
                print()
                # This while loop will constantly ask the user to type the word "repair" until they type it correctly
                while True:
                    repair = input("Type" + color.BOLD + " Repair " + color.END + "To Fix the Odyssey!: ").lower()
                    if repair == "repair":
                        print()
                        print(color.BOLD + "The Odyssey is now repaired! " + color.END)
                        time.sleep(2)
                        print()
                        # Gives the user the choice of going to Cascade Kingdom or Sand Kingdom 
                        while True:
                            cascadeorsand = input(color.BOLD + "Cappy: " + color.END + "Which Kingdom would you like to go to now? (Cascade Kingdom or Sand Kingdom): ").lower()
                            # Send the user to Cascade Kingdom
                            if cascadeorsand == "cascade" or cascadeorsand == "cascade kingdom":
                                cascade_kingdom()
                                break
                            # Sends the user to Sand Kingdom
                            elif cascadeorsand == "sand" or cascadeorsand == "sand kingdom":
                                sand_kingdom()
                                break
                            # Invalid Input. Will ask question again. 
                            else:
                                print(color.BOLD + "Invalid Input, Try Again!" + color.END)
                                print()    
                                continue
                        
                        break
                    else:
                        print(color.BOLD + "Try Again!" + color.END)
                        print()
                        continue
            # This else statement will run if the user gets the second question wrong       
            else:
                print()
                print("Incorrect!")
                print("Cappy hit you with his special move. You lost!")
                print("You will continue this game without Cappy.")
                inventory.append("No Cappy")
                print()
                print(color.BOLD + "Cappy:" + color.END + " Sorry, " + nickname + " , I will not be joining you on your adventure but I wish you the best of luck.")
                print()
                time.sleep(7)
                os.system("clear")
                print("Walking.....")
                time.sleep(2)
                print("You discovered the Odyssey! The Odyssey is a ship that helps you travel anywhere!")
                # This while loop will constantly ask the user to repair the odyssey until it is repaired
                while True:
                    repair = input("It's broken. Type" + color.BOLD + " Repair " + color.END + "to fix it: ").lower()
                    if repair == "repair":
                            print()
                            print(color.BOLD + "The Odyssey is now repaired! " + color.END)
                            print()
                            time.sleep(2)
                            while True:
                                cascadeorsand = input("Which Kingdom would you like to go to now? (Cascade Kingdom or Sand Kingdom): ").lower()
                                if cascadeorsand == "cascade" or cascadeorsand == "cascade kingdom":
                                    cascade_kingdom()
                                    break
                                elif cascadeorsand == "sand" or cascadeorsand == "sand kingdom":
                                    sand_kingdom()
                                    break
                                else:
                                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                    print()
                                    continue
                            break
                    else:
                        print(color.BOLD + "Try Again!" + color.END)
                        print()
                        continue
        # This else statment will run if the user gets the first math questions wrong
        else:
            print("Incorrect!")
            print("Cappy hit you with his special move. You lost!")
            print("You will continue this game without Cappy.")
            print()
            inventory.append("No Cappy")
            print(color.BOLD + "Cappy:" + color.END + " Sorry," + nickname + ", I will not be joining you on your adventure but I wish you the best of luck.")
            print()
            time.sleep(7)
            os.system("clear")
            print("Walking.....")
            time.sleep(2)
            print("You discovered the Odyssey! The Odyssey is a ship that helps you travel anywhere!")
             # This while loop will constantly ask the user to repair the odyssey until it is repaired
            while True:
                repair = input("It's broken. Type" + color.BOLD + " Repair" + color.END + " to fix it: ").lower()
                if repair == "repair":
                            print()
                            print(color.BOLD + "The Odyssey is now repaired! " + color.END)
                            print()
                            time.sleep(2)
                            while True:
                                cascadeorsand = input("Which Kingdom would you like to go to now? (Cascade Kingdom or Sand Kingdom): ").lower()
                                # Sends user to Cascade Kingdom
                                if cascadeorsand == "cascade" or cascadeorsand == "cascade kingdom":
                                    cascade_kingdom()
                                    break
                                # Sends user to Sand Kingdom
                                elif cascadeorsand == "sand" or cascadeorsand == "sand kingdom":
                                    sand_kingdom()
                                    break
                                # Invalid Input. Asks question again.
                                else:
                                    print(color.BOLD + "Invalid Input! Try Again!" + color.END)
                                    print()
                                    continue
                            break
                else:
                    print(color.BOLD + "Try Again!" + color.END)
                    print()
                    continue
            
            
    # This function will run cascade kingdom 
    def cascade_kingdom():
        os.system("clear")
        inventory.append("cascade")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Cascade Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        
        print("           ████████")
        print("          ███▄███████")
        print("          ███████████")
        print("          ███████████")
        print("          ██████")
        print("          █████████")
        print("█       ███████")
        print("██    ████████████")
        print("███  ██████████  █")
        print("███████████████")
        print("███████████████")
        print(" █████████████")
        print("  ███████████")
        print("    ████████")
        print("     ███  ██")
        print("     ██    █")
        print("     █     █")
        print("     ██    ██")
        print()
        # List of multiple choice questions that can be asked later on 
        cascadequestion = ["What is the strongest dinosaur?\n T-Rex\n Velociraptor\n Allosaurus\n Spinosaurus\n ", "What was the main reason dinosaurs went extinct?\n Old Age\n Asteroids\n Starvation\n Diseases\n ", "What is the name of dinosauer themed blockbuster movie?\n Dinosaur World\n Land of Dinosaurs\n Jurassic Park\n T-Rex and Friends\n ", "What is the name of the Toronto-based NBA basketball team involving a dinosaur?\n Toronto Grizzlies\n Toronto Birds\n Toronto T-REX\n Toronto Raptors\n ", "What is the term used to refer to meat eating dinosaurus?\n Carnivore\n Herbivore\n Omnivore\n Dinoivore\n " ]
        # Randomizing the list of multiple choice questions 
        cascademc = random.randrange(0,5)
        print(color.BOLD + "Welcome to Cascade Kingdom!" + color.END)
        print()
        time.sleep(2)
        print(color.BOLD + "There's a power moon near the dinosaur!" + color.END)
        time.sleep(2)
        print()
        print("Answer the following question correctly to acquire the power moon without waking up the dinosaur!")
        print()
        time.sleep(1.5)
        # Asks the user a random mutliple choice question from the list
        cascademcquestion = input(cascadequestion[cascademc]).lower()
        # Runs if answer correct and user gains power moon
        if cascademcquestion == "t-rex" or cascademcquestion == "asteroids" or cascademcquestion == "jurassic park" or cascademcquestion == "toronto raptors" or cascademcquestion == "carnivore":
            print()
            print("Correct! Great Job.")
            time.sleep(2)
            print(color.BOLD + color.RED + inventory[1] + " has acquired the Cascade Kingdom Power Moon!" + color.END + color.END)
            inventory.append("Cascade moon")
        # Runs is answer incorrect
        else:
            print()
            print(color.BOLD + "Incorrect! You didn't acquire the Cascade Kingdom Power moon." + color.END)
            inventory.append("no Cascade moon")
        
        time.sleep(4)
        os.system("clear")
        time.sleep(2)
        
        
        print(" ,,,╓╥▄╖▄▄m╖")
        print("  ,╦▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▓╢▓▓▓@╖,")
        print("  ▄▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▄")
        print("  ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒")
        print(" '█▓██████████▓▓▓▓▓▓▓▓▓▒▒╣╣▓▓▓▓▒[")
        print("▀███████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒╣")
        print(" ▀███████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("   ▀███████████▓▓▓▓▓▓▓▓▓▓▓▓Ç")
        print(" ]▓▓█████████████████▓███████╫═")
        print("  ╜▀█▀▀▀█████████████████▀▀")
        
        time.sleep(2)
        print()
        print("There's a huge boulder blocking your way to the next kingdom!")
        time.sleep(1.5)
        print()
        # Asks user to decode message 
        decodecascade = input("Guess the offset to decode the following message:" + color.BOLD + " MRPE" + color.END + " (Hint: The offset is between 1-5): ")
        # If user is correct, runs this if statement
        if decodecascade == "3":
            print()
            time.sleep(2)
            print("Correct! You pushed the boulder off the cliff!")
            time.sleep(1.5)
            print("The decoded word was Push. ")
            time.sleep(1.5)
            print(color.BOLD + "MRPE --> SHIFT EACH LETTER BY 3 LETTERS --> PUSH" + color.END)
            print()
            time.sleep(2)
            print(color.BOLD + "Onto the next kingdom!" +color.END)
            time.sleep(2)
            # If user completed cascade and sand kingdom, this if statement sends them to snow kingdom
            if "sand" in inventory and "cascade" in inventory:
                snow_kingdom()
           # If user only completed cascade kingdom, sends user to sand kingdom         
            else:
                sand_kingdom()
        # Gives user 2 more tries to guess the correct offset number        
        else:
            count = 2
            while count != 0:
                print(color.BOLD + "Incorrect. You can try again!" + color.END)
                print()
                print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                decodecascade = input("Guess the offset to decode the following message:" + color.BOLD + " HSKN" + color.END + " (Hint: The offset is between 1-5): ")
                if decodecascade == "3":
                    print()
                    time.sleep(1.5)
                    print("Correct! You pushed the boulder off the cliff!")
                    time.sleep(1.5)
                    print("The decoded word was Push. ")
                    time.sleep(1.5)
                    print(color.BOLD + "MRPE --> SHIFT EACH LETTER BY 3 LETTERS --> PUSH" + color.END)
                    print()
                    time.sleep(2)
                    print(color.BOLD + "Onto the next kingdom!" + color.END)
                    time.sleep(3)
                    
                    if "sand" in inventory and "cascade" in inventory:
                        snow_kingdom()
                        break
                    else:
                        sand_kingdom()
                        break            
                else:
                    count = count - 1
                    continue
            # User ran out of tries
            if count == 0:
                print()
                print(color.BOLD + "You lost!" + color.END)
                inventory.remove("cascade")
                if "Cascade moon" in inventory:
                    inventory.remove("Cascade moon")
                else:
                    inventory.remove("no Cascade moon")
                print(color.BOLD + "You died trying to move the boulder!" + color.END)
                print()
                # Asks user if they want to retry cascade kingdom
                cascaderetry = input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                # User will retry cascade kingdom if they enter "yes"
                if cascaderetry == "yes":
                    cascade_kingdom()
                # Exits the game if user enters "no"    
                elif cascaderetry == "no":
                    print()
                    print("Thanks for playing! Goodbye!")
                    gameover()
                    
                # If user's response is invalid, the questions will be asked again
                else:
                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                    print()
                    # This while loop will make sure the user's answer is valid
                    while True:
                        cascaderetry = input("Would you like to play again? Type Yes or No: ").lower()
                        
                        if cascaderetry == "yes":
                            cascade_kingdom()
                            break
                        
                        elif cascaderetry == "no":
                            print()
                            print("Thanks for playing! Goodbye!")
                            gameover()
                            break
                        
                        else:
                            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                            print()
                            continue
    # This function will play Sand kingdom
    def sand_kingdom():
        os.system("clear")
        inventory.append("sand")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Sand Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        
        print("        ,╓╗╥╥╗╗╖╖╖╖,, ╓╖╥╖╥,            ")
        print("    ╓╢╢▒▒▒▒▒▒▒▒▒╢▒╣╢╣╢▒▒▒╢@           ")
        print("    ╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣╬╣▒╢╣╢╢╢ÑH╖       ")
        print("      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣╢╢▓W,   ")
        print("       ▓▓▓▓████▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓╣╫▓╖ ")
        print("       '████▒█▀█▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓m")
        print("          ▀█╢█▄▌▓▐█▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        print("             ▓▒▒▓█▓▀█▀▀╢▓▓╣▓▓╫█▓▓██▓▓▓▓ ")
        print("             ╚╢╫╢╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▀  ")
        print("    ▄▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▀▀▀▀▀'     ")
        print("▓▓▓▓▓▓╗╓╖╢▒▒╢▓╢▓▓▓▓▓▓▓▓▓▓▓██▓╗,        ")
        print("▀▓▓▓▓▓╬╣▓▓▓╟▓▓╣╫╣╣╣╫▓▓╣▓▓▌╢▓░▒╫╣╟╣▓,   ")
        print("    `╙`╙▓▓▓▓▓╫▓▓▓▓▓▓▒▒▓▓╣╫╣╣╣╣╣▓   ")
        print("    ╓╓,║║▓▓▓▓▀▓Ñ▒▄███╜  ▀▓▓▓▀    ")
        print("  ▓▓▓▓▓▓██▓▓`  ▓▀▀▓▓▓           ")
        print("              ╚▓█▓█▓▀  ")
       
        print()
        # List of all the multiple choice questions for sand kingdom
        sandquestions = ["What Animals Are Typically Found in Sandy Deserts?\n Camels\n Cats\n Eagles\n Roosters\n ", "Which continent has the biggest desert?\n Asia\n Europe\n Antartica\n Australia \n ", "What is the name of the common green plant found in sandy deserts?\n Sunflowers\n Cactus\n Tulips\n Grass\n ", "Where is the biggest Sand Desert Located?\n Australia\n Saudi Arabia\n USA\n Spain \n ", "Which US City is situated in a desert?\n New York City\n Tampa Bay\n Chicago\n Las Vegas\n "]
        # Randomizes the multiple choice questions
        sandmc = random.randrange(0,5)
        print(color.BOLD + "Tostarenan:" + color.END + " Welcome to the Sand Kingdom " + inventory[1] + "! ")
        time.sleep(2)
        print()
        print(color.BOLD + "There's a power moon stuck in the sand! Answer this question to acquire it!" + color.END)
        print()
        time.sleep(1.5)
        # Asks the multiple choice question
        sandmcquestion = input(sandquestions[sandmc]).lower()
        # if user's answer is correct, user obtains power moon
        if sandmcquestion == "camels" or sandmcquestion == "antartica" or sandmcquestion == "cactus" or sandmcquestion == "saudi arabia" or sandmcquestion == "las vegas":
            print()
            print("Correct! Great Job.")
            time.sleep(2)
            print(color.BOLD + color.RED + inventory[1] + " has acquired the Sand Kingdom Power Moon!" + color.END + color.END)
            inventory.append("Sand moon")
        # If user's answer is wrong, user does not get power moon
        else:
            print()
            print(color.BOLD + "Incorrect! You didn't acquire the Sand Kingdom Power moon." + color.END)
            inventory.append("no Sand moon")
        time.sleep(4)
        os.system("clear")
        time.sleep(2)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⠋⠉⠀⠀⠀⠀⠈⠙⣷⡶⠖⠄⠀⠀⠀⠀⠀")    
        print("⠀⠀⠀⢀⣤⣶⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⣼⠟⢿⡄⠀⠀⠀⠀⠀⠀")    
        print("⠀⠀⠀⠀⠀⢰⡟⠀⢈⠻⢷⡄⡆⠀⡆⠀⡸⠯⢄⠀⢻⡄⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀ ⣠⠟⠀⡰⠁⠀⢀⣽⣾⣤⣷⣾⣦⠀⠀⠑⡀⢻⣄⠀⠀⠀⠀")    
        print("⠀⠀⠀⢀⣴⠋⠀⠀⡇⠀⠀⠸⠿⠃⠀⠇⠙⠋⠀⠀⠀⡇⠀⠙⢷⣄⠀⠀")
        print("⠀ ⣰⠟⠁⠀⠀⠀⢇⠀⠀⠀⠀⡼⠀⠘⡄⠀⠀⠀⢀⠇⠀⠀⠀⠙⢧⡀")        
        print("⠀⢸⠃⠀⠀⠀⢀⣀⠈⠓⠠⠐⠋⠀⠀⠀⠈⠑⠒⠒⠉⠀⣠⡄⠀⠀⠀⢻")
        print("⠀⢿⠀⠀⠀⠀⣆⢈⣣⠤⠤⠖⠒⠒⠒⠒⠒⠒⠲⠶⠤⠾⣀⣆⠀⠀⢀⡼")
        print(" ⠘⢷⣤⣀⣈⣉⣀⣤⣤⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⢤⣤⣤⣤⣤⠶⠛⠁")
        print("  ⢀⣠⡤⠼⢯⣥⣄⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀")
        print("⣼⠋⣀⣀⣀⣀⡀⠈⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣤⣤⣄⣀⡀⠀⠀")
        print("⢿⡎⠔⡡⠊⡠⠊⡱⢄⠀⠀⢹⣄⡀⠀⠀⢀⣀⣴⠟⠁⠀⠀⠀⠉⠻⡆⠀")
        print("⠈⠳⣤⣀⠈⠀⠊⠠⠊⠃⣀⣼⠏⠉⠉⠉⠉⠙⢧⣄⡀⠀⠀⠀⣀⣴⠇⠀")
        print("⠀    ⠉⠛⠛⠓⠒⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠋⠉⠀⠀⠀")
        
        time.sleep(2)
        print(color.BOLD + "Tostarenan: " + color.END + inventory[1] + ", I need your help! This goomba is attacking me. Please kill it!")
        print()
        time.sleep(2)
        # Asks the user to decode the message by finding the offset
        decodesand = input("Guess the offset to decode the following message:" + color.BOLD + " HSKN" + color.END + " (Hint: The offset is between 1-5): ")
        # If user correct, run if statement
        if decodesand == "2":
            print()
            time.sleep(2)
            print("Correct! The goomba has been killed and you saved Tostarenan.")
            time.sleep(1.5)
            print("The decoded word was Jump. ")
            time.sleep(1.5)
            print(color.BOLD + "HSKN --> SHIFT EACH LETTER BY 2 LETTERS --> JUMP" + color.END)
            print()
            time.sleep(2)
            print(color.BOLD + "Onto the next kingdom!" +color.END)
            time.sleep(2)
            # Send user to snow kingdom if they have completed cascade and sand
            if "sand" in inventory and "cascade" in inventory:
                snow_kingdom()
            # Send user to cascade kingdom      
            else:
                cascade_kingdom()
        # If user is wrong, they have two tries left
        else:
            count = 2
            while count != 0:
                print(color.BOLD + "Incorrect. You can try again!" + color.END)
                print()
                print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                decodesand = input("Guess the offset to decode the following message:" + color.BOLD + " HSKN" + color.END + " (Hint: The offset is between 1-5): ")
                if decodesand == "2":
                    print()
                    time.sleep(1.5)
                    print("Correct! The goomba has been killed and you saved Tostarenan.")
                    time.sleep(1.5)
                    print("The decoded word was Jump. ")
                    time.sleep(1.5)
                    print(color.BOLD + "HSKN --> SHIFT EACH LETTER BY 2 LETTERS --> JUMP" + color.END)
                    print()
                    time.sleep(2)
                    print(color.BOLD + "Onto the next kingdom!" + color.END)
                    time.sleep(3)
                    # Send user to snow kingdom if they have ocmpleted cascade and sand kingdom
                    if "sand" in inventory and "cascade" in inventory:
                        snow_kingdom()
                        break
                    # send user to cascade kingdom
                    else:
                        cascade_kingdom()
                        break            
                else:
                    count = count - 1
                    continue
            # User has 0 tries left
            if count == 0:
                print()
                print(color.BOLD + "You lost!" + color.END)
                inventory.remove("sand")
                if "Sand moon" in inventory:
                    inventory.remove("Sand moon")
                else:
                    inventory.remove("no Sand moon")
                print(color.BOLD + "You died trying to fight the goomba!" + color.END)
                print()
                # Asks if they want to play again
                sandretry = input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                # if they want to play again, send user to sand kingdom
                if sandretry == "yes":
                    sand_kingdom()
                    
                # If they dont want to play again, end game
                elif sandretry == "no":
                    print()
                    print("Thanks for playing! Goodbye!")
                    gameover()
                # If invalid, ask question again
                else:
                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                    print()
                    while True:
                        sandretry = input("Would you like to play again? Type Yes or No: ").lower()
                        
                        if sandretry == "yes":
                            sand_kingdom()
                            break
                        elif sandretry == "no":
                            print()
                            print("Thanks for playing! Goodbye!")
                            gameover()
                            break
                        
                        else:
                            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                            print()
                            continue
    # Function for snow kingdom 
    def snow_kingdom():
        os.system("clear")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Snow Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        inventory.append("snow")
        time.sleep(2)
        print("                                        ██████████                                      ")
        print("                                    ████          ████                                  ")
        print("                                  ██      ▒▒▒▒▒▒      ██                                ")
        print("                                ██      ▒▒▒▒▒▒▒▒▒▒      ██                              ")
        print("                                ██      ▒▒▒▒▒▒▒▒▒▒        ██                            ")
        print("                              ██▒▒▒▒      ▒▒▒▒▒▒        ▒▒▒▒██                          ")
        print("                              ██▒▒▒▒                    ▒▒▒▒██                          ")
        print("                              ██▒▒      ████████        ▒▒▒▒██                          ")
        print("                              ██    ██████░░░░██████      ▒▒██                          ")
        print("                              ██  ██░░░░██░░░░██░░░░██      ██                          ")
        print("                                ████░░░░██░░░░██░░░░░░██  ██                            ")
        print("                                  ██░░░░░░░░░░░░░░░░░░██  ██                            ")
        print("                                  ██░░░░████████░░░░░░████                              ")
        print("                                    ██░░░░░░░░░░░░░░████                                ")
        print("                                    ████████████████████                                ")
        print("                                  ████▓▓██░░░░██▓▓██░░░░██                              ")
        print("                               ██░░██▓▓██░░░░██▓▓▓▓██░░░░██                             ")
        print("                              ██░░██▓▓██░░░░░░██▓▓▓▓██░░░░██                            ")
        print("                              ██░░██▓▓██████████▓▓▓▓▓▓██░░░░██                          ")
        print("                              ██░░██▓▓██        ██▓▓▓▓██░░░░██                          ")
        print("                                ██████    ██      ██████████                            ")
        print("                                    ██      ██        ██                                ")
        print("                                   ██▓▓▓▓▓▓████▓▓▓▓██████                                ")
        print("                               ██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                                ")
        
        time.sleep(2)
        print()
        if "Cappy" in inventory:
            print(color.BOLD + "Cappy: " + color.END +"Hey look! I think I see someone standing in the snow!")
        else:
            print("You notice someone familiar standing in the snow...")
            
        print("It's Captain Toad!")
        print()
        time.sleep(3)
        print(color.BOLD +"Captain Toad: " +color.END + "Hey "  + inventory[1] + "! How are you doing! ")
        print()
        time.sleep(3)
        print(color.BOLD + "Captain Toad: " + color.END + "I hear you are searching for power moons.")
        print()
        time.sleep(3)
        print(color.BOLD + "Captain Toad: " + color.END + "I would love to help you on your journey, but the thing is I am also looking for power moons.")
        print()
        time.sleep(3)
        print(color.BOLD + "Captain Toad: " + color.END + "You know what, lets make a bet, if you can answer my question correctly, I will give you my power moon, if not, you will give me one of your power moons.")
        print()
        time.sleep(3)
        print(color.BOLD + "Captain Toad: " + color.END + "Lets begin...")
        time.sleep(4)
        os.system("clear")
        time.sleep(2)
        # If cappy is in the inventory, proceed the code
        if "Cappy" in inventory:
            print(color.BOLD + "Captain Toad: " + color.END + "TRUE or FALSE, The Arctic is not considered a desert...")
            time.sleep(2)
            print()
            print(color.BOLD + "Cappy: " + color.END + "Psstt...")
            time.sleep(2)
            print()
            # Asks user if they want hint
            print(inventory[1] + "... Do you want a hint? ")
            YorN = input("Yes or No...").lower()
            # If yes, cappy will give user hint
            if YorN == "yes":
                print()
                print(color.BOLD + "Cappy: " + color.END + "Okay.. Just know that a desert is land with extreme temperatures and low vegetation. ")
                time.sleep(2)
            # If no, the game will continue without you getting a hint from cappy
            else:
                print("You continued with no hint from cappy...")
                print()
                time.sleep(2)
        # True or False question being asked to user
        TorF=input(color.BOLD + "Captain Toad: "+ color.END + "TRUE or FALSE, The Arctic is NOT considered a desert...").lower()
        # While loop for question
        while True:    
            # if user says false, run if statement 
            if TorF == "false" or TorF == "f":
                print()
                print(color.BOLD + "Captain Toad: " + color.END+ "That is correct")
                print()
                time.sleep(2)
                print("Here is your power moon for getting the answer correct.")
                time.sleep(2)
                print(color.BOLD + color.RED + inventory[1] + " has acquired the Snow Kingdom Power Moon!" + color.END + color.END)
                inventory.append("Snow moon")
                time.sleep(2)
                print()
                print(color.BOLD + "Onto the next kingdom!" + color.END)
                time.sleep(2)
                metro_kingdom()
                break
            # If user says true, run else statement
            else:
                print(color.BOLD + "Captain Toad: " + color.END + "That is incorrect...")
                print()
                time.sleep(2)
                print(color.BOLD + "Captain Toad: " + color.END + "I will be taking your power moon away which will send you back to the most previous kingdom you completed...")
                print()
                time.sleep(2)
                inventory.append("no Snow moon")
                inventory.remove("snow")
                print("Goodbye for now..and good luck!")
                # Sends user to most recent kingdom they visisted 
                if inventory.index("sand") > inventory.index("cascade"):
                    inventory.remove("sand")
                    if "Sand moon" in inventory:
                        inventory.remove("Sand moon")
                    else:
                        inventory.remove("no Sand moon")
                    sand_kingdom()
                    break
                else: 
                    inventory.remove("cascade")
                    if "Cascade moon" in inventory:
                        inventory.remove("Cascade moon")
                    else:
                        inventory.remove("no Cascade moon")
                    cascade_kingdom()
                    break
                
    # This function will run metro kingdom
    def metro_kingdom():
        os.system("clear")
        inventory.append("metro")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Metro Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⣤⡶⠶⠶⠦⣤⣤⣤⣤⣤⣴⡄⠀⠀⠀⠀⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⢀⣠⣤⣴⣶⣤⣤⡀⢈⡉⠛⠻⠿⠀⠀⠀⠀⢸⣿⣿⣷⠀⣀⠻⠇⠀⠀")
        print("⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⢰⣿⣷⣦⠀⠀")
        print("⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣿⣿⣄⠀⠀⠀⠀⠀⣸⣿⠏⠀⠛⣉⣉⠁⠀⠀")
        print("⢠⡄⠠⢤⣤⣤⡤⠤⠤⠄⠸⣿⣿⣿⣿⣶⣶⣶⡾⠟⠁⣠⠖⣧⣤⡿⢿⡄⠀")
        print("⠀⢸⣷⠶⣤⡤⢤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡶⢿⣤⠷⣾⡇⠀")
        print("⠀ ⠙⢷⣿⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⣿⡾⠛⠀⠀")
        print()
        print(color.BOLD + "Welcome to Metro Kingdom also known as the big city!" + color.END)
        print()
        time.sleep(3)
        
        print(color.BOLD + inventory[1] + color.END + ": Wow! There's so much traffic on the road! How am I going to cross through this safely?")
        print()
        time.sleep(2)
        # Ask the user to decode the message 
        print(" ABCDEFGHIJKLMNOPQRSTUVWXYZ- Use this as a reference for the next question.")
        print()
        time.sleep(1.5)
        metrodecode = input("Shift each letter in the phrase 'BCDCYR' by an offset of 2. Type the new decoded word: ").lower()
        print()
        print()
        # If user decodes correctly, proceed and gain metro kingdom moon
        if metrodecode == "defeat":
            print()
            print("Correct! Great Job!")
            print(color.BOLD + "Keep this word in mind for the future. " + color.END)
            time.sleep(1)
            print("You safely crossed the road without getting hit by any cars!")
            time.sleep(3)
            print(color.BOLD + color.RED + inventory[1] + " has acquired the Metro Kingdom Power Moon!" + color.END + color.END)
            time.sleep(3)
            inventory.append("Metro moon")
        
        # User is incorrect and does not get the metro kingdom moon
        else:
            print()
            time.sleep(1)
            print(color.BOLD + "Incorrect! You didn't acquire the Metro Kingdom Power moon." + color.END)
            print("The word was 'defeat'. Please keep this word in mind for the future.")
            time.sleep(2)
            print("You were too scared to cross the road!")
            inventory.append("no Metro moon")
            time.sleep(6)
            
        os.system("clear")
        time.sleep(1)
        print("              ,")
        print("     __  _.-` `'-.")
        print("    /||\._ __{}_( ")
        print("    ||||  |'--.__/")
        print("    |  L.(   ^_\^")
        print("    \ .-' |   _ |")
        print("    | |   )\___/")
        print("    |  \-'`:._]")
        print("    \__/;      '-.")
        print("    |   |o     __ \ ")
        print("    |   |o     )( |")
        print("    |   |o     \/ /")
        
        print()
        print("Looks like the police is following you.....")
        time.sleep(1.5)
        print(color.BOLD + "Police: " + color.END + "Hey Sir! You seem a bit suspicious...")
        time.sleep(2)
        # Computer asks questions to user 
        policename = input(color.BOLD + "Police: " + color.END + "Can I get your name? ")
        time.sleep(1.5)
        policeage = input(color.BOLD + "Police: " + color.END + "Can I get your age? ")
        time.sleep(1.5)
        policerov = input(color.BOLD + "Police: " + color.END + "Can I get your reason for visit please? ")
        time.sleep(3)
        print(color.BOLD + "Police: " +color.END +"Alright " + policename + ". Sorry for the misunderstanding but you are all good to go now!")
        time.sleep(2)
        print()
        print(color.BOLD + inventory[1] + color.END + ": That was a close one. Whew!")
        time.sleep(2)
        os.system("clear")
        time.sleep(1)
        print()
        print(color.BOLD + "You discovered a note!" + color.END)
        print()
        time.sleep(2)
        print("The note reads....")
        time.sleep(2)
        print()
        print("Dear " + inventory[0] + ", ...")
        time.sleep(1)
        print("It's me Princess Peach. I miss you so much. ")
        time.sleep(3)
        print("Bowser's taking me somewhere far. I am not sure where. ")
        time.sleep(3)
        print("Maybe to his home? Please come save me. I dropped this note in the city hoping you will find it and come help me.")
        time.sleep(3)
        print("Bowser's our biggest yemne. ")
        time.sleep(3)
        print("Love.... Princess Peach,")
        print()
        
        print(color.BOLD + inventory[1] + color.END + ": Yemne? What is that supposed to mean?")
        print()
        time.sleep(2)
        if "Cappy" in inventory:
            print("Cappy wants to help you unscramble the word! ")
            print(color.BOLD + "Cappy:" + color.END + " The opposite of the word is 'friend'. ")
            print()
            # Asks the user to unscramble the word 
            unscramble = input("Unscramble the following word - 'Yemne': ").lower()
            # If user is correct, proceed
            if unscramble == "enemy":
                print(color.BOLD + "Correct! Keep this word in mind for the future" + color.END)
                time.sleep(1.5)
                print()
                # Asks user which kingdom they want to visit  
                while True:
                    seasideorlunch = input("Which kingdom would you like to go to next? - Seaside Kingdom or Luncheon Kingdom?: ").lower()
                # Sends user to seaside kingdom
                
                    if seasideorlunch == "seaside" or seasideorlunch == "seaside kingdom":
                        seaside_kingdom()
                        break
                    # Sends user to luncheon kingdom
                    elif seasideorlunch == "luncheon" or seasideorlunch == "luncheon kingdom":
                        luncheon_kingdom()
                        break
                    # Invalid input, asks the user again
                    else:
                        print(color.BOLD + "Invalid Input, Try Again" +  color.END)
                        print()
                        continue
            else:
                # Tells user that they have 2 tries left
                count = 2
                while count != 0:
                    print(color.BOLD + "Incorrect. You can try again!" + color.END)
                    print()
                    print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                    unscramble = input("Unscramble the following word - 'Yemne': ").lower()
                    if unscramble == "enemy":
                        print(color.BOLD + "Correct! Keep this word in mind for the future" + color.END)
                        time.sleep(1.5)
                        print()
                        while True:
                            seasideorlunch = input("Which kingdom would you like to go to next? - Seaside Kingdom or Luncheon Kingdom?: ").lower()
                            if seasideorlunch == "seaside" or seasideorlunch == "seaside kingdom":
                                seaside_kingdom()
                                break
                    
                            elif seasideorlunch == "luncheon" or seasideorlunch == "luncheon kingdom":
                                luncheon_kingdom()
                                break
                        
                            else:
                                print(color.BOLD + "Invalid Input! Try Again!" + color.END)
                                print()
                                continue
                        break
                         
                    else:
                        count = count - 1
                        continue
                # Proceed if user has 0 tries left
                if count == 0:
                    print() 
                    print(color.BOLD + "You lost!" + color.END)
                    inventory.remove("metro")
                    if "Metro moon" in inventory:
                        inventory.remove("Metro moon")
                    else:
                        inventory.remove("no Metro moon")
                    print()
                    # Ask the user if they want to retry this kingdom 
                    metroretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                    if metroretry == "yes":
                        metro_kingdom()
                    # This will run if user does not want to retry     
                    elif metroretry == "no":
                        print()
                        print("Thanks for playing! Goodbye!")
                        gameover()
                    # Tell the user that input is invalid and will re-ask the question 
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        #Ask user if they want to play again
                        while True:
                            metroretry = input("Would you like to play again? Type Yes or No: ").lower()
                            # Sends user to the top of this function again
                            if metroretry == "yes":
                                metro_kingdom()
                                break
                            # Elif statment sends user to the gomeover function 
                            elif metroretry == "no":
                                print()
                                print("Thanks for playing! Goodbye!")
                                gameover()
                                break
                            
                            # Tells the user their input is invalid 
                            else:
                                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                print()
                                continue
        
        # Asks the user to unscramble the code 
        else:
            unscramble = input("Unscramble the following word - 'Yemne': ").lower()
            if unscramble == "enemy":
                print(color.BOLD + "Correct! Keep this word in mind for the future" + color.END)
                time.sleep(1.5)
                # Ask the user which kingdom they want to go to 
                while True:
                    seasideorlunch = input("Which kingdom would you like to go to next? - Seaside Kingdom or Luncheon Kingdom?: ").lower()
                    print()
                    # Sends the user to seaside kingdom
                    if seasideorlunch == "seaside" or seasideorlunch == "seaside kingdom":
                        seaside_kingdom()
                        break
                    
                    # Sends the user to luncheon kingdom
                    elif seasideorlunch == "luncheon" or seasideorlunch == "luncheon kingdom":
                        luncheon_kingdom()
                        break
                    
                    # Invalid Input. Asks user again. 
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        continue
            # Tells user they have 2 tries left 
            else:
                count = 2
                # This while loop will lowers the number of tries the user has everytime a invalid statment is made 
                while count != 0:
                    print(color.BOLD + "Incorrect. You can try again!" + color.END)
                    print()
                    print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                    unscramble = input("Unscramble the following word - 'Yemne': ").lower()
                    # This will run if user enters enemy 
                    if unscramble == "enemy":
                        print(color.BOLD + "Correct! Keep this word in mind for the future" + color.END)
                        time.sleep(1.5)
                        print()
                        # Asks the user which kingdom they want to go to 
                        while True:
                            seasideorlunch = input("Which kingdom would you like to go to next? - Seaside Kingdom or Luncheon Kingdom?: ").lower()
                            # This will send user to seaside kingdom 
                            if seasideorlunch == "seaside" or seasideorlunch == "seaside kingdom":
                                seaside_kingdom()
                                break
                                
                            # Sends user to luncheon kingdom
                            elif seasideorlunch == "luncheon" or seasideorlunch == "luncheon kingdom":
                                luncheon_kingdom()
                                break
                            # Invalid Input. Asks user again. 
                            else:
                                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                print()
                                continue
                        break
                         
                    else:
                        count = count - 1
                        continue
                # If runs out of attempts, run this if statement
                if count == 0:
                    print() 
                    print(color.BOLD + "You lost!" + color.END)
                    inventory.remove("metro")
                    if "Metro moon" in inventory:
                        inventory.remove("Metro moon")
                    else:
                        inventory.remove("no Metro moon")
                    print()
                    # Ask the user if they want to play again
                    metroretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                    # If user enters yes, run this statment
                    if metroretry == "yes":
                        metro_kingdom()
                    # If user enters no, send the user to the gameover function     
                    elif metroretry == "no":
                        print()
                        print("Thanks for playing! Goodbye!")
                        gameover()
        
                    # IF input is invalid, re-ask the question
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        # While loop will run until user enters a valid response 
                        while True:
                            metroretry = input("Would you like to play again? Type Yes or No: ").lower()
                            
                            if metroretry == "yes":
                                metro_kingdom()
                                break
                            
                            elif metroretry == "no":
                                print()
                                print("Thanks for playing! Goodbye!")
                                gameover()
                                break
                            
                            else:
                                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                print()
                                continue
                
    # This function will run seaside kingdom
    def seaside_kingdom():
        os.system("clear")
        inventory.append("seaside")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Seaside Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀")
        print("⠈⣿⣶⣤⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀")
        print("⠀⢹⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀")
        print("⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀")
        print("⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃")
        print("⢸⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀")
        print("⣿⣿⠿⠋⠁⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀")
        print("⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀ ⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print()
        print("Welcome to the Seaside Kingdom, the kingdom covered in water!")
        # List of multiple choice questions used in this kingdom 
        seasidequestions = ["What is the largest Ocean? \n Pacific\n Atlantic\n Arctic\n Indian \n ", "What is the name of the largest aquatic animal?\n Shark\n Goldfish\n Blue Whale\n Dolphin \n ", "How many oceans are there in the world?\n 2\n 5\n 10\n 6\n ", "What was the reason to the titanic's sinking?\n Weight\n Iceberg\n Sharks\nInexperienced Captain \n ", "Which species of fish is the fastest?\n Goldfish\n Clownfish\n Salmon\n Sailfish\n "]
        # Randomizes the multiple choice questions 
        seasidemc=random.randrange(0,5)       
        print()
        time.sleep(2)
        for x in range(0,5):
            b = "Swimming" + "." * x
            print(b,end="\r")
            time.sleep(0.5)
        print()
        print()
        print("There's a power moon under the water. Answer the following question to go down and get it!")
        print()
        time.sleep(1.5)
        # Asks the multiple choice questions to the user
        seasidemcquestion = input(seasidequestions[seasidemc]).lower()
        # This will run if user's answer is correct 
        if seasidemcquestion == "pacific" or seasidemcquestion == "blue whale" or seasidemcquestion == "5" or seasidemcquestion == "iceberg" or seasidemcquestion == "sailfish":
            print()
            print("Correct! Great Job.")
            time.sleep(2)
            print(color.BOLD + color.RED + inventory[1] + " has acquired the Seaside Kingdom Power Moon!" + color.END + color.END)
            inventory.append("Seaside moon")
    
        # This else statement will run if user's answer is incorrect 
        else:
            print()
            print(color.BOLD + "Incorrect! You didn't acquire the Seaside Kingdom Power moon." + color.END)
            inventory.append("no Seaside moon")
            
        
        time.sleep(4)
        os.system("clear")
        time.sleep(2)
        
        print(inventory[1] + ": I am getting tired from being in the water for so long!")
        time.sleep(2)
        print("Oh No! You are beginning to drown in the water!")
        print()
        # User will be asked to type breathe
        drown = input("Type 'Breathe' to save yourself from drowning!: ").lower()
        # If the user enters "", run this statement 
        if drown == "breathe":
            print()
            print("You saved yourself from drowning! You are back on land now.")
            time.sleep(2)
            print()
            print(inventory[1] + ": Whew! I am glad I survived.")
            
            print()
            # Ff user has cappy in their inventory, run this if statement 
            if "Cappy" in inventory:
                time.sleep(2)
                print(color.BOLD + "Answer this following riddle correctly to go to the next kingdom! " + color.END)
                print()
                time.sleep(2)
                print(color.BOLD + "Cappy: " + color.END + "I'll give you a hint. The answer is a species of fish.")
                time.sleep(1)
                # User will be asked the riddle question
                seasideriddle = input("What do you call a rich fish? ").lower()
                
                # If user enters goldfish, this if statement will run
                if seasideriddle == "goldfish":
                    print()
                    print(color.BOLD + "That is correct! Good job!" + color.END)
                    print()
                    print(color.BOLD + "Onto the next kingdom!" + color.END)
                    time.sleep(4)
                    # This will send the user to bowser's kingdom if they completed luncheon and seaside kingdoms
                    if "seaside" in inventory and "luncheon" in inventory:
                        bowser_kingdom()
                    # Sends user to luncheon kingdom
                    else:
                        luncheon_kingdom()
                # Tells user they have two attemps left
                else:
                    count = 2
                    # This while loop will run until the user has 0 attempts left
                    while count != 0:
                        print(color.BOLD + "Incorrect. You can try again!" + color.END)
                        print()
                        print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                        seasideriddle = input("What do you call a rich fish? ").lower()
                        # User answering correctly will run this if statement 
                        if seasideriddle == "goldfish":
                            print()
                            print(color.BOLD + "That is correct! Good Job!" + color.END)
                            time.sleep(1.5)
                            print()
                            print(color.BOLD + "Onto the next kingdom!" + color.END)
                            time.sleep(4)
                            # Sends user to bowser if requirments are met
                            if "seaside" in inventory and "luncheon" in inventory:
                                bowser_kingdom()
                            # Sends user to luncheon kingdom
                            else:
                                luncheon_kingdom()
                            
                            
                        else:
                            count = count - 1
                            print()
                            continue
                    # This will run if user ran out of tries
                    if count == 0:
                        print() 
                        print(color.BOLD + "You lost!" + color.END)
                        inventory.remove("seaside")
                        if "Seaside moon" in inventory:
                            inventory.remove("Seaside moon")
                        else:
                            inventory.remove("no Seaside moon")
                        print()
                        # User will be asked if they want to retry this kingdom
                        seasideretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                        # If user enters yes, seaside kingdom will restart
                        if seasideretry == "yes":
                            seaside_kingdom()
                        
                        # If user enters no, they will be sent to the gameover function 
                        elif seasideretry == "no":
                            print()
                            print("Thanks for playing! Goodbye!")
                            gameover()
                        
                        # Invalid input will result in the user being asked the question again
                        else:
                            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                            print()
                            # This while loop will make sure the user answers a valid input
                            while True:
                                seasideretry = input("Would you like to play again? Type Yes or No: ").lower()
                                
                                if seasideretry == "yes":
                                    seaside_kingdom()
                                    break
                                
                                elif seasideretry == "no":
                                    print()
                                    print("Thanks for playing! Goodbye!")
                                    gameover()
                                    break
                                
                                else:
                                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                    print()
                                    continue
            # Runs if user does not have cappy
            else:
                time.sleep(2)
                print(color.BOLD + "Answer this following riddle correctly to go to the next kingdom! " + color.END)
                print()
                time.sleep(2)
                # User will be asked this question
                seasideriddle = input("What do you call a rich fish? ").lower()
                # If user types goldfish, run this code
                if seasideriddle == "goldfish":
                    print()
                    print(color.BOLD + "That is correct! Good job!" + color.END)
                    print()
                    print(color.BOLD + "Onto the next kingdom!" + color.END)
                    time.sleep(4)
                    # Send user to bowser kingdom
                    if "seaside" in inventory and "luncheon" in inventory:
                        bowser_kingdom()
                    # Send user to luncheon kingdom
                    else:
                        luncheon_kingdom()
                
                # User has two attempts left
                else:
                    count = 2
                    # While loop will run until user has 0 attempts left 
                    while count != 0:
                        print(color.BOLD + "Incorrect. You can try again!" + color.END)
                        print()
                        print(color.BOLD + "You have " + str(count) + " tries left!" + color.END)
                        seasideriddle = input("What do you call a rich fish? ").lower()
                        if seasideriddle == "goldfish":
                            print()
                            print(color.BOLD + "That is correct! Good Job!" + color.END)
                            time.sleep(1.5)
                            print()
                            print(color.BOLD + "Onto the next kingdom!" + color.END)
                            time.sleep(4)
                            if "seaside" in inventory and "luncheon" in inventory:
                                bowser_kingdom()
                            else:
                                luncheon_kingdom()
                            
                            
                        else:
                            count = count - 1
                            print()
                            continue
                    # If user runs out of attempts, run this code
                    if count == 0:
                        print() 
                        print(color.BOLD + "You lost!" + color.END)
                        inventory.remove("seaside")
                        if "Seaside moon" in inventory:
                            inventory.remove("Seaside moon")
                        else:
                            inventory.remove("no Seaside moon")
                        print()
                        # Ask user if they want to play again
                        seasideretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                        # Send to seaside kingdom
                        if seasideretry == "yes":
                            seaside_kingdom()
                        # Send user to gameover function
                        elif seasideretry == "no":
                            print()
                            print("Thanks for playing! Goodbye!")
                            gameover()
                        # Tell user input is invalid 
                        else:
                            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                            print()
                            while True:
                                seasideretry = input("Would you like to play again? Type Yes or No: ").lower()
                                
                                if seasideretry == "yes":
                                    seaside_kingdom()
                                    break
                                
                                elif seasideretry == "no":
                                    print()
                                    print("Thanks for playing! Goodbye!")
                                    gameover()
                                    break
                                
                                else:
                                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                    print()
                                    continue
        
        
        
        # This will run if user is unable to type breathe
        else:
            print()
            print(color.BOLD + "You died from drowning in the water!" + color.END)
            print()
            inventory.remove("seaside")
            if "Seaside moon" in inventory:
                inventory.remove("Seaside moon")
            else:
                inventory.remove("no Seaside moon")
            # Asks the user if they want to retry seaside kingdom 
            seasideretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
            # User inputting yes will begin the seaside_kingdom function again
            if seasideretry == "yes":
                seaside_kingdom()
            # Inputting no will send the user to the gameover function         
            elif seasideretry == "no":
                print()
                print("Thanks for playing! Goodbye!")
                gameover()
            # Invalid input will ask the retry question again
            else:
                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                print()
                # While loop will run until user enters a valid response 
                while True:
                    seasideretry = input("Would you like to play again? Type Yes or No: ").lower()
                        
                    if seasideretry == "yes":
                        seaside_kingdom()
                        break
                    
                    elif seasideretry == "no":
                        print()
                        print("Thanks for playing! Goodbye!")
                        gameover()
                        break
                    
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        continue
    
    
    # This function will run luncheon kingdom
    def luncheon_kingdom():
        os.system("clear")
        inventory.append("luncheon")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Luncheon Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        
        print("⠀⠀⠀⡇⠀⣿⠀⢸⡇⠀⠀⠀⠀⢰⣿⡄⠀⠀⠀⠀⠀⢀⣴⣾⣿⣷⣦⠀⠀")
        print("⠀⠀ ⡇⠀⣿⠀⢸⡇⠀⠀⠀⠀⢸⣿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣇⠀⠀")
        print("⠀⠀ ⣇⣀⣿⣀⣸⡇⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀")
        print("⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⡆⠀⠀⠸⣿⣿⣿⣿⣿⣿⡿⠀⠀")
        print("⠀⠀ ⠿⣿⣿⣿⠿⠃⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠹⣿⣿⣿⣿⣿⠃⠀⠀")
        print("⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠈⢻⣿⡟⠁⠀⠀⠀")
        print("     ⢸⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀")
        print("⠀⠀   ⣾⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀⠀⠀")
        print("⠀⠀⠀  ⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀")
        print("⠀⠀⠀⠀ ⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀")
        print("⠀⠀⠀⠀ ⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀")
        print("⠀⠀⠀⠀ ⠻⣿⠟⠁⠀⠀⠀⠀⠀⠘⢿⡿⠃⠀⠀⠀⠀⠀⠈⠻⣿⠟⠀⠀⠀⠀")
        # List of all the possible multiple choice questions for luncheon kingdom
        lunchquestions = ["Which of the following is not a cooking utensil? \n Spoon \n Pressure Cooker \n Measuring Cup \n Knife \n", "How many Milliliters are in a Liter?\n 100ml \n 1000ml \n 10000ml \n 10ml \n ", "Select the incorrect cooking measuring unit. \n Tablespoon \n Teaspoon \n Cup \n Bowl \n", "Which of the following terms is incorrect to describe how meat is cooked? \n Rare \n Well done \n Excellent \n Medium Rare \n"]
        # Randomizes all the questions
        lunchmc = random.randrange(0,4)
        print()
        print("Welcome to Luncheon Kingdom, a Popular Destination for the Hungry.")
        print()
        time.sleep(2)
        print(color.BOLD + inventory[1] + color.END + ": This kingdom smells amazing!")
        print()
        time.sleep(3)
        print(color.BOLD + "Volbonan: " + color.END + "Hello " + inventory[1] + ", I am the gate keeper of this kingdom. I see that you are not from around here.")
        time.sleep(3)
        print()
        print(color.BOLD +  "Volbonan: " + color.END + "Answer the following question correctly if you want to proceeed on with your journey")
        # User will be asked a multiple choice question
        print()
        time.sleep(2)
        lunchmcquestions = input(lunchquestions[lunchmc]).lower()
        # If user inputs "yes", this if statement will run
        if lunchmcquestions == "pressure cooker" or lunchmcquestions == "1000ml" or lunchmcquestions == "bowl" or lunchmcquestions == "excellent":
            print()
            print("Correct! I will now let you pass.")
            time.sleep(2)
            os.system("clear")
            for x in range(0,5):
                b = "Walking" + "." * x
                print(b,end="\r")
                time.sleep(0.5)
            print()
            print("Cookatiel: QWACKKK")
            time.sleep(3)
            print()
            print(color.BOLD + inventory[1] + color.END + ": Oh no!! It is the Cookatiel, I heard that it is the biggest and deadlist bird in all of luncheon kingdom! ")
            time.sleep(4)
    
        # If user's input is incorrect, this else statement will run
        else:
            print()
            time.sleep(3)
            print(color.BOLD + "Volbonan: " + color.END + "Too bad! I guess you won't be able to continue your journey. You are stuck in this kingdom forever!!!")
            time.sleep(4)
            print()
            #This will ask the user if they want to retry Luncheon Kingdom until user enters valid response
            while True:
                luncheonretry = input("Would you like to retry luncheon kingdom?" + color.BOLD + " Yes or No " + color.END).lower()
                # If user inputs yes, they will retry luncheon kingdom
                if luncheonretry == "yes":
                    luncheon_kingdom()
                    break
                # If user inputs no, they will be sent to the gameover function 
                elif luncheonretry == "no":
                    print("Thanks for playing! Goodbye.")
                    gameover()
                    break
                # Invalid response will ask the user to type their answer again
                else:
                    print("Invalid Answer...Try again")
                    continue
            
            time.sleep(4)
            print(color.BOLD + "Volbonan: " + color.END + "Oh no!! It is the Cookatiel, the biggest and deadlist bird in all of luncheon kingdom! Do something " + inventory[1] + "!")
            time.sleep(6)
        
        os.system("clear")
        time.sleep(2)
        
        
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠋⢻⣷⣄⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⣤⣾⣿⣷⣿⣿⣿⣿⣿⣶⣾⣿⣿⠿⠿⠿⠶⠄")
        print("⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠈⣿⣿⣿⣿⣿⣿⠟⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⣼⣿⣿⣿⣿⣿⣿⣆⣤⠿⢶⣦⡀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        
        
        print()
        # If cappy is in the inventory of the user, this if ststament will run
        if "Cappy" in inventory: 
            print(inventory[1] + ": How are we going to defeat this bird?!")
            print()
            time.sleep(3)
            print(color.BOLD + "Cappy: " + color.END + "Hey I have an idea, try throwing me to onto it, I might be able to capture and control this bird!")
            print()
            time.sleep(3)
            # While loop will run until user enters a valid response
            while True:
                # Input statement asking user to type throw
                throwcap = input("Cappy: Type " + color.BOLD + "throw" + color.END +" so that I can control the Cookatiel: ").lower()
                # Inputting "throw" will alow this if statement to run and break the while loop
                if throwcap == "throw":
                    print()
                    time.sleep(3)
                    print(color.BOLD + "Cappy:" + color.END + "Good Job! I will take the bird away from here while you search for the power moon in this kingdom ")
                    print()
                    time.sleep(3)
                    break
                # Getting the answer incorrect will result in the user trying again
                else: 
                    print(color.BOLD + "Cappy: " + color.END + "You missed! Try again. ")
                    print()
                    time.sleep(2)
                    continue
                
        # Else statement will run if user does not have cappy 
        else: 
            print(color.BOLD + inventory[1] + color.END +  ": How am I going to defeat this bird?!")
            print()
            time.sleep(4)
            print(color.BOLD + "Volbonan: " + color.END + "Hey I have an idea, try distracting the bird by showing it this giant piece of steak.")
            print()
            time.sleep(4)
            
            # While loop will run until user enters a valid response
            while True: 
                # Input statement asking the user to type meat
                meat = input("Type " + color.BOLD + "'Meat'" + color.END + " to distract the Cookatiel: " ).lower()
                # If the user inputs meat, the code will run and the while loop will break
                if meat == "meat":
                    print(color.BOLD + "Volbonan: " + color.END + "Good job! The bird isn't trying to harm us anymore!")
                    break
                # Incorrect input will ask the user to try again
                else: 
                    print("Try again!")
                    print()
                    time.sleep(2)
                    continue
        
        time.sleep(4)
        print(color.BOLD + "Volbonan: " + color.END + "Thank you for getting rid of the Cookatiel and saving my life!")
        print()
        time.sleep(4)
        print(color.BOLD + "Volbonan: " + color.END + "As a reward, I will grant you the luncheon kingdom power moon if you can solve this riddle.")
        print()
        time.sleep(4)
        attempt = 3
        # Giving the user three attempts to solve this riddle
        for i in range(3):
            # Input ststament is asking the user the question
            foodriddle = input(color.BOLD + "Volbonan: " + color.END + "What kind of cup doesn't hold water? You have 3 attempts: ").lower()
            # If user's input is correct, the if statement will run
            if foodriddle == "cupcake":
                time.sleep(3)
                print()
                print(color.BOLD + "Volbonan: " + color.END + "That is correct!")
                print()
                time.sleep(3)
                print(color.BOLD + color.RED + inventory[1] + " has acquired the Luncheon Kingdom Power Moon!" + color.END + color.END)
                inventory.append("Luncheon moon")
                time.sleep(2)
                print(color.BOLD + "Onto the next Kingdom!" + color.END)
                # if user completed seaside and luncheon kingdom, send user to bowser's kingdom
                if "seaside" and "luncheon" in inventory:
                    bowser_kingdom()
                    break
        # Send user to seaside kingdom
                else:
                    seaside_kingdom()
                    break
            # If user's input is incorrect, they will lose a life and retry the question
            else:
                attempt = attempt - 1
                if attempt != 0:
                    print()
                    print(color.BOLD + "Try Again, you have " + str(attempt) + " attempts left." + color.END)
        # If the user ran out of attempts, this if ststament will run        
        if attempt == 0:
            inventory.remove("luncheon")
            time.sleep(3)
            print()
            print(color.BOLD + "Incorrect! You didn't acquire the Luncheon Kingdom Power moon." + color.END)
            print()
            time.sleep(2)
            print(color.BOLD + "You lost!" + color.END)
            time.sleep(2)
            print()
            while True:
                luncheonretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                if luncheonretry == "yes":
                    luncheon_kingdom()
                    break
                elif luncheonretry == "no":
                    print("Thanks for playing! Goodbye!")
                    gameover()
                    break
                else:
                    print(color.BOLD + "Invalid Input. Try again!" + color.END)
                    print()
                    continue
        
            
                
        
    
    # This function will send the user to bowser's kingdom
    def bowser_kingdom():
        os.system("clear")
        inventory.append("bowser")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Bowser's Kingdom" + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
            os.system("clear")
        time.sleep(1)
        print("───────▄█──────────█─────────█▄───────")
        print("─────▐██──────▄█──███──█▄─────██▌──────")
        print("────▐██▀─────█████████████────▀██▌────")
        print("───████────████████████████────████────")
        print("──▐█████──██████████████████──█████▌────")
        print("───████████████████████████████████────")
        print("────███████▀▀████████████▀▀███████────")
        print("─────█████▌──▄▄─▀████▀─▄▄──▐█████─────")
        print("───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───")
        print("──██████████████████████████████████──")
        print("─████████████████████████████████████─")
        print("▐██████──███████▀▄██▄▀███████──██████▌")
        print("▐█████────██████████████████────█████▌")
        print("▐█████─────██████▀──▀██████─────█████▌")
        print("─█████▄─────███────────███─────▄█████─")
        print("──██████─────█──────────█─────██████──")
        print("────█████────────────────────█████────")
        print("─────█████──────────────────█████─────")
        print("──────█████────────────────█████──────")
        print("───────████───▄────────▄───████───────")
        print("────────████─██────────██─████────────")
        print("────────████████─▄██▄─████████────────")
        print("───────████████████████████████───────")
        print("────────▀█████████▀▀█████████▀────────")
        print()
        
        time.sleep(2)
        # If Cappy is in the user's inventory, run the if statement
        if "Cappy" in inventory:
            print(color.BOLD + "Cappy: " + color.END + "We are finally here! We made it. It all comes down to this. ")
        
        # Run else statement if cappy is not in inventory
        else:
            print(color.BOLD + inventory[1] + color.END + ": I am finally here. I made it. It all comes down to this. ")
            
        time.sleep(5)
        print()
        os.system("clear")
        time.sleep(2)
        
        print("░░░░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░░░░░")
        print("░░░░░░░░░▄██▄▀░░░░░░░░░░░░▀▄██▄░░░░░░░░░")
        print("░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░░")
        print("░░░░░░░░░░█░▀██░░░░░░░░░░██▀░█░░░░░░░░░░")
        print("░░░░░░░░░█░░░▄██▄░░░░░░▄██▄░░░█░░░░░░░░░")
        print("░░░░░░░░▄▀░▄▀──▀█▄░░░░▄█▀──▀▄░▀▄░░░░░░░░")
        print("░░░░░░░▄▀░▄▀───▄─██░░██─▄───▀▄░▀▄░░░░░░░")
        print("░░░░░▄▀░░░█───███─█░░█─███───█░░░▀▄░░░░░")
        print("░░░▄▀░░░░░█────▀──█░░█──▀────█░░░░░▀▄░░░")
        print("░▄▀░░░░░░░█──────█░░░░█──────█░░░░░░░▀▄░")
        print("█░░░░░▄░░░░▀▄▄▄▄▀░░░░░░▀▄▄▄▄▀░░░░▄░░░░░█")
        print("█░░░░░▌▀▄░░░░░░░░░░░░░░░░░░░░░░▄▀▐░░░░░█")
        print("█░░░░▐▄▄▄█▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄█▄▄▄▌░░░░█")
        print("█░░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀░░░░█")
        print("▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀░")
        print("░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀░░░")
        print()
        time.sleep(2)
        print(color.BOLD + "There's a huge door blocking your entrance into the kingdom!\n Tell the bodyguard the secret code in order to get in! " + color.END)
        time.sleep(2)
        print()
        # User will be asked to write the decoded message from metro kingdom
        decodebowser = input(color.BOLD + "Goomba: " + color.END + "What was the phrase that you DECODED at Metro Kingdom?: ").lower()
        # If statement will run if user is correct
        if decodebowser == "defeat":
            time.sleep(1.5)
            print()
            print(color.BOLD + "Goomba: " + color.END + "That is correct! You may enter. ")
            print()
            time.sleep(1.5)
            print(color.RED + inventory[1] + " has gone deep into Bowser's Kingdom.... " + color.END)
            time.sleep(4)
            os.system("clear")
            time.sleep(2)
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⣀⣤⣀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⣀⣤⣀⠀⠀⠀⠀")
            print("⠀⠀⠀⣿⣿⣿⣧⠀⠀⠀⠀⠘⠿⣿⣿⠿⠃⠀⠀⠀⠀⣼⣿⣿⣿⣷⠀⠀⠀")
            print("⠀⠀⠀⢿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠀⠀⠀")
            print("⠀⠀⠀⠀⠉⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠉⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⣰⣾⣿⣦⠀⠀⠀⠀⠹⣿⠏⠀⠀⠀⠀⣴⣿⣷⣆⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠘⢿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⡿⠃⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⢾⡷⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⢾⡷⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⣴⣿⣦⡀⠀⠀⢀⣴⣿⣦⡀⠀⠀⢀⣴⣿⣦⡀⠀⠀⢀⣴⣿⣦⠀⠀⠀")
            print("⠀⣿⣿⣿⣿⣿⣿⣦⣶⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣶⣴⣿⣿⣿⣿⣿⣿⠀")
            print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
            print()
            time.sleep(1.5)
            print(color.BOLD + "You see Bowser's house...." + color.END)
            time.sleep(2)
            print(color.BOLD + "There's a lava moat surrounding his house!" + color.END)
            print()
            time.sleep(2)
            print("Answer the following question to unlock the bridge to cross the moat! ")
            print()
            
            time.sleep(2)
            # User will be asked to write the unscrambled word from metro kingdom
            bowserunscramble = input("What was the word you UNSCRAMBLED at Metro Kingdom?: ").lower()
            # If statement will run if user is correct    
            if bowserunscramble == "enemy":
                print("Correct!")
                time.sleep(1.5)
                print(color.RED + "The bridge is now unlocking for you to cross..." + color.END)
                time.sleep(3)
                rock_paper_scissors()
            
            # Else statement will run if user is incorrect
            else:
                print()
                print("Incorrect!")
                time.sleep(1.5)
                print("You tried jumping across the moat and died in the lava!")
                time.sleep(1.5)
                print(color.BOLD + "You lost!" + color.END)
                print()
                # remove all of the moons in inventory until metro
                inventory.remove("metro")
                inventory.remove("seaside")
                inventory.remove("luncheon")
                inventory.remove("bowser")
                if "Metro moon" in inventory:
                    inventory.remove("Metro moon")
                else:
                    inventory.remove("no Metro moon")
                    
                if "Seaside moon" in inventory:
                    inventory.remove("Seaside moon")
                    
                else:
                    inventory.remove("no Seaside moon")
                    
                if "Luncheon moon" in inventory:
                    inventory.remove("Luncheon moon")
                    
                else:
                    inventory.remove("no Luncheon moon")
                # Ask the user if they would like to play again    
                bowserretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                # If input is yes, send user to metro kingdom
                if bowserretry == "yes":
                    metro_kingdom()
                # If inout is no, send user to gameover function
                elif bowserretry == "no":
                    print()
                    print("Thanks for playing! Goodbye!")
                    gameover()
                # Invalid response will have the user answer the question again until valid response is given
                else:
                    print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                    print()
                    while True:
                        bowserretry = input("Would you like to play again? Type Yes or No: ").lower()
                            
                        if bowserretry == "yes":
                            metro_kingdom()
                            break
                        
                        elif bowserretry == "no":
                            print()
                            print("Thanks for playing! Goodbye!")
                            gameover()
                            break
                        
                        else:
                            print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                            print()
                            continue
                
        # Else statement will run if user enters invalid response
        else:
            print(color.BOLD + "Goomba: " + color.END + "That is incorrect. ")
            time.sleep(1)
            print()
            print(color.BOLD + "The goomba got suspicious of you and sent you back all the way to Metro Kingdom!" + color.END)
            time.sleep(5)
            inventory.remove("metro")
            inventory.remove("seaside")
            inventory.remove("luncheon")
            inventory.remove("bowser")
            
            # Remove all moons until metro kingdom
            if "Metro moon" in inventory:
                inventory.remove("Metro moon")
            else:
                inventory.remove("no Metro moon")
                
            if "Seaside moon" in inventory:
                inventory.remove("Seaside moon")
                
            else:
                inventory.remove("no Seaside moon")
                
            if "Luncheon moon" in inventory:
                inventory.remove("Luncheon moon")
                
            else:
                inventory.remove("no Luncheon moon")
            # Sends user to metro kingdom    
            metro_kingdom()
    # Function to play rock paper scissors against bowser
    def rock_paper_scissors():
        time.sleep(4)
        os.system("clear")
        for x in range(0,5):
            b = "Entering" + color.BOLD +" Bowser's Home " + color.END + "." * x
            print(b,end="\r")
            time.sleep(1)
        os.system("clear")
        time.sleep(2)
            
        print(color.BOLD + "Bowser: " + color.END +  "Look who I have here. Welcome to my home little guy!")
        print()
        time.sleep(2)
        print(color.BOLD + "Princess Peach: " + color.END + inventory[0] + ", I am over here. Please save me!!!!")
        print()
        time.sleep(2)
        print(color.BOLD + "Bowser: " + color.END + "He has to get through me first. Until then, you're mine Princess Peach! ")
        print()
        time.sleep(2)
        print(color.BOLD + inventory[1] + color.END + ": It's time for battle, Bowser. You're going down. ")
        
        time.sleep(6)
        os.system("clear")
        time.sleep(2)
        print("   _______             __   ____        __  __  __   ")
        print("   / ____(_)___  ____ _/ /  / __ )____ _/ /_/ /_/ /__ ")
        print("  / /_  / / __ \/ __ `/ /  / __  / __ `/ __/ __/ / _ \ ")
        print(" / __/ / / / / / /_/ / /  / /_/ / /_/ / /_/ /_/ /  __/")
        print("/_/   /_/_/ /_/\__,_/_/  /_____/\__,_/\__/\__/_/\___/ ")
        print()
        print()
        if "Mario" in inventory:
            print(color.RED +"             ▄████▄▄" + color.END    ) 
            print("              ▀█▀▐└─┐                   ")
            print("             █▄▐▌▄█▄┘                   ")                      
            print("             └▄▄▄▄─┘                    ")                     
            print("          ▄███▒██▒███▄        vs   BOWSER          ")                      
            print("          ▒▒█▄▒▒▒▒▄█▒▒                  ")                         
            print("            ▒▒▒▀▀▒▒▒                    ")                   
            print("          ▄███────███▄                  ")
            print()
            print(color.BOLD + inventory[0] + "("+ inventory[1] +")" + " vs. " + "Bowser           " + color.END)
            time.sleep(5)  
            
        else:
            print(color.GREEN +"             ▄████▄▄" + color.END    ) 
            print("              ▀█▀▐└─┐                   ")
            print("             █▄▐▌▄█▄┘                   ")                      
            print("             └▄▄▄▄─┘                    ")                     
            print("          ▄██████████▄        vs   BOWSER          ")                      
            print("          ▒▒█▄████▄█▒▒                  ")                         
            print("            ███▀▀███                     ")                   
            print("          ▄███────███▄                  ")              
            print()
            print(color.BOLD + inventory[0] + "("+ inventory[1] +")" + " vs. " + "Bowser         " + color.END)
            time.sleep(5)  
        print()
        print(color.BOLD + "Beat Bowser in Rock, Paper, Scissors 7 times to kill him and save Princess Peach! ")
        time.sleep(3)
        rpslist = ("rock", "paper", "scissors")
        choice = random.choice(rpslist)
        scoreuser = 0
        scorecomputer = 0 
        tie = 0
        x = 0
        count = 0
# This is the start of the while loop, this allows the game to run again and again. 
        try:
            while True:
                count = count + 1
                print()
                #These will ask the user for Rock, Paper or Scissors and allows the user to type in lower or uppercase
                print("_______________________________________________________________")
                print()
                user = input("Rock, Paper, or, Scissors?: ").lower()
                choice = random.choice(rpslist)
                #If the user types exit, then it will say the total games played, the user score and their win percentage, the computer score and their win percentage, and the amount of ties and its percentage
                if user == "Exit" or user == "exit":
                    inventory.clear()
                    print(color.BOLD + "You lose! You decided to forfeit the battle. " + color.END)
                    time.sleep(1.5)
                    print(color.BOLD + "Bowser kicked you out of the kingdom and kept Princess Peach!" + color.END)
                    # User will be asked if they want to play again
                    battleretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                    
                    # If user inputs yes, they will restart the game 
                    if battleretry == "yes":
                        full_game()
                        break
                    
                    # If user enters no, they will be sent to the gameover function         
                    elif battleretry == "no":
                        print()
                        print("Thanks for playing! Goodbye!")
                        gameover()
                        break
                    
                    
                    # Invalid input will ask the user the same question again until valid input is stated 
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        while True:
                            battleretry = input("Would you like to play again? Type Yes or No: ").lower()
                                
                            if battleretry == "yes":
                                full_game()
                                break
                                break
                            
                            elif battleretry == "no":
                                print()
                                print("Thanks for playing! Goodbye!")
                                gameover()
                                break
                                break
                            
                            else:
                                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                print()
                                continue
                    break
                
                # This will print both the computer's choice and the user's choice of Rock, paper or scissors       
                print("Your Choice: " + user.capitalize())
                print("Bowser's Choice: " + choice.capitalize())
                
                # This is all the possible combinations that can happen between the user and the computer. If the user wins, it prints the user wins and the user score goes up by 1. 
                # If the computer wins, it prints the computer wins and the computer score goes up by 1.
                if choice == "rock" and user == "paper":
                    print(color.BOLD + "You Win! Paper beats Rock!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scoreuser = scoreuser + 1
                    hp = random.randrange(10,20)
                    print()
                    print("You punched Bowser for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                
                elif choice == "rock" and user == "scissors":
                    print(color.BOLD + "Bowser Wins! Rock beats Scissors!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scorecomputer = scorecomputer + 1
                    hp = random.randrange(10,20)
                    print()
                    print("Bowser punched you for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                    
                elif choice == "paper" and user == "rock":
                    print(color.BOLD + "Bowser Wins! Paper beats Rock!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scorecomputer = scorecomputer + 1
                    hp = random.randrange(10,15)
                    print()
                    print("Bowser kicked you for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                    
                elif choice == "paper" and user == "scissors":
                    print(color.BOLD + "You Win! Scissors beats Paper!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scoreuser = scoreuser + 1
                    hp = random.randrange(10,20)
                    print()
                    print("You kicked Bowser for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                
                elif choice == "scissors" and user == "rock":
                    print(color.BOLD + "You Win! Rock beats Scissors!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scoreuser = scoreuser + 1
                    hp = random.randrange(10,15)
                    print()
                    print("You punched Bowser for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                    
                elif choice == "scissors" and user == "paper":
                    print(color.BOLD + "Bowser Wins! Scissors beats Paper!" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    scorecomputer = scorecomputer + 1
                    hp = random.randrange(10,20)
                    print()
                    print("Bowser used his chain and hit you for " + str(hp) + " HP worth of damage.")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                    
                elif choice == user:
                    print(color.BOLD + "Draw" + color.END)
                    print(color.BOLD  + "Type Exit if you want to forfeit" + color.END)
                    tie = tie + 1
                    print()
                    print("You and Bowser missed and did not hit each other!")
                    print()
                    print(color.BOLD + "Your Score: " + color.END + str(scoreuser))
                    print(color.BOLD + "Bowser's Score: " + color.END + str(scorecomputer))
                    
                    
                # This is what will print if the user does not type Rock, Paper or Scissors and some random jibberish. 
                else:
                    count = count - 1
                    print(color.BOLD + "Invalid Input" + color.END)
                 
                if scoreuser == 5:
                    print()
                    print(color.BOLD + "You are getting closer to victory.." + color.END)
                    print(color.BOLD + "Bowser: " + color.END + "I am getting very tired... When did you get so strong? ")
                    print()
                
                if scorecomputer == 7:
                    print()
                    print("Bowser uses his special move on you! You have no chance of attacking back!")
                    print()
                    time.sleep(2)
                    print(color.BOLD + "Bowser wins the final battle!" + color.END)
                    time.sleep(2)
                    print()
                    print(color.BOLD + "Bowser: " + color.END  + "Get out of here " + inventory[0] + ", Princess Peach is mine. ")
                    print()
                    time.sleep(2)
                    print(color.BOLD + "Bowser: " + color.END + " I am victorious once again! ")
                    print()
                    print(color.BOLD + "You lost! You died trying to fight Bowser! " + color.END)
                    print()
                    time.sleep(7)
                    
                    print()
                    # this prints the total games played
                    print(color.BOLD + color.UNDER + "Total Games Played:" + color.END  + " " + str(count) + color.END)
                    print()
                    # this prints the amount of wins I got 
                    print(color.BOLD + color.UNDER +  "Your Score:" + color.END + " " + str(scoreuser) + " win(s) " + color.END)
                    # this prints my win rate by dividing how much I won by the amount of games I have played
                    print(color.BOLD + color.UNDER + "Your Win Rate:" + color.END + " " + str(round(scoreuser/count*100)) + "%" + color.END)
                    # this prints the amount of losses I got
                    print(color.RED + "You lost " + str(scorecomputer) + " time(s)" + color.END)
                    print()
                    # this prints the computer's wins
                    print(color.BOLD + color.UNDER + "Bowser's Score:" + color.END + " " + str(scorecomputer) + " win(s) " + color.END)
                    # this prints the computer's win percentage
                    print(color.BOLD + color.UNDER + "Bowser's Win Rate:" + color.END + " " + str(round(scorecomputer/count*100)) + "%" + color.END)
                     # this prints the amount of times the computer lost
                    print(color.RED + "Bowser lost " + str(scoreuser) + " time(s)" + color.END)
                    print()
                    # this prints the amount of ties there were
                    print(color.BOLD + color.UNDER + "Tie Score:" + color.END + " " + str(tie) +" tie(s) " + color.END)
                   
                    # this prints the amount of ties there were in percentage form
                    print(color.BOLD + color.UNDER + "Tie Percentage Rate:" + color.END + " " + str(round(tie / count*100)) + "%"+ color.END)
                    time.sleep(4)
                    
                    print()
                    
                    # User will be asked if they want to play again
                    battleretry= input("Would you like to play again?" + color.BOLD + " Type Yes or No: " + color.END).lower()
                    
                    # if user inputs yes, they will start from the beginning 
                    if battleretry == "yes":
                        inventory.clear()
                        full_game()
                        break
                    
                    # If user inputs no, they will be sent to the gameover function
                    elif battleretry == "no":
                        print()
                        print("Thanks for playing! Goodbye!")
                        gameover()
                        break
            
                    # Invalid input will ask the user the same question again until valid response is given
                    else:
                        print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                        print()
                        while True:
                            battleretry = input("Would you like to play again? Type Yes or No: ").lower()
                                
                            if battleretry == "yes":
                                inventory.clear()
                                full_game()
                                break
                                break
                            
                            elif battleretry == "no":
                                print()
                                print("Thanks for playing! Goodbye!")
                                gameover()
                                break
                                break
                                
                            else:
                                print(color.BOLD + "Invalid Input. Try Again!" + color.END)
                                print()
                                continue
                        
                    break
                    
                    
                elif scoreuser == 7:
                    print()
                    print("You tricked Bowser, moved behind him and hit him!")
                    time.sleep(2)
                    print()
                    print("Bowser didn't expect the hit and he died! ")
                    print()
                    time.sleep(2)
                    print(color.BOLD + "You have won the Final Battle! " + color.END)
                    time.sleep(2)
                    print()
                    print(color.BOLD + color.RED + inventory[1] + " has acquired the Bowser Kingdom Power Moon!" + color.END + color.END)
                    inventory.append("Bowser moon")
                    time.sleep(2)
                    print()
                    print(color.BOLD + "Princess Peach: " + color.END + "Thank you " + inventory[0] + ", I don't know how I will ever repay you for this. I love you!")
                    print()
                    time.sleep(3)
                    print(color.BOLD + inventory[1] + color.END + ": I have done it. I have defeated my biggest enemy and saved my lover, Princess Peach.")
                    time.sleep(6)
                    print()
                    # this prints the total games played
                    print(color.BOLD + color.UNDER + "Total Games Played:" + color.END  + " " + str(count) + color.END)
                    print()
                    # this prints the amount of wins I got 
                    print(color.BOLD + color.UNDER +  "Your Score:" + color.END + " " + str(scoreuser) + " win(s) " + color.END)
                    # this prints my win rate by dividing how much I won by the amount of games I have played
                    print(color.BOLD + color.UNDER + "Your Win Rate:" + color.END + " " + str(round(scoreuser/count*100)) + "%" + color.END)
                    # this prints the amount of losses I got
                    print(color.RED + "You lost " + str(scorecomputer) + " time(s)" + color.END)
                    print()
                    # this prints the computer's wins
                    print(color.BOLD + color.UNDER + "Bowser's Score:" + color.END + " " + str(scorecomputer) + " win(s) " + color.END)
                    # this prints the computer's win percentage
                    print(color.BOLD + color.UNDER + "Bowser's Win Rate:" + color.END + " " + str(round(scorecomputer/count*100)) + "%" + color.END)
                     # this prints the amount of times the computer lost
                    print(color.RED + "Bowser lost " + str(scoreuser) + " time(s)" + color.END)
                    print()
                    # this prints the amount of ties there were
                    print(color.BOLD + color.UNDER + "Tie Score:" + color.END + " " + str(tie) +" tie(s) " + color.END)
                   
                    # this prints the amount of ties there were in percentage form
                    print(color.BOLD + color.UNDER + "Tie Percentage Rate:" + color.END + " " + str(round(tie / count*100)) + "%"+ color.END)
                    time.sleep(4)
                    outro()
                    break
                    break
        
        except ZeroDivisionError:
                print()
   
   # Gameover function is used when user loses
    def gameover():
        time.sleep(2)
        os.system('clear')
        time.sleep(2)
        print("    _____                         ____                 ")
        print("   / ____|                       / __ \                ")
        print("  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
        print("  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
        print("  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
        print("   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
        print()

       
   
    # Outro function is used when user wins and beats the game
    def outro():
        time.sleep(2)
        os.system('clear')
        time.sleep(2)
     
        print("   _____                            _       ")
        print("  / ____|                          | |      ")
        print(" | |     ___  _ __   __ _ _ __ __ _| |_ ___ ")
        print(" | |    / _ \| '_ \ / _` | '__/ _` | __/ __|")
        print(" | |___| (_) | | | | (_| | | | (_| | |_\__ \ ")
        print("  \_____\___/|_| |_|\__, |_|  \__,_|\__|___/")
        print("                    __/ |                  ")
        print("                    |___/                   ")
       
        print()
        print(color.BOLD + "You beat the game!" + color.END)
        print()
        print(color.BOLD + color.UNDER + "Stats: " + color.END + color.END)
        print()
        print(color.BOLD + "You got the following moons: " + color.END)
        print()
        
        if "Cascade moon" in inventory:
            time.sleep(2)
            print("Cascade Moon")
        if "Sand moon" in inventory:
            time.sleep(2)
            print("Sand Moon")
        if "Snow moon" in inventory:
            time.sleep(2)
            print("Snow Moon")
        if "Metro moon" in inventory:
            time.sleep(2)
            print("Metro Moon")
        if "Seaside moon" in inventory:
            time.sleep(2)
            print("Seaside Moon")
        if "Luncheon moon" in inventory:
            time.sleep(2)
            print("Luncheon Moon")
        if "Bowser moon" in inventory:
            time.sleep(2)
            print("Bowser Moon")
        
        print("____________________________________________")
        print()
        cascadecount = inventory.count("Cascade moon")
        sandcount = inventory.count("Sand moon")
        snowcount = inventory.count("Snow moon")
        metrocount = inventory.count("Metro moon")
        seasidecount = inventory.count("Seaside moon")
        luncheoncount = inventory.count("Luncheon moon")
        bowsercount = inventory.count("Bowser moon")
        
        totalmoon = cascadecount + sandcount + snowcount + metrocount + seasidecount+luncheoncount+bowsercount
        
        
        # Provides the stats of the game
        if totalmoon == 7:
            print("You got 7 moons in total. Your moon rank is S tier.")
        
        elif totalmoon == 6:
            print("You got 6 moons in total. Your moon rank is A tier.")
            
        elif totalmoon == 5:
            print("You got 5 moons in total. Your moon rank is B Tier.")
            
        elif totalmoon == 4:
            print("You got 4 moons in total. Your moon rank is C Tier.")
            
        elif totalmoon == 3:
            print("You got 3 moons in total. Your moon rank is D Tier. ")
        
        elif totalmoon == 2:
            print("You got 2 moons in total. Your moon rank is E Tier. ")
            
        elif totalmoon == 1:
            print("You got 1 moon in total. Your moon rank is F Tier. ")
            
        elif totalmoon == 0:
            print("You got 0 moons in total. Your moon rank is the worst tier.")
            
            
        print("________________________________________________")
        
        # Asks the user if they want to play again
        while True:
            playagain = input("Would you like to play again? ").lower()
            
            if playagain == "yes":
                inventory.clear()
                full_game()
                break
            
            elif playagain == "no":
                inventory.clear()
                gameover()
                break
            
            else:
                print()
                print(color.BOLD + "Invalid. Try again!" + color.END)
                continue
        
     
            
    game_intro()
    time.sleep(2)
    os.system("clear")
    description()
    os.system("clear")
    mario_luigi()


full_game()