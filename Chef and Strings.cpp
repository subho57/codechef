#include <iostream>
using namespace std;

int main() {
	int t;
    cin >> t;
    while(t--)
    {
        long temp=0,temp1=0,size,sum=0;
        cin >> size;
        cin >> temp;
        while(--size)
        {
            cin >> temp1;
            sum+=abs(temp-temp1)-1;
            temp=temp1;
        }
        cout << sum << endl;
    }
	return 0;
}
