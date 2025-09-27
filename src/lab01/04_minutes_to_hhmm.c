#include <stdio.h>
int main() {
    int minutes;
    printf("Минуты: ");
    scanf("%d", &minutes);
    int hours = minutes / 60;
    int mins = minutes % 60;
    printf("%d:%02d\n", hours, mins);
    return 0;
}