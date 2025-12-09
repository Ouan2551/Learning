#include <stdio.h>
int main()
{
    // 1) Operators

    printf("Operators\n");
    //  +, -, *, /, %, ++(increase 1), --(decrease 1)
    int x = 10; x += 5; printf("%d\n", x); // use '=' follow operators to save space (made code clean)
    // comparison operators (1 true, 0 false) >, <, >=, <=, ==, !=, &&, ||, !
    int x1 = 10, x2 = 20; printf("%d\n", x1 > x2);
    printf("\n");

    printf("Arithmetic\n");
    // 2) Arithmetic
    // if you want result in decimal. you need to using data types 'float' or 'double'
    float x3 = 10.0, x4 = 7.0; printf("%.4f\n", x3/x4);

    // incrementing and decrementing
    ++x3; ++x4; printf("x3 : %.1f\n", x3); printf("x4 : %.1f\n", x4);
    --x3; --x4; printf("x3 : %.1f\n", x3); printf("x4 : %.1f\n", x4);
    printf("\n");

    printf("Assignment Operators\n");
    // 3) Assignment Operators (structure => operators connect with =)
    int a = 200; a += 200; printf("a : %d\n", a); // save space
    printf("\n");

    printf("Comparison\n");
    // 4) Comparison e.g. (>, <, >=, <=, ==, !=)
    a = 500;
    if (a == 500)
    {
        printf("The value is correct\n");
    }
    printf("%d\n",a <= 200); // 0 (true), 1 (false)
    printf("\n");

    printf("Logical\n");
    // 5) Logical (&& and, || or, ! not)
    a = 3000;
    if (a * 2 == 6000 && a % 2 == 0)
    {
        printf("The value is correct\n");
    }
    // or you using 0 and 1 as a false and true
    int value1 = 0, value2 = 1;
    printf("%d\n",value1 && value2);
    printf("\n");
    return 0;
}