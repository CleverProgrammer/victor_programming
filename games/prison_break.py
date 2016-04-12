def prison():
    print("You've just been imprisoned in a damp dungeon. It is rumored to be inescapable...")
    print("Do you bribe, stay, talk your way out, fake dead, or escape?")
    answer = input("Type bribe, stay, talk, dead or escape and hit 'Enter' (PS cheat codes ;)").lower()
    if answer == "stay" or answer == "1":
        print("You have been condemned to Death...Oh well...")
    if answer == "talk" or answer == "2":
    	print("It worked!!! Oh wait... no it didn't...")
    if answer == "dead" or answer == "3":
    	print("Buried alive... Great. Just great.")
    if answer == "escape" or answer == "4":
        print("Of course this is the only way to get out so JUST DO IT!!! (Shia laBoeuf)...")
    if answer == "bribe" or answer == "5":
    	print("Good idea. But WAIT!!! You are in a cell. Where is your money? Think!!!")

    elif answer == "666":
    	print("Nice.........")

prison()
