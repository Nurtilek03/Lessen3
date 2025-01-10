# import sqlite3

#  Инициализация базы данных
# def init_db():
#     conn = sqlite3.connect('orders.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         product TEXT,
#         address TEXT,
#         phone TEXT
#     )''')
#     conn.commit()
#     return conn, cursor

# # Сохранение данных в базу данных
# def save_order_to_db(conn, cursor, user_data, user_id):
#     cursor.execute('''INSERT INTO orders (user_id, product, address, phone) VALUES (?, ?, ?, ?)''',
#                    (user_id, user_data['product'], user_data['address'], user_data['phone']))
#     conn.commit()
