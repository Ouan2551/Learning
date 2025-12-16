#include <stdio.h>
#include <limits.h> // using for declare max or min nums.
int main()
{
    int my_array[20] = {10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 11, 22, 33, 44, 55, 12, 23, 34, 45, 56};
    printf("%d\n",my_array[3]);

    // Algorithm => find the lowest value in an array.
    int min_value = INT_MAX;
    int count = sizeof(my_array)/sizeof(my_array[0]);
    for (int i = 0; i < count; i++)
    {
        if (my_array[i] < min_value) min_value = my_array[i];
    }
    printf("%d\n", min_value);
    return 0;
}