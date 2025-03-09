import random

def get_numbers_ticket( min:int, max:int, quantity:int ) -> list[int]: 
    try:
        # перевірка параметрів функції 
        if not (min >= 1 and max <= 1000 and quantity <= (max-min)):
            return []
        # перехват помилки, якщо не вірні вхідні параметри
    except TypeError:
        print('Not valid value params')
        return []      
    numbers_list = []
    # цикл робить список номерів лотереї
    for i in range(min,max+1):
        numbers_list.append(i)
    # генерація випадкової комбінації зі списку номерів лотереї
    comb_list = random.sample(numbers_list,quantity)
    # сортування списку 
    comb_list.sort()
    return comb_list

test = get_numbers_ticket(1,36,5)
print(test)