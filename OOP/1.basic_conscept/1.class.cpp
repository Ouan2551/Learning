#include <iostream>
int main()
{
    std::ios::sync_with_stdio(0);std::cout.tie(0);std::cin.tie(0);
    // class => building block of oop in c++ (user define data type) like blueprint
    class Animal
    {
        public:
            std::string species;
            int age;

            void make_sound()
            {
                std::cout << "sound" << '\n';
            }
    };
    return 0;
}