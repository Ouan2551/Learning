#include <stdio.h>
int main()
{
    // structure for(declare, condition, change_value)
    for (int i = 0; i < 20; i++)
    {
        printf("%d\n", i);
        // nested loops => just loop inside loop
        for (int j = 0; j < 5; j++)
        {
            printf("%s", "WOW"); printf(" ");
        }
        printf("\n");
    }
    return 0;
}