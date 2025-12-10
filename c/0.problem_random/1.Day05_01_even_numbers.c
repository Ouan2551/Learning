#include <stdio.h>
int main()
{
    int x = 0; scanf("%d", &x); int i = 2, new_line = 0;
    while (i <= x)
    {
        if (i % 2 == 0)
        {
            printf("%d", i); printf(" "); new_line++;
            if (new_line % 10 == 0)
            {
                printf("\n");
            }
        }
        i++;
    }
    return 0;
}