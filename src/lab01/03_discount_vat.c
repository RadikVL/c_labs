#include <stdio.h>
int main() {
    float price, discount, vat;
    printf("Price: ");
    scanf("%f", &price);
    printf("Discount: ");
    scanf("%f", &discount);
    printf("Vat: ");
    scanf("%f", &vat);
    float base = price * (1 - discount / 100);
    float vat_amount = base * vat / 100;
    float total = base + vat_amount;
    printf("База после скидки: %.2f ₽ \n", base);
    printf("НДС:               %.2f ₽ \n", vat_amount);
    printf("Итого к оплате:    %.2f ₽ \n", total);
    return 0;
}