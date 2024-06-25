from art import text2art
from colorama import Fore


believe_achieve_art = text2art("BELIEVE", font='block') + text2art("AND", font='block') +text2art("ACHIEVE", font='block')
hello_art = text2art("HELLO", font='sub-zero')
saudi_arabia = text2art("saudi arabia", font="small")


print(Fore.MAGENTA+ believe_achieve_art)
print(Fore.GREEN + saudi_arabia)
print(Fore.CYAN +hello_art)
