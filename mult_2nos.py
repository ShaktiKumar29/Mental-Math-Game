#Multiplication
#For now, only 2 numbers
#Get input from user, the no of digits for both numbers
#How much the user can solve in under a minute

import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='')  
    
x1 = int(input("Enter No. of digits for 1st number: "))
x2 = int(input("Enter No. of digits for 2nd number: "))

score = 0
print("\n")

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

start_time = time.time()
qns_count = 0

while time.time() - start_time <= 30:
  a1 = random.randint(10**(x1-1), 10**x1-1)
  a2 = random.randint(10**(x2-1), 10**x2-1)
  print(a1," x ",a2," = ")
  qns_count+=1

  b = input()
  if int(b) == a1*a2:
    score+=1
  else:
    score-=0.25
  cl_scr()

print("You solved",qns_count,"questions\n")
print("Your score is:", score,"/",qns_count)
no_wrong = (qns_count-score)/1.25
print("Accuracy: ",100*(1-(no_wrong/qns_count)))
