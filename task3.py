exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60  # Прохідний бал

# 1. Напишіть цикл, який проходить по кожному словнику у списку exam_results.
for student in exam_results:
    # 2. Всередині циклу порівняйте значення ключа "score" кожного студента зі змінною passing_score.
    if student["score"] >= passing_score:
        # 3. Додайте до кожного словника новий ключ "passed": Значення має бути True, якщо бал студента є більшим або рівним прохідному.
        student["passed"] = True
    else:
        # 3. Додайте до кожного словника новий ключ "passed": Значення має бути False, якщо бал менший.
        student["passed"] = False

    # 4. Виведіть на екран фінальний список exam_results з доданою інформацією про складання іспиту.
print(exam_results)
