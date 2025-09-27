#include <stdio.h>
int main() {
    float a, b;
    printf("a: ");
    scanf("%f", &a);
    printf("b: ");
    scanf("%f", &b);
    printf("Sum=%.2f; Avg=%.2f \n", a+b, (a+b)/2);
    return 0;
}