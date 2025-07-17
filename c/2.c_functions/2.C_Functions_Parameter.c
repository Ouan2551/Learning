#include <stdio.h>
void functions1(int nums)
{
    printf("%d\n", nums);
}
void functions2(int array[], int array_length)
{
    // int array_length = sizeof(array)/sizeof(array[0]);
    // c is low level then you need to put length of array
    // same time that you input array into function

    for (int i = 0; i < array_length; i += 1)
    {
        printf("%d\n", array[i]);
    }
}
int function3(int x, int y) // position in front of name_functions means type of value to return
{
    int sum = x + y;
    return sum;
}
int main()
{
    functions1(200); functions1(500);

    // pass array to function parameter
    int arrays1[5] = {1, 2, 3, 4, 5};
    int length = sizeof(arrays1)/sizeof(arrays1[0]);
    functions2(arrays1, length);

    // return value from function
    printf("%d\n",function3(10, 20));
    return 0;
}