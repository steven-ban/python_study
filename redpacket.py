# redpacket.py
# coding = utf-8

import random

money = 100
count = input("Please input people count: ")
while(count >= 1) : 
    rand = random.random()
    if(rand >= 0.1 and rand <= 0.5) : 
        print money * rand 
        money -= money * rand
        count -= 1

print money