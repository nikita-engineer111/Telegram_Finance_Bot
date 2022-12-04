import ast
def save_databese(data):
    file = open('database.txt', 'w')
    file.write(str(data))
    file.close()

def open_database():
    file = ''
    try:
        file = open('database.txt', 'r')
    except FileNotFoundError:
        database = {'category':[],'purchases':{}}
        save_databese(database)
        open_database()
    database = ast.literal_eval(file.read())
    return database

def check_category(name_category):
    database = open_database()
    categories = ','.join(database['category'])
    return name_category in categories

def create_category(name_category):
    """
    Тут добавляется новая категория
    Для начала идёт проверка есть ли категория с таким названием,
    Если такая категория уже есть, метод вернёт False,
    Если такой категории нет, то метод добавляет категорию в базу и возвращает True
    """
    database = open_database()
    check = check_category(name_category)
    if check:
        pass
    else:
        database['category'].append(name_category)
        database['purchases'][name_category] = []
        save_databese(database)
    return not check

def show_categories():
    database = open_database()
    categories = database['category']
    categories = ',\n'.join(categories)
    return categories

def add_purchase(date, product, amount, category):
    check_cat = check_category(category)
    if check_cat:
        database = open_database()
        database['purchases'][category].append([date, product, amount])
        save_databese(database)
        return True
    else:
        return False
