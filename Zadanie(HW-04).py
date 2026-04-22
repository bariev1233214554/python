import json
from collections import defaultdict
with open("translator.json", "r") as my_file:
   orders = json.load(my_file)
   #print(orders)
max_price = 0
max_order_num = ''
max_quantity = 0
max_quantity_order = ''
order_count_by_day = defaultdict(int)
max_orders_day = ''
user_order_count = defaultdict(int)
top_user_by_count = ''
user_total_spent = defaultdict(float)
top_user_by_spent = ''
total_order_value = 0
total_items_count = 0
order_count = 0
for order_num, order_data in orders.items():
    price = order_data['price']
    quantity = order_data['quantity']
    date = order_data['date']
    user_id = order_data['user_id']
    order_count += 1
    total_order_value += price
    total_items_count += quantity
    if price > max_price:
        max_price = price
        max_order_num = order_num
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order_num = order_num
    order_count_by_day[date] += 1
    user_order_count[user_id] += 1
    user_total_spent[user_id] += price
max_orders_count = max(order_count_by_day.values())
max_orders_day = [day for day, count in order_count_by_day.items() if count == max_orders_count][0]
max_user_orders = max(user_order_count.values())
top_user_by_count = [user for user, count in user_order_count.items() if count == max_user_orders][0]
max_spent = max(user_total_spent.values())
top_user_by_spent = [user for user, spent in user_total_spent.items() if spent == max_spent][0]
average_order_price = total_order_value / order_count if order_count > 0 else 0
average_item_price = total_order_value / total_items_count if total_items_count > 0 else 0
print(f"Номер заказа с самой большой стоимостью: {max_order_num}, стоимость заказа: {max_price}")
print(f"Номер заказа с самым большим количеством товаров: {max_quantity_order_num}, количество: {max_quantity}")
print(f"День с наибольшим числом заказов: {max_orders_day} ({max_orders_count} заказов)")
print(f"Пользователь с наибольшим числом заказов: {top_user_by_count}")
print(f"Пользователь с наибольшей суммарной стоимостью заказов: {top_user_by_spent}")
print(f"Средняя стоимость заказа: {average_order_price:.2f}")
print(f"Средняя стоимость товара: {average_item_price:.2f}")
