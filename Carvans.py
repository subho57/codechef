"""
Problem Link: https://www.codechef.com/LRNDSA01/problems/CARVANS
@author: subho57
"""
try:
    t=int(input())
    while(t):
        n=int(input())
        car=[int(i) for i in input().split()]
        if(n==1):
            print(1)
        else:
            count=1
            for i in range(1,n):
                if car[i]<car[i-1]:
                    count+=1
                else:
                    car[i]=car[i-1]
            print(count)
        t-=1
except:
    pass
