import json
from models import Student
import argparse

def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Student.from_dict(obj) for obj in data]

print(students_to_json([Student(fio='JohnDow', birthdate='2021-02-15', group='GRP-101', gpa=4.6), Student(fio='VladDementev', birthdate='2001-03-15', group='GRP-102', gpa=4.85)], 'data/lab08/students_output.json'))