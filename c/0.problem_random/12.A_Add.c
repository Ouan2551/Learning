#include <stdio.h>
#include <string.h>
void combine_numbers(char* a, char* b, char* result)
{
    int len_a = strlen(a); int len_b = strlen(b);
    int carry = 0, i = len_a - 1, j = len_b -1, k = 100;
    result[k--] = '\0';
    while(i >= 0 || j >= 0 || carry)
    {
        int digit_a = (i >= 0) ? a[i--] - '0' : 0;
        int digit_b = (j >= 0) ? b[j--] - '0' : 0;

        int sum = digit_a + digit_b + carry;
        result[k--] = (sum % 10) + '0';
        carry = sum / 10;
    }

    // shift result to the start of array
    int start = k + 1;
    int len = 100 - start;
    for(int x = 0; x <= len; x++)
        result[x] = result[start + x];
    
}
int main()
{
    char a[100], b[100], result[101];
    scanf("%99s %99s", a, b);
    // printf("%s\n", a); printf("%s\n", b);
    combine_numbers(a, b, result);
    printf("%s", result);
    return 0;
}