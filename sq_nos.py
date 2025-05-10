#Square
#Get range from user & generate numbers in that range

import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='')  
    
x = int(input("Enter no. of digits: "))

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
  a = random.randint(10**(x-1), 10**x-1)
  print(a,"^2 = ")
  qns_count+=1

  b = input()
  if int(b) == a*a:
    score+=1
  else:
    score-=0.25
  cl_scr()

print("You solved",qns_count,"questions\n")
print("Your score is:", score,"/",qns_count)
no_wrong = (qns_count-score)/1.25
print("Accuracy: ",100*(1-(no_wrong/qns_count)))

    

