#include <stdio.h>

int isdiv(long long int n){
    int i;
    for(i=1;i<22;i++){
        if(n%i!=0){
            return -1;
        }
    }
    return 1;
}

int main()
{
    long long int num = 2.0;
    while(1){
        if(isdiv(num)==1){
            break;
        }
        num++;
    }
    printf("%d", num);
    return 0;
}
