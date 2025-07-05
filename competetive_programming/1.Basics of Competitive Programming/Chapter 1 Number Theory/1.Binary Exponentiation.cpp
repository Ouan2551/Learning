#include <iostream>

long long power(long long A, long long B)
    {
        if (B == 0)
        {
            return 1;
        }
        long long res = power(A, B / 2);
        if (B % 2 == 1) // odd num
            return res * res * A;
        else if (B % 2 == 0) // even num
            return res * res;
    }

int main()
{
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    // Binary exponentiation is way to calculate power of a number very quickly
    std::cout << power(2, 12) << '\n';
    return 0;
}