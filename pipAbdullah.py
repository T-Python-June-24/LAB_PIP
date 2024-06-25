from art import *
from termcolor import colored
from colorama import just_fix_windows_console
from termcolor import colored
user_input = input('Enter your name: ')

art_1 = text2art(f"{user_input}\n IN \n THE \n HOUSE🎉 \n",font='sub-zero', )
print(colored(art_1, 'blue'))  # Change 'blue' to any color you prefer

art_2 = text2art("Let's GO !!!", font='sub-zero')
print(colored(art_2, 'green'))  # Change 'green' to any color you prefer




# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

# then use Termcolor for all colored text output
print(colored(f"{user_input} IS THE G.O.A.T 🐐", 'black', 'on_green', attrs=['bold'],))