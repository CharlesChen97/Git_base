#!/usr/bin/python3

sum_value=0
for num in range(1,100001):
    solg=True
    for item in range(2,num):
        if num%item==0:
            solg=False
            break
    if solg:
        sum_value+=num
print(sum_value)
