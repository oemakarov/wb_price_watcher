
from lib.wb import WB
from config import products_setup

wb = WB()


def get_pric_limit(id: int):
    for p in products_setup:
        if p.get('id') == id:
            return p.get('price_limit')


product_ids = [ p.get('id') for p in products_setup ]
products = wb.get_products_data(product_ids)

for p in products:
    print(f'{p.id} - {p.brand} {p.name} - {p.price} руб ({get_pric_limit(p.id)})')