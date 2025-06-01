from colorama import init, Fore, Style
import emoji

init(autoreset=True)

print("How are you? Do you feel something? Choose it below:")
print("1 - I'm definitely not fine")
print("2 - I grieﬂy despaired")
print("3 - I feel myself exhausted")
print("4 - I'm anxious right now")

while True:
    choice = input("Write down a number from 1-4: ")
    if choice == "1":
        print(Fore.YELLOW + "I hope that soon you will feel yourself better " + emoji.emojize(":smile:", language='alias'))
        break
    elif choice == "2":
        print(Fore.BLUE + "Well, I'm in the same position now. Can share my support to you " + emoji.emojize(":disappointed:", language='alias'))
        break
    elif choice == "3":
        print(Fore.GREEN + "Try to relax. Somehow if you can... " + emoji.emojize(":sleeping:", language='alias'))
        break
    elif choice == "4":
        print(Fore.MAGENTA + "With friend anxiety should pass a bit better " + emoji.emojize(":sweat_smile:", language='alias'))
        break
    else:
        print(Fore.RED + "You wrote incorrect number")
