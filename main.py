#!/usr/bin/env python

'''
 * File: main.py
 * Project: Engipy
 * Author: kvant666ubl (GitHub)
 * -----
 * Last Modified: ***
 * Modified By: kvant666ubl
 * -----
 * Copyright (c) Kvant Ubl 2020 
 '''

from colorama import init 
from termcolor import colored 

from info import theory, howto
from methods import ask1, simple_lambda, MTBF, MTTF, MTTR, Ai, reliability

def start(color):
    print(colored('''
     ______            _                  __ __ 
    / ____/___  ____ _(_)___  __  __   __/ // /_
   / __/ / __ \/ __ `/ / __ \/ / / /  /_  _  __/
  / /___/ / / / /_/ / / /_/ / /_/ /  /_  _  __/ 
 /_____/_/ /_/\__, /_/ .___/\__, /    /_//_/    
             /____/ /_/    /____/    v 0.0.1       ''', color, attrs=['bold']));
    
    print(colored('''
★ S o l v e / y o u r / e n g i / p r o b l e m ★  ''', color, attrs=['bold', 'blink']));
    
    info  = colored('<info>', 'white', attrs=['underline'])
    go    = colored('<go>',   'white', attrs=['underline'])
    howto = colored('<howto>','white', attrs=['underline'])
    q     = colored('<q>/<quit>', 'white', attrs=['underline'])
    
    line1 = colored('* type ', color) + info  + colored(' to get basics of reliability theory and methods;\n', color);
    line2 = colored('* type ', color) + go    + colored(' to go to calculation menu;\n', color)
    line3 = colored('* type ', color) + howto + colored(' to learn more about start modes of engipy;\n', color)
    line4 = colored('* type ', color) + q     + colored(' to, well, you got it.\n', color)
    text  = line1 + line2 + line3 + line4
    print(text)


def action():
    mistake = 0
    while True:     
        com = str(input("      → "))
        print('\n')
        if com == 'info':
            theory()
            start('magenta')
        elif com == 'go':
            r = reliability()
            if r == True:
                start('blue')
        elif com == 'howto':
            howto()
        elif com == 'q' or com == 'quit':
            print(colored("★ Thanks for using Engipy ★\n", 'cyan', attrs=['bold']))
            return False
        else:
            print(colored("Ops! Loks like you made a mistake! Try again ッ\n", 'red', attrs=['bold']))
            mistake = mistake + 1 # :)
            if mistake == 4:
                print()
                print(colored('Wow-wow-wow, samurai, easy. Take it!\n', 'cyan', attrs=['bold', 'underline']))
                start('green')
                mistake = 0


def main():
    start('yellow')
    action()
    

if __name__ == "__main__":
    main()