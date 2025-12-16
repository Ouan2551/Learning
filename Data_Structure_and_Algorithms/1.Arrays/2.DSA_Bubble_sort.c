#include <stdio.h>
int main()
{
    // Bubble_sort => sort value from lowest to highest
    int unsorted_array[20] = {10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 11, 22, 33, 44, 55, 12, 23, 34, 45, 56};
    int count = sizeof(unsorted_array)/sizeof(unsorted_array[0]);
    // printf("%d\n", count); we got count = 20
    for (int i = 0; i < count; i++)
    {
        compare_value1 = unsorted_array[i];
        if (i+1 != count - 1) compare_value2 = unsorted_array[i+1];
        if (compare_value2 > compare_value1)
        {
            temp = compare_value2; compare_value2 = compare_value1; compare_value1 = temp;
        }
    }
    return 0;
}