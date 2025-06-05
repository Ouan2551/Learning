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

    // bubble sort
    return 0;
}