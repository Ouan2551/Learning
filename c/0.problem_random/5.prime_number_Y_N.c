#include <stdio.h>
#include <stdbool.h>
int main()
{
    int x = 0; scanf("%d", &x); bool check_prime = true;
    for (int i = 2; i < x; i++)
    {
        if (x % i == 0)
        {
            check_prime = false;
        }
    }
    if (check_prime == true && x != 1)
    {
        printf("is prime");
    }
    else
    {
        printf("is not prime");
    }
    return 0;
}