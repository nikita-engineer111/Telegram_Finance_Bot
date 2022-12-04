import database

def add_purchase(massage_text):
    massage_text = str(massage_text).split(',')
    date = massage_text[0].split()[1]
    product = massage_text[1]
    amount = massage_text[2]
    category = massage_text[3].replace(' ','')
    added = database.add_purchase(date, product, amount, category)
    response = f'Покупка {product} добавлена!' if added else f'Категория {category} не найдена!\n' \
                                                             f'Чтобы добавить категорию напиши команду /create_category'
    return response