from art import text2art as font
from colorama import Fore, Style, init 
#LAB_PIP



text1=font("BELIEVE AND ACHEIVE", font='block')

print(text1)

text2=font("HELLO", font='sub-zero')

print(text2)



#Bonus

init(autoreset=True)

text3 = font("i love python", font='random')
print(Fore.GREEN + text3)


text4 = font("python", font='small')
print(Fore.BLUE + text4)