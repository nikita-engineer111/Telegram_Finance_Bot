help_massage = f'- Добавлять твои покупки в базу (/add_purchase) 🙃\n' \
           f'- Показывать статистику твоих покупок (/show_statistics)🤓\n' \
           f'- Создавать категории (/create_category)\n' \
               f'- Показывать все категории (/show_categories)'

def start_response(user_name):
    return f'Приветствую, {user_name}!🤚🏻\n' \
           f'Я - твой финансовый помощник 🤖\n' \
           f'Вот, что я могу (/help):\n' \
           f'{help_massage}'

def help_response():
    return f'Вот, что я могу:\n' \
           f'{help_massage}'

def add_purchase():
    return f'Чтобы добавить покупку в базу, напиши \n' \
           f'/add_purchase дату покупки в формате 03.12.2022, а потом через запятую название товара, сумму покупки и к какой категории относится покупка, например:\n\n' \
           f'/add_purchase 03.12.2022, Кофе со сливками, 150, Напитки'

def show_statistics():
    return f'Чтобы посмотреть статистику для начало уточни какие данные ты хочешь посмотреть:\n\n' \
           f'- Посмотреть  покупки по категории за период:\n' \
           f'/show_statistics и через пробел вписав название категории и период времени, например:\n' \
           f'/show_statistics транспорт сентябрь\n' \
           f'Если хочешь за всё время, то:\n' \
           f'/show_statistics транспорт all\n\n' \
           f'- Посмотреть покупки по всем категориям за месяц, например:\n' \
           f'/show_statistics all сентябрь\n\n' \
           f'- Посмотреть покупки по всем категориям за всё время, например:\n' \
           f'/show_statistics all all\n\n' \
           f'- Посмотреть покупки, сумма которых превышает выбранной, например:\n' \
           f'/show_statistics более 1000\n\n' \
           f'- Посмотреть покупки, сумма которых менее выбранной, например:\n' \
           f'/show_statistics менее 1000\n\n'

def create_category():
    return f'Чтобы создать категорию напиши\n' \
           f'/create_category и через пробел название категории, например:\n' \
           f'/create_category Транспорт'

def trash():
    return f'Я умею отвечать только на команды🤷🏻‍♂️\n' \
           f'Список команд можно посмотреть в /help'