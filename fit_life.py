# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
WATER_IN_LITER = 1000

# приветствие
print('-'*30) # разделитель для красоты
print('Добро пожаловать в программу FitLife.')
print('Данная программа рассчитает Индекс Массы Тела(ИМТ) и нормы воды.')
print('-'*30) # разделитель для красоты

# Знакомство с пользователем
user_name = input('Для начала давай познакомимся, как тебя зовут? ')
user_age = int(input('Сколько тебе полных лет? '))

# Сбор данных
try:
    user_weight = float(input('Укажи свой вес, в кг (напр. 82.9): '))   
except ValueError:
    user_weight = float(input('!!!ОШИБКА!!!: Укажи через точку: '))
try:
    user_height = float(input('Укажи свой рост, в метрах (напр. 1.76): '))
except ValueError:
    user_height = float(input('!!!ОШИБКА!!!: Укажи через точку: '))
print('-'*30) # разделитель для красоты

# расчёт массы тела и нормы воды в мл
bmi = round((user_weight / (user_height ** 2)), 1)
water_ml = user_weight * WATER_PER_KG
water_needed = round((water_ml / WATER_IN_LITER), 1) # перевод из мл в литры

# вывод результатов расчета
print(f'Привет, {user_name}! Ознакомься с результатами:')
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
print('-'*30) # разделитель для красоты
