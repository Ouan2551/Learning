#include <stdio.h>
int main()
{
    int num; // not declare size need '&' to input
    scanf("%d", &num); // & means store to memory address
    printf("%d\n", num);

    getchar(); // consume \n left in the buffer
    // if not using this char1 will be value \n instead of whatever that you input

    char char1, char2;
    scanf("%c%c", &char1, &char2);
    printf("%c %c %c\n", char1,' ',char2);

    char char3[10]; // already declare don't need '&'
    scanf("%s", char3);
    printf("%s\n", char3);

    // get line of text using 'fgets()'
    char char4[10];
    fgets(char4, sizeof(char4), stdin);
    printf("%s\n", char4);
    return 0;
}