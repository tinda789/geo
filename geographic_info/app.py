from flask import Flask
from flask_mysqldb import MySQL
from controllers.hospital_controller import hospital_blueprint, set_hospital_model  # Thêm set_hospital_model

app = Flask(__name__)

# Cấu hình MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Chỉ cần sử dụng 'localhost' mà không cần cổng
app.config['MYSQL_PORT'] = 3306  # Cổng MySQL (có thể không cần thiết vì cổng mặc định là 3306)
app.config['MYSQL_USER'] = 'root'  # Thay 'username' bằng tên người dùng MySQL của bạn
app.config['MYSQL_PASSWORD'] = '01665846484'  # Thay 'password' bằng mật khẩu MySQL của bạn
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

@app.route('/test_db')
def test_db():
    try:
        # Mở một cursor
        cur = mysql.connection.cursor()
        # Thực hiện một truy vấn đơn giản
        cur.execute('SELECT 1')
        # Lấy kết quả
        result = cur.fetchone()
        # Đóng cursor
        cur.close()
        return f'Database connection successful: {result}'
    except Exception as e:
        return f'Database connection failed: {str(e)}'

if __name__ == '__main__':
    create_app()  # Khởi tạo ứng dụng
    app.run(debug=True)
