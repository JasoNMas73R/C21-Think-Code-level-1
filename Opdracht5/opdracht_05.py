#maak hier een functie voor een top 3 van bijvoorbeeld je favoriete games, eten of iets anders
#elke keer dat je de functie aanroept voeg je een nieuwe game toe als parameter
#weet je niet meer hoe? Check het solution filmpje op: https://www.linkedin.com/learning/programming-foundations-fundamentals-3/solution-favorite-cities

def fav_foods(thing):
    import time

    if (thing.lower() == "sushi"):
        print("Wow, you must really know me well.")
        time.sleep(1.5)
        print("Sushi is my number 1 favorite type of food.")
        time.sleep(1)
        print("It's just so freaking delicious...")
        time.sleep(2)
        print("Maybe you can guess number 2 and 3 on my list? :)")
    



fav_foods(input("Can you guess my favorite foods? "))
