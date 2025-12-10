#include <stdio.h>
int main()
{
    int n = 0, sum = 0; scanf("%d", &n);
    for (int i = 3; i <= n; i++)
    {
        if (i % 3 == 0)
        {
            sum += i;
        }
    }
    printf("%d", sum);
    return 0;
}