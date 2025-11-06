def month_to_season(month):
    
    if not 1 <= month <= 12:
        return "Неверный номер месяца"

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"
print(month_to_season(2))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(11))