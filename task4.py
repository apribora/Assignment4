# Припустимо, це результат з попереднього завдання
processed_results = [
    {'student_name': 'Анна', 'score': 91, 'passed': True},
    {'student_name': 'Богдан', 'score': 58, 'passed': False},
    {'student_name': 'Вікторія', 'score': 75, 'passed': True},
    {'student_name': 'Григорій', 'score': 45, 'passed': False}
]

# 1. Створіть новий, порожній список successful_students.
successful_students = []

# 2. Пройдіться циклом по списку processed_results. Якщо значення ключа "passed" для студента дорівнює True, додайте весь словник цього студента до списку successful_students.
for student in processed_results:
    if student['passed']:
        successful_students.append(student)

# 3. Для нового списку successful_students:
    # Виведіть, скільки всього студентів склали іспит.
print(f"Кількість студентів, які склали іспит: {len(successful_students)}")

    # Обчисліть та виведіть їхній середній бал.
total_score = 0
for student in successful_students:
    total_score += student['score']

average_score = total_score / len(successful_students) if successful_students else 0
print(f"Середній бал студентів, які склали іспит: {average_score}")
