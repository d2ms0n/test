# -*- coding: cp1251 -*-
import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER
            )
        """
        )
        self.connection.commit()

    def add_user(self, user):
        try:
            self.cursor.execute(
                """
                INSERT INTO Users (name, email, age)
                VALUES (?, ?, ?)
            """,
                (user.name, user.email, user.age),
            )
            self.connection.commit()
            print(f"������������ {user.name} ������� ��������")
        except sqlite3.Error as e:
            print(f"������ ��� ���������� ������������: {e}")

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        user_data = self.cursor.fetchone()

        if user_data:
            return user_data
        return None

    def update_user(self, user):
        try:
            self.cursor.execute(
                """
                UPDATE Users 
                SET name = ?, email = ?, age = ?
                WHERE id = ?
            """,
                (user.name, user.email, user.age, user.id),
            )
            self.connection.commit()
            print(f"������������ {user.name} ������� ��������")
        except sqlite3.Error as e:
            print(f"������ ��� ���������� ������������: {e}")

    def delete_user(self, user_id):
        try:
            self.cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
            self.connection.commit()
            print(f"������������ � ID {user_id} ������")
        except sqlite3.Error as e:
            print(f"������ ��� �������� ������������: {e}")

    def all_user(self):

        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()