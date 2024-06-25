
from termcolor import colored
from colorama import just_fix_windows_console
from art import *
import colorama
from colorama import Fore
colorama.init()

art_1 = text2art("BELIEVE AND ACHEIV", font='sub-zero')
print(Fore.BLACK + art_1 + Fore.RESET)  

art_2 = text2art("HELLO", font='sub-zero')
print(Fore.BLACK + art_2 + Fore.RESET)  



while True:
    print(colored("Welcome to the G.O.A.T program", 'red', attrs=['bold']))
    user_input = input('Do you want to Play🤔 (yes/no): ')
    
    if user_input.lower() == 'no' or user_input.lower() == 'exit':
        print(colored("Goodbye, See you later 😒", 'red', attrs=['bold']))
        break   
    if user_input.lower() == 'yes':
        userName = input('Enter your name: ')
        art_1 = text2art(f"{userName}\n IN \n THE \n HOUSE🎉 \n",font='sub-zero', )
        print(colored(art_1, 'blue')) 

        art_2 = text2art("Let's GO !!!", font='sub-zero')
        print(colored(art_2, 'green'))  


        just_fix_windows_console()

        print(colored(f"{userName} IS THE G.O.A.T 🐐", 'black', 'on_green', attrs=['bold'],))        
        break