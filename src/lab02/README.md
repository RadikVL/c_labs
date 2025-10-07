### Python BIVT-25-5 ЛР2 — Коллекции и матрицы
---
Here is code of all modules.
#### arrays.py
```
def min_max (nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: return ValueError
    return (min(nums), max(nums))

def unique_sorted (nums: list[float | int]) -> list[float | int]:
    return sorted(list(set(nums)))

def flatten(mat: list[list | tuple]) -> list:
    st = set()
    for i in mat:
        if type(i) == list or type(i) == tuple:
            for j in i:
                if type(j) == int or type(j) == float:
                    st.add(j)
                else: return TypeError
        else: return TypeError
    return list(st)
```

#### matrix.py
```
def check_rectangular(mat: list[list[float | int]]) -> bool:
    if not mat:
        return True
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return False
    return True

def transpose(mat: list[list[float | int]]) -> list | ValueError:
    if not mat:
        return []
    if check_rectangular(mat):
        return [list(col) for col in zip(*mat)]
    return ValueError("Матрица рваная (строки разной длины)")

def row_sums(mat: list[list[float | int]]) -> list[int] | list[float] | ValueError:
    if not mat:
        return []
    if check_rectangular(mat):
        return [sum(row) for row in mat]
    return ValueError("Матрица рваная (строки разной длины)")

def col_sums(mat: list[list[float | int]]) -> list[int] | list[float] | ValueError:
    if not mat:
        return []
    if check_rectangular(mat):
        return [sum(col) for col in zip(*mat)]
    return ValueError("Матрица рваная (строки разной длины)")
```

#### tuples.py
```
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
```
---

### Here is all tests for every module:
![](/images/lab02/ex_tests.png)