#include <stdio.h>
int main()
{
    int day = 4;
    switch (day)
    {
        case 1:
        {
            printf("Hello1"); return 0;
        }
        case 2:
        {
            printf("Hello2"); return 0;
        }
        default: // not match in every case
        {
            printf("Not match"); return 0;
        }
    }
    return 0;
}