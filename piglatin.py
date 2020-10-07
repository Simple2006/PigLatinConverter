import sys
vowels = ("a", "e", "i", "o", "u")
constonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

def piglatin():
    while True:
        try:
            word = input("what word would you like to convert today?: ")
            if word[0] in vowels:
                print(word + "way")
                lexit = input("Are you done?: ")
                if lexit.lower() == "yes":
                    break
                elif lexit.lower() == "no":
                    piglatin()
                else:
                    valid = input("please type a valid response! yes or no: ")
            if word[0] in constonants and word[1] in vowels:
                new_word = word[1:]
                print(new_word + word[0] + "ay")
                lexit = input("Are you done?: ")
                if lexit.lower() == "yes":
                    break
                elif lexit.lower() == "no":
                    piglatin()
                else:
                    valid = input("please type a valid response! yes or no: ")
            if word[0] in constonants and word[1] in constonants:
                new_word = word[1:]
                new_word = word[2:]
                print(new_word + word[0] + word[1] + "ay")
                lexit = input("Are you done?: ")
                if lexit.lower() == "yes":
                    break
                elif lexit.lower() == "no":
                    piglatin()
                else:
                    valid = input("please type a valid response! yes or no: ")
        except:
            print("something went wrong.")
            break

piglatin()

