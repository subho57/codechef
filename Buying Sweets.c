#include <stdio.h>
int main(void) {
	int test,n,x;
	scanf("%d", &test);
	int output[test];
	for(int i=0;i<test;i++) {
	    scanf("%d %d", &n, &x);
	    int deno[n], sum=0;
	    for(int j=0;j<n;j++) {
	        scanf("%d", &deno[j]);
	        sum+=deno[j];
	    }
	    if(sum%x==0 || n==1 && sum>x)
	        output[i]=sum/x;
	    else if(sum<x)
	        output[i]=-1;
	    else {
            int rem=sum%x;
            int j=0,flag=0;
            while(j<n)
                if(deno[j++]<=rem)
                {   flag=1;
                    break;
                }
            if (flag)
                output[i]=-1;
            else
                output[i]=sum/x;
	    }
	}
	for(int i=0;i<test;i++)
	    printf("%d\n",output[i]);
	return 0;
}
