// data type       | format specific for output
// int 2 or 4 byte | %d or %i
// float 4 byte    | %f or %F
// double 8 byte   | %lf
// char 1 byte     | %c
// string          | %s
#include <stdio.h>
int main()
{
    // Char data type
    char character_val = 'A';
    printf("%c\n", character_val);

    // use number or char it will use ASCII value to output
    character_val = 60;
    printf("%c\n", character_val);

    // Numeric data type
    // just like another program language
    // but if you want to store scientific number with 'e' using float or double
    float numbers = 1e15;
    printf("%f\n", numbers);

    // set decimal precision
    double numbers1 = 14.1245839845;
    printf("%.1f\n", numbers1); // show 1 decimal
    printf("%.4f\n", numbers1); // show 4 decimal

    // get memory size using function "sizeof"
    printf("variable numbers have size = %zu",sizeof(numbers)); printf("%s\n"," byte");
    // using %zu because it design for using with sizeof() but some computer 
    // can use with %d but more safer when using %zu

    // type conversion
    
    return 0;
}