/*
Problem Link : https://www.codechef.com/LRNDSA01/problems/FCTRL
@author: subho57
*/
#include <stdio.h>
int main(void){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        int count=0;
        while(n>=5){
            n/=5;
            count+=n;
        }
        printf("%d\n", count);
    }
}
