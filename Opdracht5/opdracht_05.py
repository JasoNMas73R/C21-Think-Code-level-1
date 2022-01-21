#maak hier een functie voor een top 3 van bijvoorbeeld je favoriete games, eten of iets anders
#elke keer dat je de functie aanroept voeg je een nieuwe game toe als parameter
#weet je niet meer hoe? Check het solution filmpje op: https://www.linkedin.com/learning/programming-foundations-fundamentals-3/solution-favorite-cities

from ssl import OPENSSL_VERSION_INFO


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

    elif (thing.lower() == "fishsticks"):
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
    
    elif (thing.lower() == "grilled cheese"):
        print("That's right! I love a grilled cheese sandwich so much.")
        time.sleep(1.5)
        print("They're my third most favorite type of food actually. \n")
        time.sleep(2.5)
        print("Pro tip out here: try making a sandwich in a pan")
        time.sleep(0.75)
        print("first and foremost, then before you add the sandwich")
        time.sleep(1)
        print("put some Samurai sauce in the sandwich together with")
        time.sleep(0.75)
        print("the cheese. When you grill the thing, the cheese and")
        time.sleep(1)
        print("the the sauce will melt together if done proper and it")
        time.sleep(0.75)
        print("will turn the cheese into a melted chili cheese!")
        time.sleep(1.25)
        print("Serve with Heinz on the side to ease off the heat and done! \n")
        time.sleep(8)
        print("Maybe you can guess number 1 and 3 on my list? :)")
        time.sleep(2.5)
        fav_foods(input("Can you guess my favorite foods? "))

    elif (thing.lower() == "grilled cheese sandwich"):
        print("That's right! I love a grilled cheese sandwich so much.")
        time.sleep(1.5)
        print("They're my third most favorite type of food actually. \n")
        time.sleep(2.5)
        print("Pro tip out here: try making a sandwich in a pan")
        time.sleep(0.75)
        print("first and foremost, then before you add the sandwich")
        time.sleep(1)
        print("put some Samurai sauce in the sandwich together with")
        time.sleep(0.75)
        print("the cheese. When you grill the thing, the cheese and")
        time.sleep(1)
        print("the the sauce will melt together if done proper and it")
        time.sleep(0.75)
        print("will turn the cheese into a melted chili cheese!")
        time.sleep(1.25)
        print("Serve with Heinz on the side to ease off the heat and done! \n")
        time.sleep(8)
        print("Maybe you can guess number 1 and 2 on my list? :)")
        time.sleep(2.5)
        fav_foods(input("Can you guess my favorite foods? "))

    #thanks to https://manytools.org/hacker-tools/convert-images-to-ascii-art
    #for the conversion and https://stackoverflow.com/questions/4703516/how-to-write-string-literals-in-python-without-having-to-escape-them
    #for letting me lead on the right path to avoid the escapes
    elif (thing.lower() == "jason"):
        print("That's not a type of food! But if you're tired of me right now, get a load of the old me:")
        time.sleep(5)
        print("\n")
        time.sleep(0.75)
        print("""                                   ///###%##%%%######*/***.                              """)
        time.sleep(0.75)
        print("""                         . ...%##((######%%%%%%%%%%%%%%%#%%#(//*//(((((((((((((########%#""")
        time.sleep(0.75)
        print("""//(/((((((##(######%%%%%%##%##((###(((((((#%#%%%%%%%%%&%%%%%####((((##%%%%%%%%%%####(((((""")
        time.sleep(0.75)
        print("""%%%####((((///////////(%((((//(((((((((((#####(######%%%%%%%%%((###(/////////////////////""")
        time.sleep(0.75)
        print("""/////////////////////##((((((##((((((############/#######%%%%%%%#%%##((((((((////////////""")
        time.sleep(0.75)
        print("""///////////////////##/%(//######((((((##(#(#############%##%%%%%%%%%%##(((((((((((((//(//""")
        time.sleep(0.75)
        print("""/////////////////(#((((/(#####((#/(((((((((####(##########%##%%%%%#%%%%##((((((((((((((((""")
        time.sleep(0.75)
        print("""/////////////////(//**((#########(/((/////////(((((((((((((########(((#%#((#(((((((((((((""")
        time.sleep(0.75)
        print("""///(///((/(//(/(((///(#%%%%%#%###((////(//*///(((((/////////(///(/(#(((%%#((####(((((((((""")
        time.sleep(0.75)
        print("""////((((/(((((((////(#%%%%%%####((*,,*/***/((/////((/(///*****/((((((#####(#(#######(((((""")
        time.sleep(0.75)
        print("""((((((((((((((#((/((#%%%/***,.**,.........,*//((((((//*,,,,,,*/(####%%%#(#############(#(""")
        time.sleep(0.75)
        print("""((((((((((((((#((#(#%##*,,..............................,,,,,*(#%%##%#(##################""")
        time.sleep(0.75)
        print("""((((((((((((((#((##%%#/*,,,................................,,*//////((((%%###############""")
        time.sleep(0.75)
        print("""(#(((########(#((#%%%(**,,,,,..*/((//(((//**,,.......,.....,,,,,******/(%%%%#############""")
        time.sleep(0.75)
        print("""#((((########(###%%%%(,,,,,,**/*,,,,,,,*//////**,,,,,,,,,*//////**,,**/(%%%%#############""")
        time.sleep(0.75)
        print("""(####(###(#(#(%###%%(,,,,,,,,****//(((/////((/***,,,**///(((((///(#(/*/(%&&%#############""")
        time.sleep(0.75)
        print("""((((((((((((,(/##%##(,,,..,,**/(//#%##(##(#(((**,,,,*//((((///***///((((%&&%#############""")
        time.sleep(0.75)
        print("""(((((((((((*######((,,,,.....,.,,,*/((((**##,**,...,*/((##%(/#%#((((/((/%%&%#############""")
        time.sleep(0.75)
        print("""(((((((((((*##,,,(#(**,,,.......,***////////,,.,...,*****/((#((*(##(///(#%%##############""")
        time.sleep(0.75)
        print("""(#((((##(#(/*/*/(#((**,,,,.........,,,,,...........,****,*************//##(#####%########""")
        time.sleep(0.75)
        print("""(*****####/***,*/,*****,,,,,,,............,,,,,,...,,***,,,,,,,,,,,****/#(#(/(#(//##//(#/""")
        time.sleep(0.75)
        print("""#(**((#####***,*,,******,,,,.,..,,,,,,,,,,**,,,,...,,***,,,,.,,,,,,****/((#//(##//#(//##/""")
        time.sleep(0.75)
        print("""*#/****#####***,,*,*/******,**,*,******///*,,//////*//*/***,,,,,,,,**//(//#//###//(//(##/""")
        time.sleep(0.75)
        print("""**#**(#######**/,,,*//***/*////////(/((((//(##%%%###%%#/////********///#//(//###/////(##(""")
        time.sleep(0.75)
        print("""(*/#**#######(**(((##/////(((#######%#((//**///((#(((/////((((////////(#(//#//###//#//###""")
        time.sleep(0.75)
        print("""######(#(#####((///#/////((((######%%%##(/////////////////(###((((((((/%#//##//##//##//##""")
        time.sleep(0.75)
        print("""######################((((((((((((((##%&%#%###########%&&%##(((#(((((#%%%%%%%%###########""")
        time.sleep(0.75)
        print("""*/#///##((#######%%&&###((((((((((((//*/*//((#(##((#/(((*//(//((((((##%%%%%%%%%#%%%%%#%#%""")
        time.sleep(0.75)
        print("""(*(#///((/###(%#%%%(##%&/#####(((/////////////*****/////////((((((#&&#(((((%%%%%%%%%#%##%""")
        time.sleep(0.75)
        print("""#//##/(////#%%%%%/((#&/#(((#####((//////((((((((((((/((/////(((##%%&&%(/##%%%%%%%%%%%%%%%""")
        time.sleep(0.75)
        print("""##//#(/#/##%%#%#(#%%&*##%((((#%%##((///*//////////////////((###%%#%%&%(///(//###%%%%%%%%%""")
        time.sleep(0.75)
        print("""###//#/**((##((/(%%&/,(#%((((###%%%##((///**********///((#####&%#%%%%(////((////*/###%%%%""")
        time.sleep(0.75)
        print("""###(##,**/((((/(/(/(((/(&#((((###%%%%%%###((((((((((((#%%%###&%##%%%(//(//**/////////(%##""")
        time.sleep(0.75)
        print("""#####***/*/(#(////(((##////(((###%%%%%%&&&&&%%%%%%%%%%&%(###%%###%%#(((////**/(/////(#((/""")
        time.sleep(0.75)
        print("""###%,,*,***(((((((/((#(/(/*//####%%%%%&&&&&&%%%%%%%%&%#((##%%%#%%%#((////////((/####((((/""")
        time.sleep(0.75)
        print("\n")
        time.sleep(0.75)
        print("Me at age 7, probably. Taken at Schiphol Airport (back when the panorama terrace was open).")
        time.sleep(4)
        fav_foods(input("Can you guess my favorite foods? "))

    elif (thing.lower() == "aphex twin"):
        print("that's not a type of food you cunt")
        exit()
        
    elif (thing.lower() == "sauerkraut"):
        print("Are you literally fucking kidding me?")
        time.sleep(3.5)
        print("God I hate that stuff")
        exit()

    elif (thing.lower() == "exit"):
        exit()

    else:
        print("Nope, that ain't it. Try again.")
        time.sleep(3.5)
        fav_foods(input("Can you guess my favorite foods? "))
        
    






fav_foods(input("Can you guess my favorite foods? "))
