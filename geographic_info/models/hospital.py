from flask_mysqldb import MySQL

class HospitalModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def add_hospital(self, name, address, latitude, longitude):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO hospitals (name, address, latitude, longitude) VALUES (%s, %s, %s, %s)", 
                    (name, address, latitude, longitude))
        self.mysql.connection.commit()
        cur.close()

    def get_hospitals(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM hospitals")
        hospitals = cur.fetchall()
        cur.close()
        return hospitals

    def get_hospital(self, id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM hospitals WHERE id=%s", (id,))
        hospital = cur.fetchone()
        cur.close()
        return hospital

    def update_hospital(self, id, name, address, latitude, longitude):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE hospitals SET name=%s, address=%s, latitude=%s, longitude=%s WHERE id=%s", 
                    (name, address, latitude, longitude, id))
        self.mysql.connection.commit()
        cur.close()

    def delete_hospital(self, id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM hospitals WHERE id=%s", (id,))
        self.mysql.connection.commit()
        cur.close()
