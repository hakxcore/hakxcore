#!/bin/python3
from __future__ import print_function
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from terminaltables import SingleTable
print(Fore.BLUE+Back.YELLOW+"Hi My name is Mukesh Kumar "+ Fore.YELLOW+ Back.BLUE+"HAKXCORE") 
table_instance = SingleTable([["""
                
                ██   ██  █████  ██   ██ ██   ██  ██████  ██████  ██████  ███████ 
                ██   ██ ██   ██ ██  ██   ██ ██  ██      ██    ██ ██   ██ ██      
                ███████ ███████ █████     ███   ██      ██    ██ ██████  █████   
                ██   ██ ██   ██ ██  ██   ██ ██  ██      ██    ██ ██   ██ ██      
                ██   ██ ██   ██ ██   ██ ██   ██  ██████  ██████  ██   ██ ███████                                                  

                Website: https://mukeshkumarcharak.ml   Author: Mukesh Kumar                            
                Github:  https://github.com/hakxcore    Email:  anonymous_mails_box@protonmail.ch       
                                                                
"""]], '(hakxcore)')
print(Fore.BLACK+Back.WHITE+(table_instance.table))
print()
