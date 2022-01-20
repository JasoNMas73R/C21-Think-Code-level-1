#maak hier een functie voor een top 3 van bijvoorbeeld je favoriete games, eten of iets anders
#elke keer dat je de functie aanroept voeg je een nieuwe game toe als parameter
#weet je niet meer hoe? Check het solution filmpje op: https://www.linkedin.com/learning/programming-foundations-fundamentals-3/solution-favorite-cities

def fav_foods(thing):
    import time
    #got this from https://www.guru99.com/python-time-sleep-delay.html

    if (thing.lower() == "sushi"):
        print("Wow, you must really know me well.")
        time.sleep(1.5)
        print("Sushi is my most favorite type of food!")
        time.sleep(1.5)
        print("It's just so freaking delicious...")
        time.sleep(2.5)
        print("I really dig Nigiri with salmon and various types of Maki.")
        time.sleep(2)
        print("Damn... wish I had some sushi right now... where's the wasabi? \n") #thanks ouke
        time.sleep(2)
        print("Maybe you can guess number 2 and 3 on my list? :)")
        time.sleep(2.5)
        fav_foods(input("Can you guess my favorite foods? "))
    
    #if (thing.lower() == "fish sticks" or "fishsticks"): didn't work the way I wanted so I did a dirty fix
    #came up with various errors if I tried to change it and leaving it as is causes ANY answer after typing
    #fish sticks or fishsticks to behave like that was being typed every time
    if (thing.lower() == "fish sticks"):
        print("Yep, that's correctamundo.")
        time.sleep(1)
        print("Fish sticks are my second most favorite type of food.")
        time.sleep(2)
        print("I especially like them on a bun,")
        time.sleep(0.75)
        print("preferably with a slice of cheese")
        time.sleep(0.75)
        print("and a nice sauce on top. \n")
        time.sleep(3)
        print("Maybe you can guess number 2 and 3 on my list? :)")
        time.sleep(2.5)
        fav_foods(input("Can you guess my favorite foods? "))

    if (thing.lower() == "fishsticks"):
        print("Yep, that's correctamundo.")
        time.sleep(1)
        print("Fishsticks are my second most favorite type of food.")
        time.sleep(2)
        print("I especially like them on a bun,")
        time.sleep(0.75)
        print("preferably with a slice of cheese")
        time.sleep(0.75)
        print("and a nice sauce on top. \n")
        time.sleep(3)
        print("Maybe you can guess number 2 and 3 on my list? :)")
        time.sleep(2.5)
        fav_foods(input("Can you guess my favorite foods? "))
    



fav_foods(input("Can you guess my favorite foods? "))
