from datetime import datetime

def get_days_from_today(date):
    try:
        # генерую дату зі строки по формату
        start = datetime.strptime(date,"%Y-%m-%d").date()
        print(start)
    except ValueError:
        print(f"{date} is not valid date")
        return
    # генерую поточну дату
    now_dt=datetime.now().date()
    print(now_dt)
    # рахую різницю між датами
    delta = now_dt.toordinal() - start.toordinal() 
    return int(delta)


# перевірка роботи функції
str_date="2021-10-9"

test = get_days_from_today(str_date)
print(test)