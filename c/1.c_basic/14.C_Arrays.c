#include <stdio.h>
int main()
{

    int nums[] = {10, 20, 30, 40, 50};
    printf("%d\n", nums[1]);
    nums[5] = 200; // add value
    for (int i = 0; i <= 5; i += 1)
    {
        printf("%d\n", nums[i]);
    }

    // array size (byte)
    printf("array size : ");printf("%zu\n", sizeof(nums));
    printf("array elements count : ");printf("%zu\n", sizeof(nums)/sizeof(nums[0]));

    // multidimensional arrays
    int matrix[2][2] = {{1,2}, {3,4}}; //2d arrays
    printf("matrix[0][1] : %d\n", matrix[0][1]);
    
    return 0;
}