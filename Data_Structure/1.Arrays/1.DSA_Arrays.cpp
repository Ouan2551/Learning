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
    std::cout << "lowest num : " << lowest << '\n';
    std::cout << "__________________" << '\n';
    
    // bubble sort => sort from lowest to highest
    std::cout << "Bubble Sort" << '\n';
    std::cout << "process" << '\n';
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
        // process output
        for (int j = 0; j < len; j++)
        {
            std::cout << nums1[j] << ' ';
        }
        std::cout << '\n';
    }
    // for (int i = 0; i < len; i++)
    // {
    //     std::cout << nums1[i] << ' ';
    // }
    std::cout << "__________________" << '\n';

    // selection sort => find lowest and move to the front
    std::cout << "Selection Sort" << '\n';
    std::cout << "process " << '\n';
    int nums2[] = {7, 12, 9, 11, 3, 5, 20};
    len = sizeof(nums2) / sizeof(nums2[0]);
    for (int i = 0; i < len; i++)
    {
        int min_index = i;
        for (int j = i+1; j < len; j++)
        {
            if (nums2[j] < nums2[min_index])
            {
                min_index = j;
            }
        }
        // insert lowest value to front
        int temp = nums2[i];
        nums2[i] = nums2[min_index];
        nums2[min_index] = temp;

        // process output
        for (int j = 0; j < len; j++)
        {
            std::cout << nums2[j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << "__________________" << '\n';

    // insertion sort => sort element and move them to correction position before go to another element
    std::cout << "Insertion Sort" << '\n';
    std::cout << "process " << '\n';
    int nums3[] = {64, 34, 25, 12, 22, 11, 90, 5};
    len = sizeof(nums3) / sizeof(nums3[0]);
    for (int i = 1; i < len; i++)
    {
        int insert_index = i;
        int current_value = nums3[i];
        int j = i - 1;
        while (j >= 0 && nums3[j] > current_value)
        {
            for (int j = 0; j < len; j++)
            {
                std::cout << nums3[j] << ' ';
            }
            std::cout << '\n';

            nums3[j+1] = nums3[j];
            insert_index = j;
            j--;
        }
        nums3[insert_index] = current_value;

        // process output
        for (int j = 0; j < len; j++)
        {
            std::cout << nums3[j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << "__________________" << '\n';

    // linear search => search pass index from 0 to index that have equal value or ned array
    std::cout << "linear search" << '\n';
    int search_value = 10;
    int nums4[] = {1, 2, 3, 4, 5, 6, 7, 8, 9 , 10};
    len = sizeof(nums4) / sizeof(nums4[0]);
    for (int i = 0; i < len; i++)
    {
        if (nums4[i] == search_value)
        {
            std::cout << "find value at index : " << i << '\n';
        }
    }
    std::cout << "__________________" << '\n';

    // binary search => use range of num search in sort array only
    std::cout << "binary_search" << '\n';
    // go to middle index then compare to num that want to find if middle_num > find_num then search left section
    // if middle_num < find_num then search right section
    int nums5[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24, 25};
    len = sizeof(nums5)/sizeof(nums5[0]);
    int find_num = 23, linear_search_count = 0, binary_search_count = 0;
    
    // test on linear_search
    for (int i = 0; i < len; i++)
    {
        linear_search_count++;
        if (nums5[i] == find_num)
        {
            std::cout << "linear_search_count : " << linear_search_count << '\n'; break;
        }
    }
    
    // test on binary search
    int low = 0, high = len - 1;
    while (low <= high)
    {
        binary_search_count++;
        // int middle_index = (low + high) / 2;
        int middle_index = low + ((high - low)/2);
        int middle_value = nums5[middle_index];
        if (middle_value > find_num)
        {
            high = middle_index - 1;
        }
        else if (middle_value < find_num)
        {
            low = middle_index + 1;
        }
        else if (middle_value == find_num)
        {
            std::cout << "binary_search_count : " << binary_search_count << '\n'; break;
        }
    }
    
    std::cout << "__________________" << '\n';
    return 0;
}