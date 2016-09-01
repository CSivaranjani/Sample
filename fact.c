#include<stdio.h>
void main()
{
long int a;
int n;
scanf("%d",&n);
a=factorial(n);
printf("%ld",a);
}
factorial(int n)
{
if(n==1)
return(1);
else if(n==0)
return 0;
else
return(n*factorial(n-1));
}
