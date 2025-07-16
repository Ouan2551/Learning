#include <stdio.h>
int main()
{
    // pointers => variable that store memory address of another values
    int nums = 100;
    int* memory_address = &nums;
    printf("%d\n", nums);
    printf("%p\n", memory_address);

    // dereference => using '*' front of pointers to get value;
    printf("%d\n", *memory_address);

    // pointers & arrays
    int numbers[4] = {1,2,3,4};
    int size_numbers = sizeof(numbers)/sizeof(numbers[0]);
    for (int i = 0; i < size_numbers; i += 1)
    {
        printf("values : %d\n", numbers[i]);
        printf("address : %p\n", &numbers[i]);
    }

    // example using pointers with arrays
    int numbers1[5] = {10, 20, 30, 40, 50};
    int *pointers1 = numbers1;
    for (int i = 0; i < 5; i += 1)
    {
        printf("%d\n", *(pointers1+1));
    }
    return 0;
}