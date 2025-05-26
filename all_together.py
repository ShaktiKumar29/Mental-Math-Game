#Overall menu to user for addition, subtraction, multiplication & Square
import numpy as np
import random
import os
import time

def cl_scr():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end='') 

#Function to calculate metrics
def metrics_calc(qns_count, score):
    no_wrong = (qns_count-score)/1.25
    print("You solved",qns_count,"questions, out of which",qns_count-no_wrong,"are correct and",no_wrong,"are wrong")
    print("\nYour score is:", score,"/",qns_count)
    no_wrong = (qns_count-score)/1.25
    print("\nAccuracy: ",100*(1-(no_wrong/qns_count)),"%")
    
#Addition - Same digits
def same_dgs(x1):
    score = 0
    x2 = int(input("\nEnter no. of digits: "))
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
    metrics_calc(qns_count, score)
    
#Addition - Different digits
def diff_dgs(x1):    
    x2_max = int(input("\nEnter max no. of digits you want: "))
    x2_min = int(input("\nEnter min no. of digits you want: "))
    score = 0
    print("\n")
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

    start_time = time.time()
    qns_count = 0

    while time.time() - start_time <= 30:
      s = 0
      for i in range(x1):
         a1 = random.randint(10**(x2_min-1), 10**x2_max-1)
         print(a1)
         s+=a1
      qns_count+=1

      b = input("\nAnswer: ")
      if int(b) == s:
        score+=1
      else:
        score-=0.25
      cl_scr()
    metrics_calc(qns_count, score)


#Function for multiplication of numbers
def mul_nos():
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
    metrics_calc(qns_count, score)


#Function for addition of numbers
def add_nos():   
    print("ADDITION\nYou can choose upto how many numbers you want to add & number of digits\n")
    x1 = int(input("How many numbers do you want to add at a given time: "))      
    if x1<2:
       print("Enter a number greater than 1: ")
       x1 = int(input())    
    sd = int(input("\nDo you want all numbers to be of same number of digits or different\nEnter 1 for yes & 2 for no: "))
    if sd==1:
       same_dgs(x1)
    else:
       diff_dgs(x1)


#Function for subtraction of numbers
def sub_nos():
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
      print(max(a1,a2),"-",min(a1,a2))
      qns_count+=1

      b = input()
      if int(b) == abs(a1-a2):
        score+=1
      else:
        score-=0.25
      cl_scr()
    metrics_calc(qns_count, score)


#Function for Squaring of numbers
def sq_nos():
    g = int(input("Enter no. of digits: "))
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
      a = random.randint(10**(g-1), 10**g-1)
      print(a,"^2 = ")
      qns_count+=1

      b = input()
      if int(b) == a*a:
        score+=1
      else:
        score-=0.25
      cl_scr()
    metrics_calc(qns_count, score)

   
#User Interface
print("Select mode:\n1. Timed Mode: How many questions can you solve within the time limit (you can set your own time)\n2. Questions: You get to choose how many questions\nEnter your choice: ")    
mode_inp = int(input("Enter your choice: "))

print("Select one from below\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Square of number\n")
inp = int(input("Enter: "))
if inp<1 or inp>4:
   inp = int(input("Enter a number between 1 & 4: "))
cl_scr()
  
if inp==1:
   add_nos()
elif inp==2:
   sub_nos()
elif inp==3:
   mul_nos()
elif inp==4:
   sq_nos()
else:
   print("Wrong input")

