import random

grades = [random.randint(1,100) for _ in range(7)]
print(f"Исходный баллы: {grades}")

min_grade = min(grades)
max_grade = max(grades)
print(f"Минимум: {min_grade}. Максимум: {max_grade}")

remainig_grades = grades.copy()
remainig_grades.remove(min_grade)
remainig_grades.remove(max_grade)
print(f"Оставшиеся баллы: {remainig_grades}")

print(f"Среднее ариф: {sum(remainig_grades) / len(remainig_grades)}")