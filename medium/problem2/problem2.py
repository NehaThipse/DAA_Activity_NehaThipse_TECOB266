#..#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
s=""

def now_check(val):

    #print("in now check")
    #print(val)
    flag=0
    v=val[0]
    for i in val:
        if i!=v and i!=0:
            flag=1
            break
    if flag==0:
        return(1)
    else:
        return -1

def isValid():

    sc = (Counter(s))
    ele = list(set(sc.elements()) )  
    flag=0  
    val= [sc[i] for i in ele]

    f = now_check(val)
    if f==1:
        return ("YES")
    else:   
        flag=0    
        for i in range(len(val)):
            temp=val
            temp[i]+=1
            f=now_check(temp)

            if f==1:
                flag=1
                return("YES")
            elif f == -1:
                temp[i]-=2
                f = now_check(temp)
                temp[i]+=1
                if f==1:
                    flag=1
                    return "YES"
        if flag==0:
            return "NO"


            

                

if __name__ == '__main__':    
    s = input()
    result = isValid()
    print(result)
