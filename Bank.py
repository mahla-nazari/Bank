#import sqlite3
#conn = sqlite3.connect('customer.db')
#c = conn.cursor()
#c.execute("""create table bank_data_6(
#username datatype,
#age datatype,
#fname datatype,
#mname datatype,
#lname datatype,
#gender datatype,
#phonenumber datatype,
#email datatype,
#ID datatype,
#country datatype,
#city datatype,
#password datatype,
#money datatype,
#time datatype,
#log_history datatype)""")


#_________


#import sqlite3
#conn = sqlite3.connect('customer.db')
#c = conn.cursor()
#c.execute("""create table operator_accounts(
#fname datatype,
#lname datatype,
#username datatype,
#password datatype)""")



# The Functions____________________________________________________
def check_user(s):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select username from bank_data_6")
    item = c.fetchall()
    for i in item:
        for j in i:
            if s == j:
                return False
    return True




def check_pass_1(a1,a2,a3,a4):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select * from operator_accounts where rowid='1'")
    v = c.fetchall()
    for p in v:
        fname = p[0]
        lname = p[1]
        username = p[2]
        password = p[3]
        if a1 == fname and a2 == lname and a3 == username and a4 == password:
            return True
        return False





def check_pass_2(a1,a2,a3,a4):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select * from operator_accounts where rowid='2'")
    v = c.fetchall()
    for p in v:
        fname = p[0]
        lname = p[1]
        username = p[2]
        password = p[3]
        if a1 == fname and a2 == lname and a3 == username and a4 == password:
            return True
        return False



def check_pass_3(a1,a2,a3,a4):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select * from operator_accounts where rowid='3'")
    v = c.fetchall()
    for p in v:
        fname = p[0]
        lname = p[1]
        username = p[2]
        password = p[3]
        if a1 == fname and a2 == lname and a3 == username and a4 == password:
            return True
        return False



def check_pass_4(a1,a2,a3,a4):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select * from operator_accounts where rowid='4'")
    v = c.fetchall()
    for p in v:
        fname = p[0]
        lname = p[1]
        username = p[2]
        password = p[3]
        if a1 == fname and a2 == lname and a3 == username and a4 == password:
            return True
        return False






def show_log_history(a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"SELECT log_history FROM bank_data_6 WHERE rowid='{a}'")
    print(c.fetchall())
    conn.commit()




def add_log_history(a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    n = time_date()
    l = []
    l.append(n)
    c.execute(f"""UPDATE bank_data_6 SET log_history = '{l}'
    WHERE rowid='{a}'""")
    conn.commit()


def time_date():
    import datetime
    b = datetime.datetime.now()
    return b


# ADD INFORMATION TO THE DATABASE
def add_data(username, age, fname, mname, lname, gender, phone_number,
             email, ID, country, city, password, money, time,log_history):
    the_data = []
    the_data.append(username)
    the_data.append(age)
    the_data.append(fname)
    the_data.append(mname)
    the_data.append(lname)
    the_data.append(gender)
    the_data.append(phone_number)
    the_data.append(email)
    the_data.append(ID)
    the_data.append(country)
    the_data.append(city)
    the_data.append(password)
    the_data.append(money)
    the_data.append(time)
    the_data.append(log_history)



    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO bank_data_6 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", the_data)
    conn.commit()
    conn.close()


# Display all data in the LOGIN_AS_OPERATOR -> SHOW ALL DATA
def show_all_data():
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select rowid,* from bank_data_6")
    items = c.fetchall()
    for item in items:
        print(f"""account_number: ({item[0]})   username: ({item[1]})    age: ({item[2]})   first name: ({item[3]})    middle name: ({item[4]})    last name: ({item[5]})    gender: ({item[6]})    phone number: ({item[7]})   email: ({item[8]})  ID: ({item[9]})    country: ({item[10]})    city: ({item[11]})    password: ({item[12]})  money: ({item[13]})    time: ({item[14]})  Last login({item[15]})""",end="\n\n")



# Display the amount of money to the user in the LOGIN section.
def show_money(n):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("""select money from bank_data_6 where rowid = {}""".format(n))
    item = (c.fetchall())
    for i in item:
        for j in i:
            print('Money:', end="")
            print(j)


# Money transfer in the LOGIN section
def money_transfer(h, a1, a2):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("""select money from bank_data_6 where rowid = {}""".format(a1))
    item = (c.fetchall())
    for i in item:
        for j in i:
            if h > j:
                print('not enough money to transfer.')
            else:
                add_money(a2, h)
                withdraw_money(a1, h)


# Withdraw money in the LOGIN section
def withdraw_money(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("select money from bank_data_6 where rowid = {}".format(n))
    item = (c.fetchall())
    for i in item:
        for j in i:
            h = (j - a)
            c.execute("update bank_data_6 set money = {} where rowid = {}".format(h, n))
            print("successful")
    conn.commit()


# Add money in the LOGIN section
def add_money(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("select money from bank_data_6 where rowid = {}".format(n))
    item = (c.fetchall())
    for i in item:
        for j in i:
            h = (j + a)
            c.execute("update bank_data_6 set money = {} where rowid = {}".format(h, n))
            print("The operation was completed successful")
    conn.commit()


# To check the password in the LOGIN section
def show_password(n):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("select password from bank_data_6 where rowid = {}".format(n))
    item = (c.fetchall())
    for i in item:
        for j in i:
            return j
    conn.commit()



# To show a special account in the LOGIN and LOGIN_AS_OPERATOR section.
def show_an_account(n):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("select rowid,* from bank_data_6 where rowid = {}".format(n))
    items = c.fetchall()
    for item in items:
        print(f"""account_number: ({item[0]})   username: ({item[1]})    age: ({item[2]})   first name: ({item[3]})    middle name: ({item[4]})    last name: ({item[5]})    gender: ({item[6]})    phone number: ({item[7]})   email: ({item[8]})  ID: ({item[9]})    country: ({item[10]})    city: ({item[11]})    password: ({item[12]})  money: ({item[13]})    time: ({item[14]})   Last login({item[15]})""", end="\n\n")
    conn.commit()


# To change first name in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_fname(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET fname = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change last name in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_lname(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET lname = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change middle name in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_mname(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET mname = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change age in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_age(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET age = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change email in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_email(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET email = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change phone number in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_phone_number(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET phonenumber = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change gender in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_gender(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET gender = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change username in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_username(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET username = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change country in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_country(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET country = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change city in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_city(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET city = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change password in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_password(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute(f"""UPDATE bank_data_6 SET password = '{n}'
    WHERE rowid='{a}'""")
    conn.commit()


# To change ID in the LOGIN_AS_OPERATOR -> UPDATE ACCOUNT INFORMATION
def update_ID(n, a):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("update bank_data_6 set ID = {} where rowid = {}".format(n, a))
    conn.commit()


# To delete an account in the LOGIN_AS_OPERATOR -> DELETE AN ACCOUNT
def delete_account(n):
    import sqlite3
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("delete from bank_data_6 where rowid = {}".format(n))
    print("account was deleted.")
    conn.commit()


# __________________VALIDATIONS________________
# tool function
def counter(n):
    c = 0
    for i in n:
        c += 1
    return c


# Is age a number or not ?????
def age_validation_1(n):
    c = 0
    for i in n:
        if ord('0') <= ord(i) <= ord("9"):
            c += 1
    if c == len(n):
        return True
    return False


# Is the user of legal age to create an account or not ????
def age_validation_2(n):
    if int(n) >= 18:
        return True
    return False


def name_valid(n):
    c = 0
    for i in n:
        if ord('a') <= ord(i) <= ord("z") or ord('A') <= ord(i) <= ord("Z"):
            c += 1
    if c == len(n):
        return True
    return False


def middle_name_valid(n):
    if n != "":
        c = 0
        for i in n:
            if ord('a') <= ord(i) <= ord("z") or ord('A') <= ord(i) <= ord("Z"):
                c += 1
        if c == len(n):
            return True
        return False
    else:
        return True


def gender_valid(n):
    if n == 'female' or n == 'male':
        return True
    return False


def phone_valid(n):
    c = 0
    for i in n:
        if ord('0') <= ord(i) <= ord("9"):
            c += 1
    if c == len(n):
        if counter(n) == 11 and n[0:4] == '0912'or'0911'or'0913'or'0914'or'0915'or'0916'or'0917'or'0918'or'0991'or\
        '0992'or'0993'or'0994'or'0930'or'0933'or'0935'or'0936'or'0937'or'0938'or'0939'or'0901'or'0902'or'0903'or'0904'or\
        '0905'or'0941'or'0942'or'0920'or'0921'or'0922'or'0932'or'0931'or'0934':
            return True
        return False
    return False


def email_valid(n):
    if counter(n) > 10 and (n[-10:] == '@gmail.com' or n[-10:] == '@yahoo.com'):
        return True
    return False


def ID_valid(n):
    c = 0
    for i in n:
        if ord('0') <= ord(i) <= ord("9"):
            c += 1
    if c == len(n):
        if len(n) == 10:
            return True
        return False
    return False


# tool function
def isalpha_1(n):
    c = 0
    for i in n:
        if ord('a') <= ord(i) <= ord("z") or ord('A') <= ord(i) <= ord("Z") or \
                (i == " " and n.isspace() == False):
            c += 1
    if c == len(n):
        return True
    return False


# tool function
def check(n, a):
    if n == a:
        return True
    return False


def password_valid(n):
    c = 0
    v = 0
    if len(n) >= 8:
        for i in n:
            if ord('0') <= ord(i) <= ord('9'):
                c += 1
            if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
                v += 1
        if v + c == len(n):
            return True
    return False


def username_check(n):
    for i in n:
        if ord('a') <= ord(i) <= ord("z") or ord('A') <= ord(i) <= ord("Z") or (i == "_"):
            return True
    return False


# ________CLASS_________

class bank:

    # get information from user and save in database
    def create_account(self):
        username = input("Enter username: ")
        if username_check(username) == True:
            if check_user(username)==True:
                age = input('how old are you?: ')
                if age_validation_1(age) == True:
                    if age_validation_2(age) == True:
                        fname = input("what is your first name?: ")
                        if name_valid(fname) == True:
                            mname = input("what is your middle name?: ")
                            if middle_name_valid(mname) == True:
                                lname = input("what is your last name?: ")
                                if name_valid(lname) == True:
                                    gender = input("Enter your gender: ")
                                    if gender_valid(gender) == True:
                                        phone_number = input("Enter your phone number: ")
                                        if phone_valid(phone_number) == True:
                                            email = input("Enter your email: ")
                                            if email_valid(email) == True:
                                                ID = input("Enter your national code(ID): ")
                                                if ID_valid(ID) == True:
                                                    country = input("Enter your country: ")
                                                    if isalpha_1(country) == True:
                                                        city = input("where do you live?: ")
                                                        if isalpha_1(city) == True:
                                                            password = input("set your password: ")
                                                            if password_valid(password) == True:
                                                                password_again = input("Enter your password again: ")
                                                                if check(password_again, password) == True:
                                                                    money = 0
                                                                    the_time = time_date()
                                                                    log_history = 'none'
                                                                    add_data(username, age, fname, mname, lname, gender,
                                                                             phone_number, email, ID, country, city,
                                                                             password, money, the_time,log_history)
                                                                    print('sign up successfull')


                                                                else:
                                                                    print("Enter valid password")
                                                            else:
                                                                print("Enter valid password")
                                                        else:
                                                            print("Enter valid city")
                                                    else:
                                                        print("Enter valid country")
                                                else:
                                                    print("Enter valid ID")
                                            else:
                                                print("Enter valid email")
                                        else:
                                            print("Enter valid phone number")
                                    else:
                                        print("Enter female or male")
                                else:
                                    print("Enter valid last name")
                            else:
                                print("Enter valid middle name")
                        else:
                            print("Enter valid first name")
                    else:
                        print("not enough age")
                else:
                    print("enter valid age")
            else:
                print('This username is already exist')
        else:
            print("enter valid username")

    # login into account and transfer money , add money , withdraw money , view account information ,.....
    def login(self):


        num = input("Enter your account number: ")
        pas = input("Enter your password: ")

        if show_password(num) == pas:
            add_log_history(num)



            a = input("""
            welcome.select an action :

            1.add money 

            2.money transfer 

            3.withdraw money

            4.show money

            5.my account information
            

            """)

            if a == '1':
                h = int(input("how much money?: "))
                add_money(num, h)


            elif a == '2':
                n = input("Enter number of account you wanna transfer money to: ")
                m = int(input("how much money do you want to transfer?: "))
                money_transfer(m, num, n)

            elif a == '3':
                h = int(input("How much money?: "))
                withdraw_money(num, h)
            elif a == '4':
                show_money(num)
            elif a == '5':
                show_an_account(num)
            else:
                print("Enter valid action")





        else:
            print("password is wrong ")

    # login as operator & update account info
    # ,delete an account,.view all accounts
    # ,view account information
    def login_as_operator(self):
        # operators info:
        # fnames     lnames    usernames      passwords
        #('James', 'Brown', 'operator_1', 'jamesoperator_1')
        #('Mary', 'Gadon', 'operator_2', 'marymary222op')
        #('John', 'Freeman', 'operator_3', 'jjjoperator_3')
        #('Elen', 'Silvera', 'operator_4', 'eloperator3##')
        fname = input("Enter your first name please: ")
        lname = input("Enter your last name please: ")
        username = input("Enter your username please: ")
        password = input("Enter your password please: ")

        if check_pass_1(fname,lname,username,password)==True or check_pass_2(fname,lname,username,password)==True or\
            check_pass_3(fname,lname,username,password)== True or check_pass_4(fname,lname,username,password)==True:


            action = input(""" check_pass_

            Welcome.please select an action:

             1.update account info

             2.delete an account

             3.view all accounts

             4.view account information
             
             5.view last login

             """)

            if action == "1":
                item = input("""

                1.update username
                2.update age
                3.update first name
                4.update last name
                5.update gender
                6.update ID
                7.update country 
                8.update city
                9.update middle name
                10.update email
                11.update phone number
                12.update password

                """)

                if item == '1':
                    num = input("Enter account number: ")
                    username_1 = input("Enter new username: ")
                    if name_valid(username_1) == True:
                        update_fname(username_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid username")

                elif item == '2':
                    num = input("Enter account number: ")
                    age_1 = input("Enter new age: ")
                    if age_validation_1(age_1) == True and age_validation_2(age_1) == True:
                        update_age(age_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid age")

                elif item == '3':
                    num = int(input("Enter account number: "))
                    fname_1 = input("Enter new first name: ")
                    if name_valid(fname_1) == True:
                        update_fname(fname_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid first name")


                elif item == '4':
                    num = input("Enter account number: ")
                    lname_1 = input("Enter new last name: ")
                    if name_valid(lname_1) == True:
                        update_lname(lname_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid last name")



                elif item == '5':
                    num = input("Enter account number: ")
                    gender_1 = input("Enter new gender(male or female): ")
                    if gender_valid(gender_1) == True:
                        update_gender(gender_1, num)
                        print("Updated successful")
                    else:
                        print("Enter female or male")



                elif item == '6':
                    num = input("Enter account number: ")
                    ID_1 = input("Enter new national code(ID)")
                    if ID_valid(ID_1) == True:
                        update_ID(ID_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid national code(ID)")





                elif item == '7':
                    num = input("Enter account number: ")
                    country_1 = input("Enter new country: ")
                    if isalpha_1(country_1) == True:
                        update_country(country_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid country")



                elif item == '8':
                    num = input("Enter account number: ")
                    city_1 = input("Enter new city: ")
                    if isalpha_1(city_1) == True:
                        update_city(city_1, num)
                        print("Updated successful")
                    else:
                        print("Enter valid city")






                elif item == '9':
                    num = input("Enter account number: ")
                    midname = input("Enter new middle name: ")
                    if middle_name_valid(midname) == True:
                        update_mname(midname, num)
                        print("Updated successful")
                    else:
                        print("Enter valid middle name")




                elif item == '10':
                    num = input("Enter account number: ")
                    em = input("Enter new email: ")
                    if email_valid(em) == True:
                        update_email(em, num)
                        print("Updated successful")
                    else:
                        print("Enter valid Email")





                elif item == '11':
                    num = input("Enter account number: ")
                    ph = input("Enter new phone number: ")
                    if phone_valid(ph) == True:
                        update_phone_number(ph, num)
                        print("Updated successful")
                    else:
                        print("Enter valid phone number")



                elif item == '12':
                    num = input("Enter account number: ")
                    pas = input("Enter new password: ")
                    if password_valid(pas) == True:
                        update_password(pas, num)
                        print("Updated successful")
                    else:
                        print("Enter valid password")


                else:
                    print("Enter valid number(1,...,12)")

            elif action == "2":
                t = input("Enter the account number you want to delete: ")
                delete_account(t)


            elif action == "3":
                show_all_data()

            elif action == '4':
                t = input("Enter the account number: ")
                show_an_account(t)
            elif action == '5':
                t = input("Enter the account number: ")
                show_log_history(t)
            else:
                print('Enter valid action')
        else:
            print('try again')




t = bank()
t.create_account()
