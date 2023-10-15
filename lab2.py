class Product:
    def __init__(self, product, price):
        self.product = product
        self.price = price


class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products_and_price = []
        self.total_price = 0

    def add_product(self, product, price):
        self.products_and_price.append(
            Product(product=product, price=price)
        )
        self.raise_total_price(price)

    def raise_total_price(self, price):
        self.total_price += price


def add_shops():
    shops = []

    while True:
        shop_name = input('Введите название магазина: ')
        if shop_name == '0':
            break
        shops.append(Shop(shop_name))

    return shops


def collect_products():
    products_list = []
    while True:
        product = input('Введите продукт: ')
        if product == '0':
            break

        if product not in products_list:
            products_list.append(product)

    return products_list


def add_products_prices(products_list, shops):
    for shop in shops:
        for product in products_list:
            price = int(input(f'Введите цену для товара {product} в магазине {shop.shop_name}: '))
            shop.add_product(product=product, price=price)

    return shops


def main():
    help_msg_stop_add_shops = 'Введите "0" если хотите закончить ввод наименований магазинов'
    print(help_msg_stop_add_shops)

    shops = add_shops()

    print()
    help_msg_stop_add_products = 'Введите "0" если хотите закончить ввод продуктов'
    print(help_msg_stop_add_products)

    products_list = collect_products()
    shops = add_products_prices(products_list, shops)

    best_shop = shops[0].shop_name
    best_price = shops[0].total_price

    print('Итог:')
    for i, shop in enumerate(shops):
        print(f'Магазин: {shop.shop_name}, Итоговая цена: {shop.total_price}')
        if i == 0:
            continue

        if shop.total_price < best_price:
            best_shop = shop.shop_name
            best_price = shop.total_price

    print('Магазин с лучшей ценой:')
    print(f'Магазин: {best_shop}, Итоговая цена: {best_price}')


if __name__ == '__main__':
    main()
