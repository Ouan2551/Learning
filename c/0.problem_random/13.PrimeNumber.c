#include <stdio.h>
#include <stdbool.h>
int main()
{
    int x = 0, count = 0; scanf("%d", &x);
    for (int i = 2; i <= x; i++)
    {
        bool check_num = true;
        for (int j = 2; j < i; j++)
        {
            if(i % j == 0)
            {
                check_num = false;
            }
        }
        if (check_num == true)
        {
            printf("%d ", i); count++;
        }
    }
    printf("\n"); printf("%d", count);
    return 0;
}