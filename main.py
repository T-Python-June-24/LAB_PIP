from art import text2art
from colorama import Fore



believe_achieve = text2art("BELIEVE AND ACHIEVE", font="block")
hello = text2art("HELLO", font="sub-zero")

print(Fore.RED + believe_achieve)
print(Fore.GREEN + hello)

phrase = text2art("I've done my sentence", font="cybermedium")
print(Fore.BLUE + phrase)