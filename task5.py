sales_data = [

    {"product": "Смартфон", "category": "Електроніка",
     "quantity": 1, "price": 15000},

    {"product": "Книга 'Python для всіх'", "category":
        "Книги", "quantity": 2, "price": 700},

    {"product": "Навушники", "category": "Електроніка",
     "quantity": 2, "price": 2500},

    {"product": "Чайник", "category": "Побутова техніка",
     "quantity": 1, "price": 1200},

    {"product": "Книга 'Алгоритми'", "category": "Книги",
     "quantity": 1, "price": 900},

    {"product": "Ноутбук", "category": "Електроніка",
     "quantity": 1, "price": 32000}
]

# 1. Створіть новий порожній словник під назвою category_report.
category_report = {}

# 2. Напишіть цикл, що проходить по списку sales_data. Для кожного продажу:
# ○ Визначте його категорію.
# ○ Якщо такої категорії ще немає в category_report, створіть для неї
#   новий ключ. Значенням для цього ключа має бути словник з початковими даними,
#   наприклад: {'total_revenue': 0, # 'total_items_sold': 0}.
# ○ Оновіть дані для цієї категорії:
#   ■ Збільште загальний дохід (total_revenue) на вартість цієї транзакції (quantity * price).
#   ■ Збільште загальну кількість проданих одиниць
#     (total_items_sold) на кількість товарів у цій транзакції (quantity).

for sale in sales_data:
    category = sale["category"]

    if category not in category_report:
        category_report[category] = {
            'total_revenue': 0,
            'total_items_sold': 0
        }
    transaction_value = sale["quantity"] * sale["price"]
    category_report[category]["total_revenue"] += transaction_value
    category_report[category]["total_items_sold"] += sale["quantity"]

# 3. Виведіть фінальний словник category_report у зручному для читання форматі.

print("Звіт за категоріями:")
print("-" * 30)
for category, data in category_report.items():
    print(f"Категорія: {category}")
    print(f"Загальний дохід: {data['total_revenue']} грн")
    print(f"Кількість проданих одиниць: {data['total_items_sold']}")
    print()
print("-" * 30)
print(f"Всього категорій: {len(category_report)}")