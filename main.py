from art import *
from colorama import *

Text1 = text2art("BELIEVE AND ACHIEVE", font='block')
print(Text1)
print(Fore.BLUE +Text1)

# Print the phrase "HELLO" with the "sub-zero" font
Text2 = text2art("HELLO", font='sub-zero')
print(Text2)

Text3 = text2art("Abdulaziz", font='sub-cybermedium')
print(Fore.CYAN + Text3)
print(Back.LIGHTBLUE_EX + Text3)