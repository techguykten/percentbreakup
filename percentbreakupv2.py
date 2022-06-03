from random import *
import os
import time
import sys
import colorama
import random
from colorama import Fore, Back, Style

while True:
    os.system('cls')
    print (Fore.WHITE+Style.NORMAL+"-" * 110)
    print ()
    print(Fore.GREEN+'''
                    M#"""""""'M                             dP       M""MMMMM""M          
                    ##  mmmm. `M                            88       M  MMMMM  M          
                    #'        .M 88d888b. .d8888b. .d8888b. 88  .dP  M  MMMMM  M 88d888b. 
                    M#  MMMb.'YM 88'  `88 88ooood8 88'  `88 88888"   M  MMMMM  M 88'  `88 
                    M#  MMMM'  M 88       88.  ... 88.  .88 88  `8b. M  `MMM'  M 88.  .88 
                    M#       .;M dP       `88888P' `88888P8 dP   `YP Mb       dM 88Y888P' 
                    M#########M                                      MMMMMMMMMMM 88       
                                                                                 dP''')       


                                                                        
    print()
    print (Fore.WHITE+Style.NORMAL+"-" * 110)
    print()
    print (Fore.MAGENTA + " (Break Up v2.0)")
    print (Fore.YELLOW + " Contact me through: tuananhfa20@gmail.com")
    print()
    print (Fore.RED + " (0) Thoát")
    print (Fore.CYAN + " (1) Tính Toán Phần Trăm Đổ Vỡ Của Cặp Đôi")
    print ()
    print (Fore.GREEN+" Lựa chọn: "+Fore.WHITE, end='')
    x = input()
    if x == ("0"):
        exit()


    elif x == ("1"):
        os.system('cls')
        print(Fore.GREEN+'''

                                         _   ______                 _    _    _       
                                        (_) / /  _ \               | |  | |  | |      
                                           / /| |_) |_ __ ___  __ _| | _| |  | |_ __  
                                          / / |  _ <| '__/ _ \/ _` | |/ / |  | | '_ \ 
                                         / / _| |_) | | |  __/ (_| |   <| |__| | |_) |
                                        /_/ (_)____/|_|  \___|\__,_|_|\_\\____/| .__/ 
                                                                               | |    
                                                                               |_| ''')  

        print(Fore.MAGENTA)
        a = input(" Xin mời bạn nhập người thứ 1: ")
        b = input(" Xin mời bạn nhập người thứ 2: ")
        print(" Tỉ lệ đổ vỡ của cặp đôi", a, "và", b, end = ' ')
        print("là:", end = ' ')
        print(randint(1, 100), end = ' ')
        print("%")
        time.sleep(2)
        print()
        print(Fore.RED + " (1) Thoát Chương Trình")
        print()
        print(Fore.GREEN + " Lựa chọn: "+Fore.WHITE, end='')
        restart = input()
        if restart == ("1"):
            exit()
            


    




