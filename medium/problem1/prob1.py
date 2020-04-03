#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the timeInWords function below.
def timeInWords(h, m):
    wrds =['' ,'one' ,'two' ,'three','four','five' ,'six' ,'seven' ,'eight','nine' ,'ten' , 'eleven' ,'twelve']
    mins1= ['eleven' , 'twelve' ,'thirteen' ,'fourteen' ,'fifteen' ,'sixteen' ,'seventeen' ,'eighteen' ,'nineteen']
    

    if (m==0):
        return (wrds[h]+' o\' clock')
    if m <=30:
        if( m == 15):
            return('quarter past ' +wrds[h])
        if( m ==30):
            return('half past ' +wrds[h])
        
        if m <=10:
            if(m==1):
                return ( wrds[m] +' minute past '+wrds[h])
            else:
                return ( wrds[m] +' minutes past '+wrds[h])
        elif m <20 :
            return( mins1[m-11] +' minutes past '+wrds[h])
        else:
            return('twenty '+wrds[m-20] +' minutes past '+wrds[h])


    else:
        m1 = 60-m
        if(m==45):
            return('quarter to '+wrds[h+1])
        if m1<=10:
            return(wrds[m1]+' minutes to '+wrds[h+1])
        elif m1<=19:
            return(mins1[m1-11] +' minutes to '+wrds[h+1])
        else:
            return("twenty "+wrds[m1-20]+' minutes to '+wrds[h+1])




       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
