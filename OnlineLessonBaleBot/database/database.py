import sqlite3
class Database:
    def __init__(self, debuger):
        self.path = "database/bot.db"
        self.conn = None
        self.cur = None
        self.is_open = False
        self.Debuger = debuger
        self.create_logdatabase()
        self.create_ticketsdatabase()

    def open_database(self):
        if not self.is_open:
            self.conn = sqlite3.connect(self.path)
            self.cur = self.conn.cursor()
            self.is_open = True

    def close_database(self):
        if self.is_open:
            self.conn.close()
            self.is_open = False

    def commit(self):
        self.conn.commit()

    def create_logdatabase(self):
        self.open_database()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS Log (
            id TEXT,
            username TEXT,
            firstname TEXT
        );
        
        ''')
        self.commit()
        self.close_database()

    def create_ticketsdatabase(self):
        self.open_database()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS Ticket (
            message TEXT,
            username TEXT,
            firstname TEXT
        );
        ''')
        self.commit()
        self.close_database()

    def add_log(self, message):
        self.open_database()
        self.cur.execute("INSERT INTO Log VALUES (?,?,?)", (message.content, message.author.username, message.author.first_name))
        self.commit()
        self.close_database()

    def add_ticket(self, message, onvan):
        self.open_database()
        self.cur.execute("INSERT INTO Ticket VALUES (?,?,?)", (onvan, message.author.username, message.author.first_name))
        self.Debuger.print_ticket(message)
        self.commit()
        self.close_database()

    def get_notif(self, c):
        self.open_database()
        self.cur.execute("SELECT * FROM users")
        s = self.cur.fetchall()
        for i in s:
            if i[5] == "Yes" and i[0] == c.user_id:
                return True

            elif i[5] == "No" and i[0] ==  c.user_id:
                return False
        self.close_database()

    def change_notif(self, c):
        self.open_database()

        a = self.get_notif(c)
        if a :
            self.cur.execute("UPDATE users SET notif = ? WHERE id = ?", ("No", c.user_id))

        else:
            self.cur.execute("UPDATE users SET notif = ? WHERE id = ?", ("Yes", c.user_id))


        self.commit()
        self.close_database()

    def get_ids(self):
        ac = []
        self.open_database()
        self.cur.execute("SELECT * FROM users")
        s = self.cur.fetchall()
        for i in s:
            ac.append(i[0])

        self.close_database()
        return ac

    def get_notif_id(self, user_id):
        self.open_database()
        self.cur.execute("SELECT * FROM users")
        s = self.cur.fetchall()
        for i in s:
            if i[5] == "Yes" and i[0] == user_id:
                
                self.close_database()
                return True

            elif i[5] == "No" and i[0] ==  id:
                self.close_database()
                return False

                
