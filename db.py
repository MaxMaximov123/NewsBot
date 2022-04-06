import psycopg2


a = 0
if a:
    try:
        conn = psycopg2.connect(user="mfitezskzynjlh",
                                # пароль, который указали при установке PostgreSQL
                                password="f1fee7852b0c2a6d957fd5fff2c874a19ae06ecc1062bdc655fbf1b41c12836c",
                                host="ec2-34-246-227-219.eu-west-1.compute.amazonaws.com",
                                port="5432",
                                database="d17vgbfokvor7q")

        # Создайте курсор для выполнения операций с базой данных
        cursor = conn.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE trackers
                              (ID          BIGINT,
                              ZNAK       TEXT,
                              NAME         TEXT,
                              USERNAME      TEXT,
                              TOPIC         TEXT,
                              ARTICLE       INT,
                              MODES         TEXT,
                              BIRTHDAY      TEXT);'''
        # Выполнение команды: это создает новую таблицу
        # cursor.execute(create_table_query)
        cursor.execute("""ALTER TABLE trackers ADD COLUMN status TEXT;""")
        conn.commit()
        print(546)
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    print("Соединение с PostgreSQL закрыто")


class BotDB:
    def __init__(self):
        self.conn = psycopg2.connect(user="mfitezskzynjlh",
                                # пароль, который указали при установке PostgreSQL
                                password="f1fee7852b0c2a6d957fd5fff2c874a19ae06ecc1062bdc655fbf1b41c12836c",
                                host="ec2-34-246-227-219.eu-west-1.compute.amazonaws.com",
                                port="5432",
                                database="d17vgbfokvor7q")
        self.cursor = self.conn.cursor()

    def user_exists(self, id):
        self.cursor.execute("SELECT * FROM trackers WHERE id = %s", (id,))
        return bool(len(self.cursor.fetchall()))

    def add_user(self, id, status, name, username, znak, modes):
        self.cursor.execute("INSERT INTO trackers (id, name, status, username, znak, modes) VALUES "
                            "(%s, %s, %s, %s, %s, %s)", (id, name, status, username, znak, modes))
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

    def update_modes(self, id, modes):
        self.cursor.execute("UPDATE trackers SET modes = %s WHERE id = %s", (modes, id))
        return self.conn.commit()

    def get_modes(self, id):
        self.cursor.execute("SELECT modes FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def add_birth(self, id, data):
        data = '.'.join(list(map(str, list(map(int, data.split('.'))))))
        self.cursor.execute("UPDATE trackers SET birthday = %s WHERE id = %s", (data, id))
        return self.conn.commit()

    def get_birth(self, id):
        self.cursor.execute("SELECT birthday FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def update_case(self, id, stonk):
        self.cursor.execute("UPDATE trackers SET case_ = %s WHERE id = %s", (stonk, id))
        return self.conn.commit()

    def get_case(self, id):
        self.cursor.execute("SELECT case_ FROM trackers WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]
