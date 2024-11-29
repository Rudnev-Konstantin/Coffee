"""Это скрипт для добавления данных в бд"""

import sqlite3 as bd

# добавляю шаблонные записи в таблицу
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
