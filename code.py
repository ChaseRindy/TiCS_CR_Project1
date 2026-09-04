print("Welcome to The Abandoned Cabin!")

name = input("What is your name? ")

health = 100
temperature = 15.5
hasFlashlight = False
items = []

print(f"\nHello, {name}!")
print("You are hiking through the woods when it starts getting dark.")
print("You see an old cabin a little ways off the trail.")

def showItems():
    if len(items) == 0:
        print("You don't have any items.")
    else:
        print("You have:")
        for item in items:
            print("-", item)

playing = True

while playing:
    print("\nWhat do you want to do?")
    print("1. Enter the cabin")
    print("2. Search around outside")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou enter the old cabin.")
        print("It is dark and dusty. You find an old flashlight on a table.")

        takeFlashlight = input("Do you take the flashlight? (yes/no): ")

        if takeFlashlight == "yes":
            hasFlashlight = True
            items.append("flashlight")
            print("You take the flashlight.")

        print("\nYou see a staircase going upstairs and a door leading to the basement.")

        choice2 = input("Do you go upstairs or to the basement? ")

        if choice2.lower() == "basement":
            print("\nYou walk down the stairs into the basement.")

            if hasFlashlight:
                print("You turn on the flashlight and can see everything.")
                print("You find an old key sitting on a shelf.")
                items.append("key")
                print("You take the key.")
            else:
                print("It is completely dark. You can't see anything.")
                print("You decide to go back upstairs.")

        elif choice2.lower() == "upstairs":
            print("\nYou walk upstairs.")
            print("There is an old radio sitting on a desk.")

            radio = input("Do you try to turn on the radio? (yes/no): ")

            if radio == "yes":
                print("You turn the radio on.")
                print("You hear a weak signal from somewhere nearby.")
                print("It sounds like someone is looking for hikers.")

            else:
                print("You leave the radio alone.")

        else:
            print("You don't know where that is, so you go back downstairs.")

    elif choice == "2":
        print("\nYou search around the outside of the cabin.")
        print("You find some food underneath an old wooden box.")
        items.append("food")
        print("You put the food in your backpack.")

        temperature = temperature - 2
        health = health - 5

        print(f"The temperature drops to {temperature} degrees.")
        print(f"Your health is now {health}.")

        print("It is getting darker, so you decide to enter the cabin.")

        enter = input("Do you enter the cabin? (yes/no): ")

        if enter == "yes":
            print("You enter the cabin and find an old flashlight on a table.")

            takeFlashlight = input("Do you take it? (yes/no): ")

            if takeFlashlight == "yes":
                hasFlashlight = True
                items.append("flashlight")
                print("You take the flashlight.")

        else:
            print("\nYou decide to stay outside.")
            print("The temperature keeps dropping.")
            health = health - 20
            print(f"Your health is now {health}.")

    else:
        print("Invalid choice. Try again.")

    if "key" in items:
        print("\nYou notice a locked door at the back of the cabin.")
        print("You use the key you found and unlock it.")
        print("Behind the door is a trail leading back toward town.")
        print("\nYou escaped the woods safely!")
        print(f"Congratulations, {name}!")
        playing = False

    elif health <= 0:
        print("\nYou are too tired to continue.")
        print("You decide to stay at the cabin and wait for help.")
        print("The next morning, a rescue team finds you.")
        print("\nYou survived, but you probably should have stayed on the trail.")
        playing = False

    else:
        print("\nCurrent items:")
        showItems()

        finalChoice = input("\nDo you want to keep exploring or leave the cabin? ")

        if finalChoice.lower() == "leave":
            print("\nYou leave the cabin and try to find your way through the woods.")
            print("After walking for a while, you realize you are completely lost.")
            print("\nYou should have stayed in the cabin.")
            playing = False

        elif finalChoice.lower() == "explore":
            print("\nYou decide to keep exploring the cabin.")
            print("You hear something outside and decide to look around.")

        else:
            print("You aren't sure what to do, so you stay inside.")

print("\nThanks for playing!")