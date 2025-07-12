#include <stdio.h>
int main()
{
    // basic while loops
    int nums = 0;
    while (nums < 20)
    {
        printf("%d\n", nums); nums += 1;
    }

    // do-while loops
    int nums1 = 0;
    do
    {
        printf("%d\n", nums1+1); nums1 += 1;
    } while (nums1 < -1); // different from while loop because it will run at least once
    // but normal while loop check condition before run
    return 0;
}