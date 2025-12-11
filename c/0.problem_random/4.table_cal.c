#include <stdio.h>
int main()
{
    int x = 0; scanf("%d", &x);
    for (int i = 1; i <= 10; i++)
    {
        printf("%d", x); printf(" * "); printf("%d", i); printf(" = "); printf("%d\n", x*i);
    }
    return 0;
}