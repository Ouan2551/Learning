#include <iostream>
#include <climits>
int main()
{
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    // arrays => dsa that store multiple elements
    int nums[] = {1, 20, 500, 35, 25};
    // find the lowest value in array
    int lowest = INT_MAX;
    for (int i : nums)
    {
        lowest = std::min(lowest, i);
    }
    std::cout << lowest << '\n';

    // bubble sort => sort from lowest to highest
    int nums1[5] = {1, 20, 500, 35, 25};
    int len = sizeof(nums1) / sizeof(nums1[0]);
    for (int i = 0; i < len - 1; i++)
    {
        for (int j = 0; j < len - i - 1; j++)
        {
            if (nums1[j] > nums1[j+1])
            {
                int temp = nums1[j];
                nums1[j] = nums1[j+1];
                nums1[j+1] = temp;
            }
        }
    }
    for (int i = 0; i < len; i++)
    {
        std::cout << nums1[i] << ' ';
    }
    
    // selection sort => find lowest and move to the front
    int nums2[] = {7, 12, 9, 11, 3, 5, 20};
    len = sizeof(nums2) / sizeof(nums2[0]);
    for (int i = 0; i < len; i++)
    {
        
    }
    
    return 0;
}