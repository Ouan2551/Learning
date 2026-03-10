#include <iostream>
#include <vector>
int main()
{
    std::vector<int> numbers = {1, 2, 3, 4, 5, 2};
    std::vector<int> leaders = {};
    for (size_t i = 0; i < numbers.size(); i++)
    {
        bool check = true;
        for (size_t j = i+1; j < numbers.size(); j++)
        {
            if (numbers[i] < numbers[j] and numbers[i] != numbers[j])
            {
                check = false;
            }
        }
        if (check == true)
        {
            leaders.push_back(numbers[i]);
        }
    }
    for (size_t  i = 0; i < leaders.size(); i++)
    {
        std::cout << leaders[i] << ' ';
    }
    return 0;
}