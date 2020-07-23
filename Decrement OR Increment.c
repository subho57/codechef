#include <stdio.h>
#include <string.h>
#include <math.h>
int main(void) {
    int n;
    scanf("%d", &n);
    if(n%4==0)
        printf("%d",++n);
    else
        printf("%d", --n);
	return 0;
}
