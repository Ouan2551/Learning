#include <stdio.h>
int main()
{
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size_nums = sizeof(nums)/sizeof(nums[0]);
    for (int i = 0; i < size_nums; i++)
    {
        printf("%d\n", nums[i]);
    }
    return 0;
}