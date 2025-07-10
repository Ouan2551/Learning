#include <stdio.h>
int main()
{
    //  +, -, *, /, %, ++(increase 1), --(decrease 1)
    int x = 10; x += 5; printf("%d\n", x); // use '=' follow operators to save space (made code clean)
    // comparison operators (1 true, 0 false) >, <, >=, <=, ==, !=, &&, ||, !
    int x1 = 10, x2 = 20; printf("%d\n", x1 > x2);
    return 0;
}