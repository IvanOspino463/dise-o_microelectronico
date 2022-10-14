import mysql.connector
from decouple import config


def conectarDB():
    mydb = mysql.connector.connect(
        host=config('HOST'),
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config('NAME_DB')
    )

    return mydb


def insertUsersDB(mydb,name,email,password):
    cur = mydb.cursor()
    cur.execute(f'INSERT INTO users (name,email,password) VALUES ("{name}","{email}","{password}");')
    mydb.commit()
    cur.close()
    

    
def insertGrafic_DB(mydb,fecha,sensor1,sensor2,id_user):
    cur = mydb.cursor()
    cur.execute(f'INSERT INTO data_grafic (fecha,sensor1,sensor2,id_user) VALUES ("{fecha}","{sensor1}","{sensor2}",{id_user})')
    mydb.commit()
    cur.close()

def validateEmailUser(mybd,email):
    cur = mydb.cursor()
    cur.execute(f'SELECT email FROM users WHERE email="{email}"')
    data = cur.fetchall()
    cur.close()
    return True if len(data)!=0 else False  
    



if __name__== "__main__":
    mydb = conectarDB()
    #print(mydb)
    #insertUsersDB(mydb,"Ivan","ivan_gay@gmail.com","password")
    # insertGrafic_DB(mydb,"02-02-02","32","50","1")
    print(str(validateEmailUser(mydb,"estebangvx@gail.com")))
