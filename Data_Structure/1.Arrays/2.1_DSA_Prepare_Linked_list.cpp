#include <iostream>
int main()
{
    std::ios::sync_with_stdio(0);std::cin.tie(0);std::cout.tie(0);
    // 1) Pointers
    std::cout << "___get address memory" << '\n';
    std::string value = "food";
    std::cout << value << '\n';
    std::cout << &value << '\n'; // memory allocate

    std::cout << "___creat pointer" << '\n';
    std::string* value_copy = &value; // creat pointer
    std::cout << value_copy << '\n'; // output memory allocate with pointer
    std::cout << *value_copy << '\n'; // output value that variable

    std::cout << "___change value from pointer" << '\n';
    *value_copy = "Hello world";
    std::cout << value_copy << '\n';
    std::cout << value << '\n';

    std::cout << "____________________" << '\n';

    // 2) Struct
    std::cout << "Struct" << '\n';
    struct 
    {
        int num;
        std::string address;
    } test_struct1, test_struct2;
    struct car
    {
        int plate;
        std::string location;
    };
    
    // assign value
    test_struct1.num = 100; test_struct1.address = "Hello bro";
    std::cout << test_struct1.num << ' ' << test_struct1.address << '\n';
    
    test_struct2.num = 999; test_struct2.address = "How is going";
    std::cout << test_struct2.num << ' ' << test_struct2.address << '\n';

    car my_car1;
    my_car1.location = "Thailand"; my_car1.plate = 1234;
    return 0;
}