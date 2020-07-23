#include <stdio.h>
#include <string.h>
#include <math.h>
int main(void) {
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        int res=0;
        while(n>0){
            res=res*10+n%10;
            n/=10;
        }
        printf("%d\n",res);
    }
	return 0;
}
