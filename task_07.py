titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [{'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [{'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

for key, elem in titles.items():
    goods_code = elem
    goods_name = key
    total_quantity = 0
    total_price = 0
    for i in range(0, len(sales[goods_code])):
        total_quantity += sales[goods_code][i]['quantity']
        total_price +=  sales[goods_code][i]['quantity'] * sales[goods_code][i]['price']

    print(f'{goods_name}: общее количество {total_quantity}, общая стоимость {total_price} - руб.')

#     Отлично
