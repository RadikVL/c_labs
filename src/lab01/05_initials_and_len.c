#include <locale.h>
#include <wchar.h>
#include <stdio.h>

void get_initials(const wchar_t *fullname, wchar_t *initials) {
    int j = 0;
    for (int i = 0; fullname[i] != L'\0'; i++) {
        if ((i == 0 && fullname[i] != L' ') || (fullname[i-1] == L' ' && fullname[i] != L' ' && fullname[i] != L'\n')) {
            initials[j++] = fullname[i];
        }
    }
    initials[j] = L'\0';
}

int count_symbols(const wchar_t *fullname) {
    int symbols = 0;
    for (int i = 0; fullname[i] != L'\0'; i++) {
        if (fullname[i] != L' ' && fullname[i] != L'\n') {
            symbols++;
            wprintf(L"%lc\n", fullname[i]);
        }
    }
    return symbols;
}

int main() {
    setlocale(LC_ALL, "");
    wchar_t fullname[100];
    wprintf(L"ФИО: ");
    fgetws(fullname, 100, stdin);
    int symbols = count_symbols(fullname) + 2;

    wchar_t initials[100];
    get_initials(fullname, initials);

    wprintf(L"Инициалы: %ls\n", initials);
    wprintf(L"Количество символов: %d\n", symbols);
    return 0;
}

