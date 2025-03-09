from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    birthday_list = []
    today = datetime.today().date()
    # перебираємо список users, генеруємо дату народження та переводимо у поточний рік,
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        # перевірка минулого дня народження та перевод на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # рахуємо різницю в днях від тепер до дня народження
        days_to_birthday = (birthday_this_year - today).days
        
        # перевірка на дня народження на наступний тиждень
        if 0 <= days_to_birthday < 7:
            # перевірка та коригування вихідних днів
            if birthday_this_year.weekday() >= 5:
                days_to_birthday = days_to_birthday + 7 - birthday_this_year.weekday()
                
            # формування дати привітання
            congratulation_date = today + timedelta(days=days_to_birthday)

            birthday_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return birthday_list


users = [
    {"name": "John Doe", "birthday": "1982.04.27"},
    {"name": "Jane Smith", "birthday": "2000.03.15"},
    {"name": "Eva Braun", "birthday": "1995.02.25"},
    {"name": "Peter Brom", "birthday": "1972.03.10"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)