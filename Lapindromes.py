"""
CodeChef Link: https://www.codechef.com/LRNDSA01/problems/LAPIN
Problem Code: LAPIN
@author -- Subhankar Pal
"""
try:
    t=int(input())
    while(t):
        string=input()
        fh=string[:len(string)//2]
        fd = {i : fh.count(i) for i in set(fh)}
        sh=string[len(string)//2:] if len(string)%2==0 else string[len(string)//2+1:]
        sd = {i : sh.count(i) for i in set(sh)}
        #print(fd,sd)
        if(fd==sd):
            print("YES")
        else:
            print("NO")
        t-=1
except:
    pass
