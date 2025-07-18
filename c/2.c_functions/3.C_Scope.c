#include <stdio.h>
int y = 100; // this call global variable
int x = 20;
void functions1()
{
    int x = 5; // this x only live in function1;
    printf("inside functions1");
    printf("%d\n", x);
    printf("%d\n", y);
}
int main()
{
    // scope => variable work only place that they created
    // global scope => declare variable outside function
    // if it use same name variable it will choose local variable
    printf("main functions");
    printf("%d\n", y);
    functions1();
    return 0;
}