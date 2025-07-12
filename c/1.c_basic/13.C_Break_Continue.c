#include <stdio.h>
int main()
{
    // break => stop loop
    for (int i = 0; i < 20; i++)
    {
        printf("%i\n", i);
        if (i == 10)
        {
            break;
        }
    }
    printf("\n");
    // continue => skip loop
    for (int i = 0; i < 20; i++)
    {
        if (i % 2 == 0)
        {
            continue;
        }
        printf("%i\n", i);
    }
    return 0;
}