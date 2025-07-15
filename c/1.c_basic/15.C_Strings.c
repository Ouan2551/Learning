#include <stdio.h>
#include <string.h> //using string fucntion
int main()
{
    // string in c is just array of char
    char string[] = "Hello bro";
    printf("%s\n", string);
    printf("%c\n", string[0]); // using %c output 1 char

    // modify string
    string[5] = '!';
    printf("%c\n", string[5]);

    // loop string
    int size_string = strlen(string); // find length of string
    printf("strlen : %zu\n", strlen(string));   // 9
    printf("sizeof : %zu\n", sizeof(string));   // 10
    // as sizeof also includes the \0 character when counting
    // The string "Hello" is stored as {'H', 'e', 'l', 'l', 'o', '\0'} in memory.
    // \0 auto put into string when declare it
    for (int i = 0; i <= size_string; i++)
    {
        printf("%c", string[i]);
    }
    printf("\n");
    // example
    char greetings[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\0'};
    printf("%s", greetings);

    // special characters
    char txt[] = "We are the so-called \"Vikings\" from the north.";
    // have by this \' single quote, \" double quote, \\ blackslash
    // \n newline, \t tap, \0 null
    return 0;
}