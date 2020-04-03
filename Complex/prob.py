#!/bin/python3


'''
5/13 test cases failed , 8 passes 
'''
import math
import os
import random
import re
import sys
import collections

# Complete the matrixRotation function below.
def matrixRotation(matrix, r , n, m):
    layers = int(n/2)
    for i in range(layers):
        l=[]       

        for xx in range(i,m-i-1):
            l.append(matrix[xx][i])
        for xx in range(i , n-i-1):
            l.append(matrix[m-1-i][xx])
        for xx  in (range(m-1-i ,i ,-1) ):
            l.append(matrix[xx][n-1-i])
        for xx in (range(n-i-1 , i ,-1 )):
            l.append(matrix[i][xx])
        #print(l)
        '''if r>len(l):
            r= r%len(l)
        if r>=len(l)/2:
            l = (l[r:] + l[:r])
        else:
            l = (l[-r:] + l[:-r])'''

        x=0
        for y in range(r):
            if(x==0):
                x=len(l)-1
            else:
                x-=1
        
        
            
        #print(x)
        
        
        cnt=x
        for xx in range(i,m-i-1): 
            #print("changing")           
            matrix[xx][i]= l[cnt]
            
            if cnt==len(l)-1:
                cnt=0
            else:
                cnt+=1

        for xx in range(i , n-i-1):
            matrix[m-1-i][xx]= l[cnt]
            
            if cnt==len(l)-1:
                cnt=0
            else:
                cnt+=1
        for xx  in (range(m-1-i ,i ,-1) ):
            matrix[xx][n-1-i]= l[cnt]
           
            if cnt==len(l)-1:
                cnt=0
            else:
                cnt+=1
        for xx in (range(n-i-1 , i ,-1 )):
            matrix[i][xx]= l[cnt]
            
            if cnt==len(l)-1:
                cnt=0
            else:
                cnt+=1
    for i in range(m):
        for j in range(n):
            print(str(matrix[i][j])+" " ,end="")
        print("")
    
            
    
    

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r ,n ,m)
