def format_record(rec: tuple[str, str, float]) -> str:
    s = rec[0].split()
    if len(s) == 3:
        return f'{s[0].capitalize()} {s[1][0].upper()}.{s[2][0].upper()}., гр. {rec[1]}, GPA {rec[2]:.2f}'
    elif len(s) == 2:
        return f'{s[0].capitalize()} {s[1][0].upper()}., гр. {rec[1]}, GPA {rec[2]:.2f}'
    return ValueError('Неверный формат ФИО')
    


# test_tuple = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
# "Иванов И.И., гр. BIVT-25, GPA 4.60"
# print(format_record(test_tuple))