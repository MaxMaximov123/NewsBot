import psycopg2


# try:
#     conn = psycopg2.connect(user="thszlocyntmmgg",
#                             # пароль, который указали при установке PostgreSQL
#                             password="daea238bb862af4128bd5a075824f4e2ad4fa8242fb36b8535e5a3e663b0b1c2",
#                             host="ec2-63-34-130-73.eu-west-1.compute.amazonaws.com",
#                             port="5432",
#                             database="djjpvsdhnc9pl")
#
#     # Создайте курсор для выполнения операций с базой данных
#     cursor = conn.cursor()
#     # SQL-запрос для создания новой таблицы
#     # create_table_query = '''CREATE TABLE trackers
#     #                       (ID          BIGINT,
#     #                       ZNAK       TEXT,
#     #                       NAME         TEXT,
#     #                       USERNAME      TEXT); '''
#     # Выполнение команды: это создает новую таблицу
#     # cursor.execute(create_table_query)
#     cursor.execute("""ALTER TABLE trackers ADD COLUMN article INTEGER;""")
#     conn.commit()
#     print(546)
# except (Exception, psycopg2.Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if conn:
#         cursor.close()
#         conn.close()
# print("Соединение с PostgreSQL закрыто")


class BotDB:
    def __init__(self):
        self.conn = psycopg2.connect(user="thszlocyntmmgg",
                                     password="daea238bb862af4128bd5a075824f4e2ad4fa8242fb36b8535e5a3e663b0b1c2",
                                     host="ec2-63-34-130-73.eu-west-1.compute.amazonaws.com",
                                     port="5432",
                                     database="djjpvsdhnc9pl")
        self.cursor = self.conn.cursor()

    def user_exists(self, id):
        self.cursor.execute("SELECT * FROM trackers WHERE id = %s", (id,))
        return bool(len(self.cursor.fetchall()))

    def add_user(self, id, status, name, username, znak):
        self.cursor.execute("INSERT INTO trackers (id, name, status, username, znak) VALUES (%s, %s, %s, %s, %s)", (id, name, status, username, znak))
        return self.conn.commit()

    def update_status(self, id, new_status):
        self.cursor.execute("UPDATE trackers SET status = %s WHERE id = %s", (new_status, id))
        return self.conn.commit()

    def update_znak(self, id, new_znak):
        self.cursor.execute("UPDATE trackers SET znak = %s WHERE id = %s", (new_znak, id))
        return self.conn.commit()

    def get_status(self, id):
        self.cursor.execute("SELECT status FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def get_id(self):
        self.cursor.execute("SELECT id FROM trackers")
        return self.cursor.fetchall()

    def get_znak(self, id):
        self.cursor.execute("SELECT znak FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def update_topic(self, id, topic):
        self.cursor.execute("UPDATE trackers SET topic = %s WHERE id = %s", (topic, id))
        return self.conn.commit()

    def update_article(self, id, article):
        self.cursor.execute("UPDATE trackers SET article = %s WHERE id = %s", (article, id))
        return self.conn.commit()

    def get_article(self, id):
        self.cursor.execute("SELECT article FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def get_topic(self, id):
        self.cursor.execute("SELECT topic FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]
