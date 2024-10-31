from flask import Flask
from flask_mysqldb import MySQL
from controllers.hospital_controller import hospital_blueprint
from controllers.hospital_controller import hospital_blueprint, set_hospital_model  # Thêm set_hospital_model


app = Flask(__name__)

# Cấu hình MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Thay 'username' bằng tên người dùng MySQL của bạn
app.config['MYSQL_PASSWORD'] = 'JinR25012002'  # Thay 'password' bằng mật khẩu MySQL của bạn
app.config['MYSQL_DB'] = 'hospital_management'

mysql = MySQL(app)

# Đăng ký blueprint
app.register_blueprint(hospital_blueprint)

def create_app():
    from models.hospital import HospitalModel
    hospital_model = HospitalModel(mysql)
    
    # Thiết lập hospital_model cho controller
    set_hospital_model(hospital_model)

    return hospital_model
if __name__ == '__main__':
    create_app()  # Khởi tạo ứng dụng
    app.run(debug=True)
