#include <stdio.h>
#include <stdbool.h>
int main()
{
    int x = 0; scanf("%d", &x);
    for (int i = 2; i <= x; i++)
    {
        int num_prime = i; bool check_prime = true;
        for (int j = 2; j < i; j++)
        {
            if (num_prime % j == 0)
            {
                check_prime = false;
            }
        }
        if (check_prime == true)
        {
            printf("%d", num_prime); printf(" ");
        }
    }
    return 0;
}