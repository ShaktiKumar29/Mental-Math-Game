
#Division
#Get input from user: No. of digits for both dividend & divisor
#How much the user can solve in under a minute

import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='') 

    
dividend_dig = int(input("No. of digits for dividend: "))
divisor_dig = int(input("No. of digits for divisor: "))

if divisor_dig>dividend_dig:
   print("No. of digits in divisor cannot be greater than dividend. Enter again: ")
   divisor_dig = int(input())    

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
  divisor = random.randint(10**(divisor_dig-1), 10**divisor_dig-1)  # 1-digit divisor (exclude 1 to make it less trivial)

  # Find possible quotients that keep the dividend in the 3-digit range
  min_quotient = 10**(dividend_dig-1) // divisor + (1 if (10**(dividend_dig-1)) % divisor != 0 else 0)
  max_quotient = (10**dividend_dig-1) // divisor

  quotient = random.randint(min_quotient, max_quotient)
  dividend = divisor * quotient
  
  print(dividend,"%",divisor,"=")
  qns_count+=1

  ans = int(input())
  if dividend/divisor == ans:
    score+=1
  else:
    score-=0.25
  cl_scr()

no_wrong = (qns_count-score)/1.25
print("You solved",qns_count,"questions, out of which",qns_count-no_wrong,"are correct and",no_wrong,"are wrong")
print("\nYour score is:", score,"/",qns_count)
no_wrong = (qns_count-score)/1.25
print("\nAccuracy: ",100*(1-(no_wrong/qns_count)),"%")

