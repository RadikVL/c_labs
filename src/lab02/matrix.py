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


a = [[1,2],
     [2,3,5], 
     [2,5]]
print(*a)
