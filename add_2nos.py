#Addition
#Get input from user the no. of numbers to display and digits
#For now, we will keep digits same in all numbers
#For now, only addition of all nos and no negatives
#How much the user can solve in under a minute

import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='')  

    
x1 = int(input("How many numbers on screen: "))
if x1<2:
   print("Enter a number greater than 1: ")
   x1 = int(input())    
x2 = int(input("Enter max no. of digits: "))

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

while time.time() - start_time <= 60:
  s = 0
  for i in range(x1):
     a1 = random.randint(1, 10**x2-1)
     print(a1)
     s+=a1
  qns_count+=1

  b = input("\nAnswer: ")
  if int(b) == s:
    score+=1
  else:
    score-=0.25
  cl_scr()

print("You solved",qns_count,"questions\n")
print("Your score is:", score,"/",qns_count)
no_wrong = (qns_count-score)/1.25
print("Accuracy: ",100*(1-(no_wrong/qns_count)))

