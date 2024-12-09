# Логика расчета стоимости
def calculate_cleaning_cost(area, rate, discount, additional_services):
    base_cost = area * rate  # Стоимость без скидки
    discount_amount = base_cost * (discount / 100)  # Скидка
    additional_cost = sum(additional_services.values())  # Дополнительные услуги
    total_cost = base_cost - discount_amount + additional_cost  # Общая стоимость
    return round(total_cost, 2)
