import os

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "abdulloh",
    database = "login"
)


class Loginpage:
    def __init__(self):
        self.login = None
        self.password = None
        self.name = None
        self.age = None

    def tanlash_qismi(self):
        self.clear()
        tanlash = input("""
        Tanlash qism
        Registr [1]
        Login   [2]
        
        [1/2]: """)
        tanlash_option = ['1', '2']

        while tanlash not in tanlash_option:
            self.clear_and_invalid("Faqat 1 va 2 raqamni kiriting!!!")
            tanlash = input("[1/2]: ")

        if tanlash == tanlash_option[0]:
            self.registr()
        else:
            self.login()

    def registr(self):
        print("Regist qism")

    def login(self):
        print("Login qism")


    def clear(self):
        os.system("clear")

    def clear_and_invalid(self, string: str):
        self.clear()
        print(f"{string}")







person = Loginpage()
person.tanlash_qismi()

