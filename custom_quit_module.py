import random, sys, time, os 
sey = ["yes", "y"]
han = ["no", "n"]


def funnyquit():
    print("\n Then..")
    time.sleep(1)
    print("GET OUT! \n")
    time.sleep(1)
    try:
        os.remove("saves.txt")
    except FileNotFoundError as e:
        pass
    sys.exit()     

def endgamefilemanager():
 print("Would you like to delete your save file?")
 saveresponse = input("Y/N:")
 if saveresponse in sey:
     if os.path.exists("roulettesaves\\saves.txt"):
         os.remove("roulettesaves\\saves.txt")
         print("Save removed!")
         time.sleep(1)
         print("Exiting program!")
         time.sleep(1)
         sys.exit()
 elif saveresponse in han:
        print("Sucks to be you, deleting anyway!")
        os.remove("roulettesaves\\saves.txt")
        os.rmdir("roulettesaves")
        time.sleep(1)
        sys.exit()
 else:
        print("Invalid input. Please try again. \n")
        time.sleep(1)
        endgamefilemanager()
        
def realquit():
 quitresponse = input("Would you like to play again?: \n").strip().lower()
 if quitresponse in sey:
        main()
 elif quitresponse in han:
        endgamefilemanager()       
 else:
        print("Invalid input")
        realquit()
