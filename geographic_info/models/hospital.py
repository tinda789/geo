from flask_mysqldb import MySQL

class HospitalModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def add_hospital(self, name, address, latitude, longitude):
        # Kiểm tra dữ liệu đầu vào
        if not all([name, address, latitude, longitude]):
            raise ValueError("All fields are required.")
        
        try:
            with self.mysql.connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO hospitals (name, address, latitude, longitude) VALUES (%s, %s, %s, %s)", 
                    (name, address, latitude, longitude)
                )
                self.mysql.connection.commit()
        except Exception as e:
            print(f"An error occurred while adding the hospital: {e}")
            self.mysql.connection.rollback()

    def get_hospitals(self):
        try:
            with self.mysql.connection.cursor() as cur:
                cur.execute("SELECT * FROM hospitals")
                hospitals = cur.fetchall()
                return hospitals
        except Exception as e:
            print(f"An error occurred while fetching hospitals: {e}")
            return []

    def get_hospital(self, id):
        try:
            with self.mysql.connection.cursor() as cur:
                cur.execute("SELECT * FROM hospitals WHERE id=%s", (id,))
                hospital = cur.fetchone()
                return hospital
        except Exception as e:
            print(f"An error occurred while fetching the hospital: {e}")
            return None

    def update_hospital(self, id, name, address, latitude, longitude):
        # Kiểm tra dữ liệu đầu vào
        if not all([id, name, address, latitude, longitude]):
            raise ValueError("All fields are required.")
        
        try:
            with self.mysql.connection.cursor() as cur:
                cur.execute(
                    "UPDATE hospitals SET name=%s, address=%s, latitude=%s, longitude=%s WHERE id=%s", 
                    (name, address, latitude, longitude, id)
                )
                self.mysql.connection.commit()
        except Exception as e:
            print(f"An error occurred while updating the hospital: {e}")
            self.mysql.connection.rollback()

    def delete_hospital(self, id):
        # Kiểm tra dữ liệu đầu vào
        if not id:
            raise ValueError("ID is required.")
        
        try:
            with self.mysql.connection.cursor() as cur:
                cur.execute("DELETE FROM hospitals WHERE id=%s", (id,))
                self.mysql.connection.commit()
        except Exception as e:
            print(f"An error occurred while deleting the hospital: {e}")
            self.mysql.connection.rollback()
