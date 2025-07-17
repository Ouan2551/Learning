#include <stdio.h>
void functions1() // custom function
{ // void mean this function not return value
    printf("Hello, World!\n");
}
int main() // main functions
{
    functions1(); // call function
    functions1(); functions1(); functions1(); // call the function multiple times
    return 0;
}