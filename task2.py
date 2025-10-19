deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08, # 8% річних
    "is_active": True
}

# 1. Обчисліть суму нарахованих відсотків за рік (сума = баланс * відсоткова_ставка).
interest = deposit_account["balance"] * deposit_account["interest_rate"]

# 2. Оновіть значення ключа "balance", додавши до нього нараховані відсотки.
deposit_account["balance"] += interest

# 3. Додайте до словника новий ключ "last_update_type" зі значенням "interest accrual".
deposit_account["last_update_type"] = "interest accrual"

# 4. Змініть значення ключа "is_active" на False, ніби клієнт закрив рахунок.
deposit_account["is_active"] = False

# 5. Виведіть на екран фінальний оновлений словник.
print(deposit_account)
