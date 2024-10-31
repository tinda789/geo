from flask import Blueprint, render_template, request, redirect, url_for

# Tạo blueprint cho các route liên quan đến bệnh viện
hospital_blueprint = Blueprint('hospitals', __name__)
hospital_model = None

# Thiết lập mô hình bệnh viện
def set_hospital_model(model):
    global hospital_model
    hospital_model = model

# Route để hiển thị danh sách bệnh viện
@hospital_blueprint.route('/')
def index():
    hospitals = hospital_model.get_hospitals()  # Lấy danh sách bệnh viện từ mô hình
    return render_template('index.html', hospitals=hospitals)  # Render template index.html

# Route để thêm bệnh viện
@hospital_blueprint.route('/add', methods=['POST'])
def add_hospital():
    name = request.form['name']  # Lấy tên bệnh viện từ form
    address = request.form['address']  # Lấy địa chỉ từ form
    latitude = request.form['latitude']  # Lấy vĩ độ từ form
    longitude = request.form['longitude']  # Lấy kinh độ từ form

    hospital_model.add_hospital(name, address, latitude, longitude)  # Thêm bệnh viện vào cơ sở dữ liệu
    return redirect(url_for('hospitals.index'))  # Chuyển hướng về trang danh sách bệnh viện

# Route để chỉnh sửa thông tin bệnh viện
@hospital_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_hospital(id):
    if request.method == 'POST':
        name = request.form['name']  # Lấy tên bệnh viện từ form
        address = request.form['address']  # Lấy địa chỉ từ form
        latitude = request.form['latitude']  # Lấy vĩ độ từ form
        longitude = request.form['longitude']  # Lấy kinh độ từ form
        
        hospital_model.update_hospital(id, name, address, latitude, longitude)  # Cập nhật thông tin bệnh viện
        return redirect(url_for('hospitals.index'))  # Chuyển hướng về trang danh sách bệnh viện
    
    hospital = hospital_model.get_hospital(id)  # Lấy thông tin bệnh viện từ ID
    return render_template('edit.html', hospital=hospital)  # Render template edit.html

# Route để xóa bệnh viện
@hospital_blueprint.route('/delete/<int:id>', methods=['GET'])
def delete_hospital(id):
    hospital_model.delete_hospital(id)  # Xóa bệnh viện theo ID
    return redirect(url_for('hospitals.index'))  # Chuyển hướng về trang danh sách bệnh viện
