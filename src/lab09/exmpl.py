from group import Group
from models import Student

g = Group("data/lab09/students.csv")

print("=== list() ===")
print(*g.list()[:3], sep="\n")

print("\n=== add() ===")
s = Student("Тестовый Студент", "2005-05-05", "TEST-01", 4.5)
g.add(s)
print("Добавлен:", s)

print("\n=== find('Тест') ===")
print(g.find("Тест"))

print("\n=== update() ===")
g.update("Тестовый Студент", gpa="4.9")
print(g.find("Тест"))

print("\n=== remove() ===")
g.remove("Тестовый Студент")
print(g.find("Тест"))

print("\n=== stats() ===")
print(g.stats())
