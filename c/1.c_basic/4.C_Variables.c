// declare variable with data type in c follow this
// type variable name = value of that variable
#include <stdio.h>
int main()
{
    int nums = 200;
    float nums1 = 1580.4054;
    // and you need printf() with specific tell what data type you output
    // print("%specific_value", value)
    // %d for int, %c for char, %f for float
    printf("%d\n", nums); // new line not same like c++
    printf("%f\n", nums1);

    // for more full output for better code
    printf("my int : %d\n", nums);
    printf("my float : %f\n", nums1);

    // declare multiple variable with same type
    int x, y, z;
    x = y = z = 100;
    printf("my all nums : %d\n", x + y + z);
    return 0;
}