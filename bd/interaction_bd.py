"""Это модуль для взаимодействия с базой данных"""

import sqlite3 as bd


# функция для добавления записи
def add_data(variety_name="Variety Name", roast_level="Medium", grind_type="Ground",
             taste_description="description...", price=0, package_volume="500g"):
    with bd.connect("bd/coffee.sqlite") as con:
        cur = con.cursor()
        
        cur.execute(f"""
        INSERT INTO 
        coffee(variety_name, roast_level, grind_type, taste_description, price, package_volume)
        VALUES
        ("{variety_name}", "{roast_level}", "{grind_type}", "{taste_description}",
        {price}, "{package_volume}")
        """)


# функция для изменения записи
def edit_data(id_title, variety_name="Variety Name", roast_level="Medium", grind_type="Ground",
              taste_description="description...", price=0, package_volume="500g"):
    with bd.connect("bd/coffee.sqlite") as con:
        cur = con.cursor()
        
        try:
            id_title = int(id_title)
        except ValueError:
            pass
        
        cur.execute(f"""
        UPDATE coffee
        SET roast_level = "{roast_level}", grind_type = "{grind_type}",
            taste_description = "{taste_description}", variety_name = "{variety_name}",
            price = {price}, package_volume = "{package_volume}"
        WHERE id = ? OR variety_name = ?
        """, (id_title, id_title))
        
        print("Вроде хотяб без ишибки", id_title)


# функция для добавления шаблонных записей в таблицу
def add_template_data():
    with bd.connect("bd/coffee.sqlite") as con:
        cur = con.cursor()
        
        cur.execute("""
        INSERT INTO 
        coffee(variety_name, roast_level, grind_type, taste_description, price, package_volume)
        VALUES
        ('Ethiopian Yirgacheffe', 'Light', 'Whole Bean',
        'Floral and citrus notes with a bright acidity', 12.99, '250g'),
        ('Colombian Supremo', 'Medium', 'Ground', 'Balanced with a smooth body and nutty flavor', 9.99, '500g'),
        ('Sumatra Mandheling', 'Dark', 'Whole Bean', 'Bold and earthy with low acidity', 14.99, '200g'),
        ('Guatemalan Antigua', 'Medium', 'Ground', 'Rich and spicy with a chocolatey finish', 11.99, '400g'),
        ('Brazilian Santos', 'Light', 'Whole Bean', 'Sweet and nutty with a mild body', 8.99, '300g')
        """)


# функция для получения данных из бд
def data_acquisition(id_title=None):
    with bd.connect("bd/coffee.sqlite") as con:
        cur = con.cursor()
        
        if id_title is None:
            result = cur.execute("""SELECT * FROM coffee""").fetchall()
        else:
            try:
                id_title = int(id_title)
            except ValueError:
                pass
            
            result = cur.execute('''
            SELECT * FROM coffee
            WHERE id = ? OR variety_name = ?
            ''', (id_title, id_title)).fetchone()
        
        return result
