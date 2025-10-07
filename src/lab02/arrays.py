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