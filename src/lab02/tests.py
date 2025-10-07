from matrix import check_rectangular, transpose, row_sums, col_sums
from arrays import min_max, unique_sorted, flatten
from tuples import format_record

def print_matrix_tests():
    print('transpose([[1,2],[3,4]]):', transpose([[1,2],[3,4]]))
    print('transpose([]):', transpose([]))
    print('transpose([[1],[2,3]]):', transpose([[1],[2,3]]))
    print('row_sums([[1,2],[3,4]]):', row_sums([[1,2],[3,4]]))
    print('row_sums([]):', row_sums([]))
    print('row_sums([[1],[2,3]]):', row_sums([[1],[2,3]]))
    print('col_sums([[1,2],[3,4]]):', col_sums([[1,2],[3,4]]))
    print('col_sums([]):', col_sums([]))
    print('col_sums([[1],[2,3]]):', col_sums([[1],[2,3]]))

def print_arrays_tests():
    print('min_max([1,2,3]):', min_max([1,2,3]))
    print('min_max([-1,0,1]):', min_max([-1,0,1]))
    print('min_max([]):', min_max([]))
    print('unique_sorted([3,1,2,1]):', unique_sorted([3,1,2,1]))
    print('unique_sorted([]):', unique_sorted([]))
    print('flatten([[1,2],[3,4]]):', flatten([[1,2],[3,4]]))
    print('flatten([(1,2),(3,4)]):', flatten([(1,2),(3,4)]))
    print('flatten([[1,"a"],[2,3]]):', flatten([[1,"a"],[2,3]]))
    print('flatten([1,2,3]):', flatten([1,2,3]))

def print_tuples_tests():
    print('format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)):', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print('format_record(("Петров Петр", "ABB-01", 3.99)):', format_record(("Петров Петр", "ABB-01", 3.99)))
    print('format_record(("Петров", "ABB-01", 3.99)):', format_record(("Петров", "ABB-01", 3.99)))
    print('format_record(("сидорова анна сергеевна", "ABB-01", 3.999)):', format_record(("сидорова анна сергеевна", "ABB-01", 3.999)))

if __name__ == "__main__":
    print("--- Matrix tests ---")
    print_matrix_tests()
    print("\n--- Arrays tests ---")
    print_arrays_tests()
    print("\n--- Tuples tests ---")
    print_tuples_tests()
