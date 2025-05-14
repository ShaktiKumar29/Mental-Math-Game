#Flash Anzan. Series of numbers will flash one after the another. User has to enter the sum once done
#For now, only 1 set of numbers
#Future, we can include multiple sets of numbers

import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='')  

x1 = int(input("Enter No. of digits: "))
x2 = int(input("\nEnter Number Count: "))
x3 = float(input("\nEnter Flash Speed (in seconds): "))
cl_scr()

print("Ready....")
time.sleep(1)
print("3....")
time.sleep(1)
print("2....")
time.sleep(1)
print("1....")
time.sleep(1)
print("Your time starts now")
time.sleep(1)
cl_scr()

sum_num = []

for i in range(x2):
    a = random.randint(10**(x1-1), 10**x1-1)
    print(a)
    sum_num.append(a)
    time.sleep(x3)
    cl_scr()

y = int(input("Enter the answer: "))
if np.sum(sum_num) == y:
    print("Correct\n")
    print("The numbers displayed were: ", sum_num)
else:
    print("Wrong. The correct answer is: ", np.sum(sum_num), "\n")
    print("\nThe numbers displayed were: ", sum_num)
