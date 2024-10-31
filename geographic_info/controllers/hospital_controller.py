from flask import Blueprint, render_template, request, redirect, url_for

hospital_blueprint = Blueprint('hospitals', __name__)
hospital_model = None

def set_hospital_model(model):
    global hospital_model
    hospital_model = model

@hospital_blueprint.route('/')
def index():
    hospitals = hospital_model.get_hospitals()
    return render_template('index.html', hospitals=hospitals)

@hospital_blueprint.route('/add', methods=['POST'])
def add_hospital():
    name = request.form['name']
    address = request.form['address']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    hospital_model.add_hospital(name, address, latitude, longitude)
    return redirect(url_for('hospitals.index'))


@hospital_blueprint.route('/add', methods=['POST'])
def add_hospital():
    name = request.form['name']
    address = request.form['address']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    
    hospital_model.add_hospital(name, address, latitude, longitude)
    return redirect(url_for('hospitals.index'))

@hospital_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_hospital(id):
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        
        hospital_model.update_hospital(id, name, address, latitude, longitude)
        return redirect(url_for('hospitals.index'))
    
    hospital = hospital_model.get_hospital(id)
    return render_template('edit.html', hospital=hospital)

@hospital_blueprint.route('/delete/<int:id>', methods=['GET'])
def delete_hospital(id):
    hospital_model.delete_hospital(id)
    return redirect(url_for('hospitals.index'))
