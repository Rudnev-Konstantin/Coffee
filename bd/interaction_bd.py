"""Это модуль для взаимодействия с базой данных"""

import sqlite3 as bd


# функция для добавления записи
def add_data(variety_name="Variety Name", roast_level="Medium", grind_type="Ground",
             taste_description="description...", price=0, package_volume="500g"):
    with bd.connect("coffee.sqlite") as con:
        cur = con.cursor()
        
        cur.execute(f"""
        INSERT INTO 
        coffee([название сорта], [степень обжарки], [молотый/в зернах], [описание вкуса], [цена], [объем упаковки])
        VALUES
        ({variety_name}, {roast_level}, {grind_type}, {taste_description}, {price}, {package_volume})
        """)


# функция для добавления шаблонных записей в таблицу
def add_template_data():
    with bd.connect("coffee.sqlite") as con:
        cur = con.cursor()
        
        cur.execute("""
        INSERT INTO 
        coffee([название сорта], [степень обжарки], [молотый/в зернах], [описание вкуса], [цена], [объем упаковки])
        VALUES
        ('Ethiopian Yirgacheffe', 'Light', 'Whole Bean',
        'Floral and citrus notes with a bright acidity', 12.99, '250g'),
        ('Colombian Supremo', 'Medium', 'Ground', 'Balanced with a smooth body and nutty flavor', 9.99, '500g'),
        ('Sumatra Mandheling', 'Dark', 'Whole Bean', 'Bold and earthy with low acidity', 14.99, '200g'),
        ('Guatemalan Antigua', 'Medium', 'Ground', 'Rich and spicy with a chocolatey finish', 11.99, '400g'),
        ('Brazilian Santos', 'Light', 'Whole Bean', 'Sweet and nutty with a mild body', 8.99, '300g')
        """)


# функция для получения данных из бд
def data_acquisition():
    with bd.connect("coffee.sqlite") as con:
        cur = con.cursor()
        
        result = cur.execute("""
        SELECT 
        [название сорта], [степень обжарки], [молотый/в зернах], [описание вкуса], [цена], [объем упаковки]
        FROM coffee
        """).fetchall()
        
        return result
