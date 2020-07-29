"""
Problem Link:https://www.codechef.com/LRNDSA01/problems/FCTRL
@author: subho57
"""
t=int(input())
while(t):
    count=0
    n=int(input())
    while n>=5:
        n//=5
        count+=n
    print(count)
    t-=1
