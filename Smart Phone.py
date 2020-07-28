"""
Problem Link: https://www.codechef.com/LRNDSA01/problems/ZCO14003
@author: subho57
"""
try:
    t=int(input())
    l=[]
    cpy=t
    while(t):
        n=int(input())
        l+=[n]
        t-=1
    l.sort()
    for i in range(len(l)):
        l[i]=l[i]*cpy
        cpy-=1
    print(max(l))
except:
    pass
