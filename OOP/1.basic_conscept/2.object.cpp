#include <iostream>
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
int main()
{
    std::ios::sync_with_stdio(0);std::cout.tie(0);std::cin.tie(0);
    // Object => actual entity
    Animal bobby; // animal name bobby (specific) this call object4
    bobby.age = 10; bobby.species = "Dog";
    bobby.make_sound();
    // std::cout << bobby.age() << ' ' << bobby.species();
    return 0;
}