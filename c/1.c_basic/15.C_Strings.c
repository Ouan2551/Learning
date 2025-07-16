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
    for (int i = 0; i <= size_string; i++)
    {
        printf("%c\n", string[i]);
    }
    printf("\n");
    // example
    char greetings[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\0'};
    printf("%s\n", greetings);

    // special characters
    char txt[] = "We are the so-called \"Vikings\" from the north.";
    printf("Special char : %s\n", txt);
    // have by this \' single quote, \" double quote, \\ blackslash
    // \n newline, \t tap, \0 null

    // string functions

    // string length
    printf("strlen : %zu\n", strlen(string));   // 9
    printf("sizeof : %zu\n", sizeof(string));   // 10
    // as sizeof also includes the \0 character when counting
    // The string "Hello" is stored as {'H', 'e', 'l', 'l', 'o', '\0'} in memory.
    // \0 auto put into string when declare it

    // combine two strings using "strcat()"
    char str1[] = "Hello";
    char str2[] = " World";
    strcat(str1, str2); // str 2 to str1 (result = str1)
    printf("combine strings : %s\n", str1);

    // copy strings using "strcpy()"
    char str3[] = "";
    strcpy(str3, str1);
    printf("copy strings : %s\n", str3);

    // compare strings using "strcmp()" (return 0 mean equal)
    printf("compare str1 and str3 : %d\n", strcmp(str1, str3));
    printf("compare str1 and str2 : %d\n", strcmp(str1, str2));
    return 0;
}