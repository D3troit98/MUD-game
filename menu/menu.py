import database.user as User



def openMenu(p,w,h):

    while True:
        print("choose z to save the game")
        print("choose x to level up")
        print("choose c to quit the game")
        print("choose v to see leader board")
        print("choose p to return to game")
        c = (input().lower())
        if c == 'p':
            return
        elif c == "z":
            print("storing data")
            User.storeData(p)
            User.storeInTextFile()
            print("done")
        elif c  == "x":
            print("leveling up takes xp but increases your health")
            p.levelUp(p)
        elif c == "c":
            print("quit successful, hoped you saved!")
            exit(-1)
        elif c == "v":
            print("Leader Board")
            User.listbyScore()

            
            

