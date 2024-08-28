import random
import time

operators=["+","-","*"]
MAX=15
MIN=2
problems=10

def generator():
    left_side=random.randint(MIN,MAX)
    right_side=random.randint(MIN,MAX)
    operator=random.choice(operators)
    exp=str(left_side) +" "+ operator+" "+str(right_side)
    ans=eval(exp)
    return exp,ans
wrong=0
start_time=time.time()
input("press any key to start!!!!")
print("-----------------------")
for i in range(problems):
    exp,ans=generator()
    while True:


        guess=input("Problem #" + str(i + 1) + ": " + exp + " = ")
        if guess ==str(ans):
            break
        wrong +=1
end_time=time.time()
total_time=round(end_time-start_time,2)
print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")        
