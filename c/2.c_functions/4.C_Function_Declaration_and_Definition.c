#include <stdio.h>
void functions1(); // declare over there
void functions2(int x, int y);
// but move to under main because easier to organize
int main()
{
    functions1();
    functions2(10, 20);
    return 0;
}

void functions1() // full function over there but declare above main() function
{
    printf("Hello Bro\n");
    functions2(50, 100); // functions calling another functions
}

void functions2(int x, int y)
{
    printf("%d\n", x + y);
}