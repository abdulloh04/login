import getpass
import os

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "abdulloh",
    database = "login"
)
dbtitle = 'loginpage'


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
            self.login_()

    def registr(self):
        self.clear()
        login = input("Login: ").lower().strip()

        while self.string_empty(login[0].isalpha()):
            self.clear_and_text("Loginda faqat harf va sondan iborat bo'lsin!!!")
            login = input("Login: ").lower().strip()

        while self.birxil('login', login):
            self.clear_and_text("Bunday login mavjud boshqa login kiriting!!!")
            login = input("Login: ").lower().strip()

        self.clear()

        password = getpass.getpass("Password: ").lower().strip()

        while self.string_empty(password) or self.len_(password, 8):
            self.clear_and_text("Passworddingiz 8ta belgidan oz!!!")
            password = getpass.getpass("Password: ").lower().strip()

        t_password = getpass.getpass("Passwordni takrorlang: ").lower().strip()

        while t_password != password:
            self.clear_and_text("Hozirgi kiritgan passwordingiz birinchisi bilan mos tushmayapti iltimos to'g'ri kiriting!!!")
            t_password = getpass.getpass("Passwordni takrorlang: ").lower().strip()

        self.clear()

        name = input("Ismingizni kirinting: ").capitalize().strip()

        while self.string_empty(name.isalpha()):
            self.clear_and_text("Faqat harfdan iborat bo'lsin!")
            name = input("Ismingizni kirinting: ").capitalize().strip()


        self.clear()

        age = input("Yoshingiz: ").strip()

        while self.string_empty(age.isnumeric()) or not len(age) <= 3:
            self.clear_and_text("Bosh belgi yoki hajmi uchdan ko'p bo'lgan son kiritmang!")
            age = input("Yoshingiz: ").strip()


        self.db_ulash(login, password, name, int(age))


    def login_(self):
        self.clear()
        login = input("Login: ").strip().lower()
        password = input("Password: ").strip().lower()

        while not self.loginqism(login, password):
            self.clear_and_text("Login yokida password to'g'ri")
            login = input("Login: ").strip().lower()
            password = input("Password: ").strip().lower()

        self.loginni_ichi()


    def loginni_ichi(self):
        self.clear()
        self.option_4()
        tanlash = input("[1-4]")
        tanlash_option = ['1', '2', '3', '4']

        while tanlash not in tanlash_option:
            self.clear_and_text("Faqat 1 dan 4 gacham raqamni kiriting!!!")
            tanlash = input("[1-4]: ")

        






    def clear(self):
        os.system("clear")

    def clear_and_text(self, string: str):
        self.clear()
        print(f"{string}")

    def string_empty(self, string):
        return not bool(string)

    def len_(self, password, len_: int):
        if len(password) >= len_:
            return False
        return True

    @staticmethod
    def option_4():
        print("""
        Loginni yangilash               [1]
        Passwordni yangilash            [2]
        Accountni o'chirib tashlash     [3]
        Tizimdan chiqib ketish          [4]""")

    # Mysql

    def birxil(self, login, t_title):
        mydb = db.cursor()
        mydb.execute(f"select * from {dbtitle} where {t_title}='{login}';")
        mydb1 = mydb.fetchall()

        if mydb1:
            return True
        return False

    def loginqism(self, login, password):
        mydb = db.cursor()
        mydb.execute(f"select * from {dbtitle} where login='{login}' and password='{password}';")
        mydb1 = mydb.fetchall()

        if mydb1:
            return True
        return False

    def db_ulash(self, login, password, name, age):
        mydb = db.cursor()
        mydb.execute(f"insert into {dbtitle} (login, password, name, age) values ('{login}', '{password}', '{name}', '{age}');")
        db.commit()







person = Loginpage()
person.loginni_ichi()

