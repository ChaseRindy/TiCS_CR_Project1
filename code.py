print("Welcome to The Abandoned Cabin!")

name = input("What is your name? ")

health = 100
temperature = 15.5
food = 2
firewood = 0
hasFlashlight = False
hasRadio = False
fireStarted = False
hours = 6
items = []

print(f"\nHello, {name}!")
print("You are hiking through the woods when you realize you are lost.")
print("It is getting dark, and the temperature is dropping.")
print("Luckily, you find an old cabin that looks like it has been abandoned.")

def showItems():
    print("\nItems:")
    if len(items) == 0:
        print("You don't have any items.")
    else:
        for item in items:
            print("-", item)

playing = True

while playing:

    print(f"\nIt is {hours}:00 PM.")
    print(f"Temperature: {temperature} degrees")
    print(f"Health: {health}")
    print(f"Food: {food}")
    print(f"Firewood: {firewood}")

    print("\nWhat do you want to do?")
    print("1. Search the cabin")
    print("2. Search outside")
    print("3. Rest")
    print("4. Check your items")

    choice = input("Choose an action: ")

    if choice == "1":
        print("\nYou search through the cabin.")

        if not hasFlashlight:
            print("You find an old flashlight on a table.")
            take = input("Do you take it? (yes/no): ")

            if take.lower() == "yes":
                hasFlashlight = True
                items.append("flashlight")
                print("You put the flashlight in your backpack.")
            else:
                print("You leave the flashlight behind.")

        else:
            print("You search through some old cabinets.")
            print("You don't find anything useful.")

        if not hasRadio:
            findRadio = input("\nDo you search upstairs? (yes/no): ")

            if findRadio.lower() == "yes":
                print("\nYou walk upstairs and find an old radio.")
                takeRadio = input("Do you take the radio? (yes/no): ")

                if takeRadio.lower() == "yes":
                    hasRadio = True
                    items.append("radio")
                    print("You take the radio.")

    elif choice == "2":
        print("\nYou go outside to search around the cabin.")

        if hasFlashlight:
            print("You use your flashlight to see through the darkness.")
        else:
            print("It is getting hard to see because it is almost dark.")
            print("You have trouble searching without a flashlight.")
            health = health - 5
            print("You lose 5 health from struggling in the dark.")

        print("\nWhat do you search for?")
        print("1. Food")
        print("2. Firewood")

        searchChoice = input("Choose 1 or 2: ")

        if searchChoice == "1":
            if food < 4:
                print("\nYou search around the cabin for food.")
                food = food + 1
                health = health - 5
                print("You find some canned food.")
                print("You lose 5 health from being outside in the cold.")
            else:
                print("\nYou search around but don't find any more food.")

        elif searchChoice == "2":
            print("\nYou collect some dry branches from around the cabin.")
            firewood = firewood + 2
            health = health - 5
            print("You collect 2 pieces of firewood.")
            print("You lose 5 health from being outside in the cold.")

        else:
            print("You don't know what to search for.")

    elif choice == "3":
        print("\nYou sit down and rest for a while.")

        if food > 0:
            eat = input("Do you eat some food while you rest? (yes/no): ")

            if eat.lower() == "yes":
                food = food - 1
                health = health + 10

                if health > 100:
                    health = 100

                print("You eat some food and recover 10 health.")
            else:
                print("You decide not to eat yet.")

        else:
            print("You don't have any food left.")

    elif choice == "4":
        showItems()

    else:
        print("Invalid choice. Try again.")
        continue

    hours = hours + 1

    if not fireStarted:
        temperature = temperature - 2
    else:
        temperature = temperature + 1

    if temperature < 5:
        health = health - 10
        print("\nThe cabin is getting very cold.")
        print("You lose 10 health.")

    if firewood > 0 and not fireStarted:
        startFire = input("\nYou have firewood. Do you start a fire? (yes/no): ")

        if startFire.lower() == "yes":
            fireStarted = True
            firewood = firewood - 1
            print("You start a fire in the fireplace.")
            print("The cabin begins to warm up.")
    elif fireStarted:
        print("\nThe fire is still burning and keeping the cabin warm.")

    if hasRadio and hours >= 9:
        print("\nYou remember the radio you found upstairs.")

        useRadio = input("Do you try to contact someone? (yes/no): ")

        if useRadio.lower() == "yes":
            print("\nYou turn on the radio.")
            print("After a few seconds, someone answers.")
            print("It is a rescue team searching the area.")

            print("You give them your location.")
            print("They tell you to stay inside the cabin.")

            print("\nA few hours later, the rescue team arrives.")
            print(f"\nYou were rescued safely, {name}!")
            playing = False

    if health <= 0:
        print("\nYou are too exhausted and cold to continue.")
        print("You spend the night in the cabin, but you are unable to stay warm.")
        print("\nENDING: You did not survive the night.")
        playing = False

    elif hours >= 12:
        print("\nThe sun begins to rise.")
        print("You look outside and see the woods clearly again.")

        if health >= 70 and fireStarted and food >= 1:
            print("\nYou made it through the night safely.")
            print("You kept the cabin warm and saved enough food to stay healthy.")
            print(f"\nENDING: You survived the night, {name}!")

        elif health >= 40 and (fireStarted or food >= 1):
            print("\nYou are tired and cold, but you prepared enough to make it through.")
            print("You leave the cabin and begin looking for the trail back home.")
            print(f"\nENDING: You survived, {name}, but it was a rough night.")

        else:
            print("\nYou barely made it through the night.")
            print("You decide to stay in the cabin and wait for a rescue team.")
            print(f"\nENDING: You survived, but barely, {name}.")

        playing = False

print("\nThanks for playing!")