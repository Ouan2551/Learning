#include <iostream>
#include <vector>
int main()
{
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    // Data Structure => way to store data it have 2 different type
    // 1) Primitive Data Structure => basic single value
    // 2) Abstract Data Structure => high level complex value
    // Algorithms => step by step how to solve problem

    // Fibonacci Numbers => first is 0, 1, but next num is the sum of two previous num
    std::cout << "Fibonacci Numbers Example" << '\n';
    long long count = 0; std::cin >> count;  std::vector<long long> fibonacci_num = {0, 1};
    for (int i = 0; i < count; i++)
    {
        long long num = fibonacci_num[i] + fibonacci_num[i+1];
        fibonacci_num.push_back(num);
        std::cout << "num : " << num << '\n';
    }
    std::cout << "__________________________" << '\n';


    return 0;
}