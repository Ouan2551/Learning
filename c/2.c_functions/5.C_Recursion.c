#include <stdio.h>

int sum(int num);

int main()
{
    // Recursion => technical that made function call itself
    int result = sum(10);
    printf("%d\n", result);
    return 0;
}

int sum(int num)
{
    if (num > 0)
    {
        return num + sum(num-1);
    }
    else
    {
        return 0;
    }
}