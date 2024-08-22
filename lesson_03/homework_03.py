alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."""
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Count single quotes:", alice_in_wonderland.count("'"))
print(f"Print variable: \n{alice_in_wonderland}")


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
total_area = area_black_sea + area_azov_sea
print(f"Total area seas: {total_area} km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
quantity_goods_all_warehouse = 375291
quantity_goods_third_warehouse = quantity_goods_all_warehouse - 250449
quantity_goods_second_warehouse = 222950 - quantity_goods_third_warehouse
quantity_goods_first_warehouse = 250449 - quantity_goods_second_warehouse
print(f"Quantity goods in the first warehouse: {quantity_goods_first_warehouse} pieces")
print(f"Quantity goods in the first warehouse: {quantity_goods_second_warehouse} pieces")
print(f"Quantity goods in the first warehouse: {quantity_goods_third_warehouse} pieces")
# print(quantity_goods_first_warehouse + quantity_goods_second_warehouse + quantity_goods_third_warehouse)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment_for_a_computer = 1179
cost_of_the_computer = monthly_payment_for_a_computer * 18
print(f"Cost of the computer: {cost_of_the_computer}")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print(f"Remainder of dividing 'a)': {a}")
b = 9907 % 9
print(f"Remainder of dividing 'b)': {b}")
c = 2789 % 5
print(f"Remainder of dividing 'c)': {c}")
d = 7248 % 6
print(f"Remainder of dividing 'd)': {d}")
e = 7128 % 5
print(f"Remainder of dividing 'e)': {e}")
f = 19224 % 9
print(f"Remainder of dividing 'f)': {f}")



# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
cost_of_large_pizzas = 274
large_pizzas = 4
cost_of_medium_pizzas = 218
medium_pizzas = 2
cost_of_juice = 35
juices = 4
cost_of_pie = 350
pies = 1
cost_of_water = 21
water = 3
total_cost_of_large_pizzas = cost_of_large_pizzas * large_pizzas
total_cost_of_medium_pizzas = cost_of_medium_pizzas + medium_pizzas
total_cost_of_juices = cost_of_juice * juices
total_cost_of_pie = cost_of_pie * pies
total_cost_of_water = cost_of_water * water
print(f"Amount of money will be needed for this her order: {total_cost_of_large_pizzas + total_cost_of_medium_pizzas + total_cost_of_juices + total_cost_of_pie + total_cost_of_water} uah")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
quantity_of_photos = 232
quantity_per_page = 8
how_many_pages_will_be_needed = quantity_of_photos / quantity_per_page
print(f"Pages will be needed to paste all the photos: {int(how_many_pages_will_be_needed)}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_between_cities = 1600
tank_capacity = 48
fuel_consumption_per_100_km = 9
quantity_liters_gasoline_for_trip = distance_between_cities / 100 * fuel_consumption_per_100_km
will_have_to_refuel = quantity_liters_gasoline_for_trip / tank_capacity
print(f"The quantity of liters of gasoline will be needed: {int(quantity_liters_gasoline_for_trip)} liters")
print(f"Will have to refuel: {int(will_have_to_refuel)}")