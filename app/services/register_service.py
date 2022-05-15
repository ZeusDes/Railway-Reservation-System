from . import storage_wrapper

db_conn = storage_wrapper.db_conn

# TODO: insert into db after getting user data
def register_user(NID, phone_no, email, DOB, gender, password):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM Person WHERE NID = %s", (NID, ))
    VerifyUser = cur.fetchall()
    if len(VerifyUser) != 0:
        raise ValueError("National ID already exists")
    else:
        cur.execute("INSERT INTO Person (NID, Phone_no, Email, DOB, Gender, Password) VALUES (%s, %s, %s, %s, %s, %s)", (NID, phone_no, email, DOB, gender, password))
        db_conn.commit()
    cur.close()
