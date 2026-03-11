#include <iostream>
#include <vector>
int main()
{
    std::vector<int> number = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (int i = 0; i < number.size(); i += 2)
    {
        std::cout << number[i] << " ";
    }
    return 0;
}