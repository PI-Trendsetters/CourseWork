from flask import Flask, render_template, request

app = Flask(__name__)


# Логика расчета стоимости
def calculate_cleaning_cost(area, rate, discount, additional_services):
    base_cost = area * rate  # Стоимость без скидки
    discount_amount = base_cost * (discount / 100)  # Скидка
    additional_cost = sum(additional_services.values())  # Дополнительные услуги
    total_cost = base_cost - discount_amount + additional_cost  # Общая стоимость
    return round(total_cost, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получение данных из формы
        area = float(request.form.get("area"))
        rate = float(request.form.get("rate"))
        discount = float(request.form.get("discount", 0))

        # Дополнительные услуги
        services = {
            "disinfection": 500 if "disinfection" in request.form else 0,
            "window_cleaning": 300 if "window_cleaning" in request.form else 0
        }

        # Расчет стоимости
        total_cost = calculate_cleaning_cost(area, rate, discount, services)
        return render_template("Calculator.html", total_cost=total_cost, area=area, rate=rate, discount=discount,
                               services=services)

    return render_template("Calculator.html", total_cost=None)


if __name__ == "__main__":
    app.run(debug=True)
