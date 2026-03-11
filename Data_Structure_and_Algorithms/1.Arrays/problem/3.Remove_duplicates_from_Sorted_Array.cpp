#include <iostream>
#include <vector>
int main()
{
    std::vector<int> arr = {1, 2, 2, 3, 4, 4, 4, 5, 5};
    std::vector<int> arr_complete = {};
    for (size_t i = 0; i < arr.size(); i++)
    {
        bool check = false;
        for (size_t j = i+1; j < arr.size(); j++)
        {
            if (arr[i] == arr[j])
            {
                check = true; break;
            }
        }
        if (check == false)
        {
            arr_complete.push_back(arr[i]);
        }
    }
    for (size_t i = 0; i < arr_complete.size(); i++)
    {
        std::cout << arr_complete[i] << ' ';
    }
    return 0;
}