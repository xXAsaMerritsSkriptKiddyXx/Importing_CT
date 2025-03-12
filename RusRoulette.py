#Module importing
import random, sys, time, os 

selfdestructtimer = 4

# Custom module importing with error handling
try:
    from package import custom_quit_module as c
except (ModuleNotFoundError, ImportError) as b:
    print("Critical Failure!: \n Missing Critical Files!")
    time.sleep(1)#Module importing
import random, sys, time, os 

selfdestructtimer = 4

# Custom module importing with error handling
try:
    from package import custom_quit_module as c
except (ModuleNotFoundError, ImportError) as b:
    print("Critical Failure!: \n Missing Critical Files!")
    time.sleep(1)
    print("Self destructing in..")
    while selfdestructtimer != 0:
        print(selfdestructtimer-1 , "...")
        selfdestructtimer -= 1
        time.sleep(1)
    if selfdestructtimer == 0:
        sys.exit()


try: 
    from package.specific_var import schlorgus as s
except (ModuleNotFoundError, ImportError) as e:
    print("Missing Schlorgus!")
    time.sleep(1)
    print("Self destructing in")
    while selfdestructtimer != 0:
        print(selfdestructtimer-1 , "...")
        selfdestructtimer -= 1
        time.sleep(1)
    if selfdestructtimer == 0:
        sys.exit()




# def funnyquit():
#     print("\n Then..")
#     time.sleep(1)
#     print("GET OUT! \n")
#     time.sleep(1)
#     try:
#         os.remove("saves.txt")
#     except FileNotFoundError as e:
#         pass
#     sys.exit()      

#Runs when game quits

playerscore = 0
botscore = 0
run = False
firsttime = True
selwep = None
hitc = 0
sey = ["yes", "y"]
han = ["no", "n"]

# Blueprint for different weapons.
class Weapon:
    def __init__(self,
        type = "1886 New Model Army", 
        name = "revolver",
        shells = 6,
        liveR = 1,
        damage = 80
    ):
        self.type = type
        self.name = name
        self.shells = shells
        self.liveR = liveR
        self.damage = damage

rubberband = Weapon("Rubber Band Launcher", "rubberband", 30, 2, 2 )
revolver = Weapon("1887 New Model Army","revolver", 6, 1, 100)
shotgun = Weapon("Remington 700","shotgun", 8, 3, 120)
bobsemple = Weapon("M1A2 Abrams","bobsemple", 29, 20, 3500)
gau21int = Weapon("M61A1 Vulcan","gau21int", 964, 700, 560)

options = {
    "rubberband" : rubberband,
    "revolver" : revolver,
    "shotgun" : shotgun,
    "bobsemple": bobsemple,
    "gau21int" : gau21int
}
# Dictionary for Weapon Options

weapons = []
weapons.append(rubberband)
weapons.append(revolver)
weapons.append(shotgun)
weapons.append(bobsemple)
weapons.append(gau21int)
# List for Weapon Options.
# Combo of List and Dictionary gives optoins on which to refer to. 

class Player:
    def __init__(self,
        name = "You",
        health = 100,
        x = True
):
        self.name = name
        self.health = health
        self.x = x

user = Player()

class Bot:
    def __init__(self,
        bname = "Evan Michael Merritt",
        bhealth = 100,
        y = False,
        qchance = 3
):
        self.bname = bname
        self.bhealth = bhealth
        self.y = y
        self.qchance = qchance
# x and y are used to iterate between whose turn it is.

comp = Bot()

def fireweapon():
 shotsfired = 0
 hitc = random.randint(0, selwep.shells - shotsfired)
 user.health = 100
 comp.bhealth = 100
 if hitc <= selwep.liveR:
     print("The " , selwep.type, "goes off") 
     time.sleep(1) 
     shotsfired += 1
     if user.x:
         print(user.name + " take " + str(selwep.damage) + " damage!")
         user.health = (user.health - selwep.damage)
     else:
         print(comp.bname + " takes " + str(selwep.damage) + " damage!")
         comp.bhealth = (comp.bhealth - selwep.damage)
 else: 
    print("Nothing happened.")
    time.sleep(1)

#Runs if weapon fires

#Swaps turn between bot and human
def turnswap():
    if user.x == True and comp.y == False:
        user.x = False
        comp.y = True
        print("It is now " + comp. bname + "'s turn!")
        time.sleep(1)
    else:
        user.x = True
        comp.y = False
        print("It is now your turn!")

#Runs at the end of the game. Gives options to play again and file deletion

# def endgamefilemanager():
#     print("Would you like to delete your save file?")
#     saveresponse = input("Y/N:")
#     if saveresponse in sey:
#         if os.path.exists("roulettesaves\\saves.txt"):
#             os.remove("roulettesaves\\saves.txt")
#             print("Save removed!")
#             time.sleep(1)
#             print("Exiting program!")
#             time.sleep(1)
#             sys.exit()
#     elif saveresponse in han:
#             print("Sucks to be you, deleting anyway!")
#             os.remove("roulettesaves\\saves.txt")
#             os.rmdir("roulettesaves")
#             time.sleep(1)
#             sys.exit()
#     else:
#             print("Invalid input. Please try again. \n")
#             time.sleep(1)
#             endgamefilemanager()

def realquit():
 quitresponse = input("Would you like to play again?: \n").strip().lower()
 if quitresponse in sey:
        main()
 elif quitresponse in han:
        c.endgamefilemanager()       
 else:
        print("Invalid input")
        realquit()


#File handling content

def makefile(path,content=""):
    with open(path, "w") as file:
        file.write(content)

if os.path.exists("roulettesaves"):
    makefile("roulettesaves\\saves.txt")
else:
    os.mkdir("roulettesaves")
    makefile("roulettesaves\\saves.txt")


def scoreboardsave():
    global botscore
    global playerscore
    try:
        with open("roulettesaves\\saves.txt","r+") as f:
            f.write(f"Bot Score: {str(botscore)} | Player Score: {str(playerscore)}")
        with open("roulettesaves\\saves.txt", "r") as f:    
            print(f.read())

    except:
     print("File Read Error!")
     sys.exit()

#Game Start, weapon selection
def main():
    global firsttime, run, s
    shotsfired = 0
    if s == 1:
        if firsttime:
             print("Hello. Welcome to Russian Roulette. Where your bravery will be put to the test.")
             time.sleep(1)
             print("Would you like to continue?")
             firsttime = False
             res = input("Y/N: \n").strip().lower()
             if res in sey:
                 run = True
                 weapon_selection()
             elif res in han:
                 c.funnyquit()
             else:
                 print("Please return a valid answer between Yes or No.")
                 firsttime = True
                 main()
        else:
         weapon_selection()

def weapon_selection():
 global run, res, selwep
 while(run):
     print("Please pick a weapon: \n")
     for i, weapon in enumerate(weapons):
            print(i+1, weapon.name)
     userin = input().strip().lower()
     if userin.isnumeric() and int(userin) <= len(weapons):
         selwep = weapons[int(userin)-1]
         print("\n You have chosen:" , selwep.type, "\n") 
         starter()
     else:
         print("Please return an integer from the allowed list!")

def starter():
    playorder = input("Would you like to go first? \n").strip().lower()
    if playorder in sey:
     user.x = True
     comp.y = False
     trigger()
    elif playorder in han:
     comp.y = True
     user.x = False
     print("It is now " + comp. bname + "'s turn!")
     trigger()
    else:
     print("Please return a valid answer.") 

#Roulette functions
def trigger():
    global hitc, playerscore, botscore, selwep
    roundsfired = 0
    while roundsfired <= selwep.shells:
        while user.x == True and comp.y == False:
            firc = input("Fire? \n Y/N:").lower().strip()
            if firc in sey:
                    fireweapon()
                    roundsfired += 1 
                    #Only runs at end of game
                    if user.health <= 0:
                        print(user.name + " have gone kablooey.\n ")
                        botscore += 1
                        scoreboardsave()
                        realquit()
                    turnswap()
            #Only runs if you decide not to fire
            elif firc in han:
                c.funnyquit()
            else:
             print("Please return a valid response: \n")   
        else:
            #Bot coding
            while comp.y == True and user.x == False:
                 quitp = random.randint(0,20)
                 if quitp <= comp.qchance:
                     print(comp.bname + " forefits! \n")
                     playerscore += 1
                     scoreboardsave()
                     realquit()
                 else:
                     if hitc <= selwep.liveR:
                         fireweapon() 
                         roundsfired += 1
                         #Only runs at end of game
                         if comp.bhealth <= 0:
                             print(comp.bname + " has gone kablooey.\n ")
                             playerscore += 1
                             scoreboardsave()
                             realquit()
                         turnswap()


if __name__ == "__main__":
    main() 

    print("Self destructing in..")
    while selfdestructtimer != 0:
        print(selfdestructtimer-1 , "...")
        selfdestructtimer -= 1
        time.sleep(1)
    if selfdestructtimer == 0:
        sys.exit()


try: 
    from package.specific_var import schlorgus
except (ModuleNotFoundError, ImportError) as e:
    print("Missing Schlorgus!")
    time.sleep(1)
    print("Self destructing in")
    while selfdestructtimer != 0:
        print(selfdestructtimer-1 , "...")
        selfdestructtimer -= 1
        time.sleep(1)
    if selfdestructtimer == 0:
        sys.exit()




# def funnyquit():
#     print("\n Then..")
#     time.sleep(1)
#     print("GET OUT! \n")
#     time.sleep(1)
#     try:
#         os.remove("saves.txt")
#     except FileNotFoundError as e:
#         pass
#     sys.exit()      

#Runs when game quits

playerscore = 0
botscore = 0
run = False
firsttime = True
selwep = None
hitc = 0
sey = ["yes", "y"]
han = ["no", "n"]

# Blueprint for different weapons.
class Weapon:
    def __init__(self,
        type = "1886 New Model Army", 
        name = "revolver",
        shells = 6,
        liveR = 1,
        damage = 80
    ):
        self.type = type
        self.name = name
        self.shells = shells
        self.liveR = liveR
        self.damage = damage

rubberband = Weapon("Rubber Band Launcher", "rubberband", 30, 2, 2 )
revolver = Weapon("1887 New Model Army","revolver", 6, 1, 100)
shotgun = Weapon("Remington 700","shotgun", 8, 3, 120)
bobsemple = Weapon("M1A2 Abrams","bobsemple", 29, 20, 3500)
gau21int = Weapon("M61A1 Vulcan","gau21int", 964, 700, 560)

options = {
    "rubberband" : rubberband,
    "revolver" : revolver,
    "shotgun" : shotgun,
    "bobsemple": bobsemple,
    "gau21int" : gau21int
}
# Dictionary for Weapon Options

weapons = []
weapons.append(rubberband)
weapons.append(revolver)
weapons.append(shotgun)
weapons.append(bobsemple)
weapons.append(gau21int)
# List for Weapon Options.
# Combo of List and Dictionary gives optoins on which to refer to. 

class Player:
    def __init__(self,
        name = "You",
        health = 100,
        x = True
):
        self.name = name
        self.health = health
        self.x = x

user = Player()

class Bot:
    def __init__(self,
        bname = "Evan Michael Merritt",
        bhealth = 100,
        y = False,
        qchance = 3
):
        self.bname = bname
        self.bhealth = bhealth
        self.y = y
        self.qchance = qchance
# x and y are used to iterate between whose turn it is.

comp = Bot()

def fireweapon():
 shotsfired = 0
 hitc = random.randint(0, selwep.shells - shotsfired)
 user.health = 100
 comp.bhealth = 100
 if hitc <= selwep.liveR:
     print("The " , selwep.type, "goes off") 
     time.sleep(1) 
     shotsfired += 1
     if user.x:
         print(user.name + " take " + str(selwep.damage) + " damage!")
         user.health = (user.health - selwep.damage)
     else:
         print(comp.bname + " takes " + str(selwep.damage) + " damage!")
         comp.bhealth = (comp.bhealth - selwep.damage)
 else: 
    print("Nothing happened.")
    time.sleep(1)

#Runs if weapon fires

#Swaps turn between bot and human
def turnswap():
    if user.x == True and comp.y == False:
        user.x = False
        comp.y = True
        print("It is now " + comp. bname + "'s turn!")
        time.sleep(1)
    else:
        user.x = True
        comp.y = False
        print("It is now your turn!")

#Runs at the end of the game. Gives options to play again and file deletion

# def endgamefilemanager():
#     print("Would you like to delete your save file?")
#     saveresponse = input("Y/N:")
#     if saveresponse in sey:
#         if os.path.exists("roulettesaves\\saves.txt"):
#             os.remove("roulettesaves\\saves.txt")
#             print("Save removed!")
#             time.sleep(1)
#             print("Exiting program!")
#             time.sleep(1)
#             sys.exit()
#     elif saveresponse in han:
#             print("Sucks to be you, deleting anyway!")
#             os.remove("roulettesaves\\saves.txt")
#             os.rmdir("roulettesaves")
#             time.sleep(1)
#             sys.exit()
#     else:
#             print("Invalid input. Please try again. \n")
#             time.sleep(1)
#             endgamefilemanager()

def realquit():
 quitresponse = input("Would you like to play again?: \n").strip().lower()
 if quitresponse in sey:
        main()
 elif quitresponse in han:
        c.endgamefilemanager()       
 else:
        print("Invalid input")
        realquit()


#File handling content

def makefile(path,content=""):
    with open(path, "w") as file:
        file.write(content)

if os.path.exists("roulettesaves"):
    makefile("roulettesaves\\saves.txt")
else:
    os.mkdir("roulettesaves")
    makefile("roulettesaves\\saves.txt")


def scoreboardsave():
    global botscore
    global playerscore
    try:
        with open("roulettesaves\\saves.txt","r+") as f:
            f.write(f"Bot Score: {str(botscore)} | Player Score: {str(playerscore)}")
        with open("roulettesaves\\saves.txt", "r") as f:    
            print(f.read())

    except:
     print("File Read Error!")
     sys.exit()

#Game Start, weapon selection
def main():
    global firsttime, run
    s = 1
    shotsfired = 0
    if s == 1:
        if firsttime:
             print("Hello. Welcome to Russian Roulette. Where your bravery will be put to the test.")
             time.sleep(1)
             print("Would you like to continue?")
             firsttime = False
             res = input("Y/N: \n").strip().lower()
             if res in sey:
                 run = True
                 weapon_selection()
             elif res in han:
                 c.funnyquit()
             else:
                 print("Please return a valid answer between Yes or No.")
                 firsttime = True
                 main()
        else:
         weapon_selection()

def weapon_selection():
 global run, res, selwep
 while(run):
     print("Please pick a weapon: \n")
     for i, weapon in enumerate(weapons):
            print(i+1, weapon.name)
     userin = input().strip().lower()
     if userin.isnumeric() and int(userin) <= len(weapons):
         selwep = weapons[int(userin)-1]
         print("\n You have chosen:" , selwep.type, "\n") 
         starter()
     else:
         print("Please return an integer from the allowed list!")

def starter():
    playorder = input("Would you like to go first? \n").strip().lower()
    if playorder in sey:
     user.x = True
     comp.y = False
     trigger()
    elif playorder in han:
     comp.y = True
     user.x = False
     print("It is now " + comp. bname + "'s turn!")
     trigger()
    else:
     print("Please return a valid answer.") 

#Roulette functions
def trigger():
    global hitc, playerscore, botscore, selwep
    roundsfired = 0
    while roundsfired <= selwep.shells:
        while user.x == True and comp.y == False:
            firc = input("Fire? \n Y/N:").lower().strip()
            if firc in sey:
                    fireweapon()
                    roundsfired += 1 
                    #Only runs at end of game
                    if user.health <= 0:
                        print(user.name + " have gone kablooey.\n ")
                        botscore += 1
                        scoreboardsave()
                        realquit()
                    turnswap()
            #Only runs if you decide not to fire
            elif firc in han:
                c.funnyquit()
            else:
             print("Please return a valid response: \n")   
        else:
            #Bot coding
            while comp.y == True and user.x == False:
                 quitp = random.randint(0,20)
                 if quitp <= comp.qchance:
                     print(comp.bname + " forefits! \n")
                     playerscore += 1
                     scoreboardsave()
                     realquit()
                 else:
                     if hitc <= selwep.liveR:
                         fireweapon() 
                         roundsfired += 1
                         #Only runs at end of game
                         if comp.bhealth <= 0:
                             print(comp.bname + " has gone kablooey.\n ")
                             playerscore += 1
                             scoreboardsave()
                             realquit()
                         turnswap()


if __name__ == "__main__":
    main() 
