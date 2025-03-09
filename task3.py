import re

def normalize_phone(phone_number):
    # видаляю всі символи крім цифр та '+'
    norm_number = re.sub(r"\D", "", phone_number)
    # Перевірка, якщо номер починається із '+'
    if not norm_number.startswith("+"):
        # Додаю код '+38', якщо його немає
        norm_number = "+38" + norm_number.lstrip("38")

    return norm_number


raw_numbers = [
    "    +38(050)123-32-343442323434",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)