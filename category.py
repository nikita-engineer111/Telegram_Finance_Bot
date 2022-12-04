import database

def create_category(massage_text):
    massage_text = str(massage_text).split()
    name_category = massage_text[1]
    created = database.create_category(name_category)
    response = f'Категория {name_category} добавлена!' if created else f'Категория {name_category} уже существует!\n' \
                                                                       f'Попробуйте назвать как-то по-другому.'
    return response

def show_categories():
    return database.show_categories()