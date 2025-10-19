book_profile = {
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info": {
    "name": "Наукова думка",
    "city": "Київ"
    }
}

# 1. Отримайте назву книги та ім'я її автора.
title = book_profile["title"]
author = book_profile["author"]

# 2. Отримайте назву видавництва з вкладеного словника.
publisher_name = book_profile["publisher_info"]["name"]

# 3. Напишіть код, який виводить інформацію у вигляді речення: Книга "[назва]" автора [автор] була видана у місті [місто].
city = book_profile["publisher_info"]["city"]
print(f"Книга \"{title}\" автора {author} була видана у місті {city}.")

# 4. Перевірте, чи є у словнику book_profile ключ "year". Якщо він є, виведіть його значення, якщо ні — повідомлення "Рік видання невідомий".
if "year" in book_profile:
    print(book_profile["year"])
else:
    print("Рік видання невідомий")