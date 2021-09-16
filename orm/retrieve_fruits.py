from fruits_db import session, Fruit

fruits = session.query(Fruit).all()
for fruit in fruits:
    print()
    print(f'Fruit: { fruit.name }')
    print(f'Price: { fruit.price_cents } cents')