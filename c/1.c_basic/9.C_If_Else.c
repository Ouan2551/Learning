#include <stdio.h>
int main()
{
    // basic
    int a = 5, b = 10;
    if (a > b)
    {
        printf("value a more than value b\n");
    }
    else if (a < b)
    {
        printf("value b more than value a\n");
    }
    else
    {
        printf("value a equal value b\n");
    }

    // short form if-else
    // structure
    // value = (condition) ? (true_section) : (false_section);
    int a1 = 20, b1 = 20;
    (a1 == b1) ? (printf("a1 equal b1")) : (printf("a1 not equal b1"));
    return 0;
}