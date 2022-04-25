import sqlite3


class TableCreate:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_tables(self):
        sql_create_category_table = """ CREATE TABLE IF NOT EXISTS category (
                                        category_id INT PRIMARY KEY,
                                        category_name TEXT NOT NULL
                                    ); """
        sql_create_goods_table = """CREATE TABLE IF NOT EXISTS goods (
                                    goods_id INT PRIMARY KEY,
                                    goods_name TEXT NOT NULL,
                                    goods_price FLOAT,
                                    reference_id INT NOT NULL,
                                    FOREIGN KEY(reference_id) REFERENCES category(category_id)
                                );"""

        self.cur.execute(sql_create_category_table)
        self.cur.execute(sql_create_goods_table)

        self.conn.commit()

    def insert_category(self, category):
        self.cur.execute("INSERT INTO category VALUES(?, ?);", category)
        self.conn.commit()

    def insert_goods(self, goods):
        self.cur.execute("INSERT INTO goods VALUES(?, ?, ?, ?);", goods)
        self.conn.commit()

    def print_data(self):
        self.cur.execute("SELECT * FROM category;")
        category = self.cur.fetchall()
        self.cur.execute(("SELECT * FROM goods;"))
        goods = self.cur.fetchall()
        print(category)
        print(goods)



base = TableCreate('pythonsqlite.db')
base.create_tables()
# base.insert_category((3, 'Cars'))
base.insert_goods((2, 'IPhone', 1000, 5))
base.print_data()
