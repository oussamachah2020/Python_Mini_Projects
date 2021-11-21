import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="yourUsername",
    password="yourPassword",
    db="yourDataBase"
)

name = []
phone_number = []

while True:
    nm = str(input("Enter the name: "))
    ph = str(input("Please enter a name: "))

    while ph == "" and nm == "":
        print("Please try again!")
        nm = str(input("Enter the name: "))
        ph = str(input("Please enter a name: "))

    name.append(nm)
    phone_number.append(ph)

    mycursor = mydb.cursor()
    sql_1 = "SELECT * FROM CONTACT WHERE name = %s"
    sql_2 = "SELECT * FROM CONTACT WHERE number = %s"
    val_1 = (nm, )
    val_2 = (ph, )

    if nm:
        mycursor.execute(sql_1, val_1)
    elif ph:
        mycursor.execute(sql_2, val_2)

    result = mycursor.fetchall()

    for i in result:
        print("result: ", i)
        print(phone_number)