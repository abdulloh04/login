import getpass
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
            self.clear_and_text("Faqat 1 va 2 raqamni kiriting!!!")
            tanlash = input("[1/2]: ")

        if tanlash == tanlash_option[0]:
            self.registr()
        else:
            self.login()

    def registr(self):
        # self.clear()
        # login = input("Login: ").lower()
        #
        # while self.string_empty(login[0].isalpha()) or self.birxil_login(login):
        #     self.clear_and_text("Login faqat harf va sondan iborat bo'lsin!!!")
        #     login = input("Login: ").lower()
        #
        # self.clear()
        #
        # password = getpass.getpass("Password: ").lower()
        #
        # while self.string_empty(password) or self.passlen(password):
        #     self.clear_and_text("Passworddingiz 8ta belgidan oz!!!")
        #     password = getpass.getpass("Password: ").lower()
        #
        # t_password = getpass.getpass("Passwordni takrorlang: ").lower()
        #
        # while t_password != password:
        #     self.clear_and_text("Hozirgi kiritgan passwordingiz birinchisi bilan mos tushmayapti iltimos to'g'ri kiriting!!!")
        #     t_password = getpass.getpass("Passwordni takrorlang: ").lower()
        #
        # self.clear()
        #
        name = input("Ismingizni kirinting: ").capitalize()

        while self.string_empty(name.isalpha()):
            self.clear_and_text("Faqat harfdan iborat bo'lsin!")
            name = input("Ismingizni kirinting: ").capitalize()

        




    def login(self):
        print("Login qism")


    def clear(self):
        os.system("clear")

    def clear_and_text(self, string: str):
        self.clear()
        print(f"{string}")

    def string_empty(self, string):
        return not bool(string)

    def birxil_login(self, login):
        mydb = db.cursor()
        mydb.execute(f"select * from loginpage where login='{login}';")
        mydb = mydb.fetchall()

        if mydb:
            return True
        return False

    def passlen(self, password):
        if len(password) >= 8:
            return False
        return True






person = Loginpage()
person.registr()

