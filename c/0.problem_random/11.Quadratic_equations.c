#include <stdio.h>
#include <math.h>
int main()
{
    float a, b, c, result1, result2, root_result; a = b = c = 0;
    scanf("%f %f %f", &a, &b, &c);
    root_result = sqrt((b*b) - (4*a*c));
    result1 = (-b + root_result) / (2*a); result2 = (-b - root_result) / (2*a);
    printf("x = "); printf("%.2f\n", result1);
    printf("x = "); printf("%.2f\n", result2);
    return 0;
}