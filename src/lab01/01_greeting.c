#include <stdio.h>
int main() {
    char name[100];
    int age;
    printf("Имя: ");
    scanf("%99s", name);
    printf("Возраст: ");
    scanf("%d", &age);
    age += 1;
    printf("Привет, %s! Через год тебе будет %d. \n", name, age);
    return 0;
}