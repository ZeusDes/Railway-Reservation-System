import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from services import register_service

from flask import render_template, flash, redirect, url_for, request, Blueprint

register_manage = Blueprint('register_manage', __name__)

@register_manage.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Username = request.form.get('username')
        phone = request.form.get('Phone_No')
        email = request.form.get('email')
        password = request.form.get('pass')
        dateofBirth = request.form.get('DOB')
        iNID = request.form.get('NID')
        gender = request.form.get('Gender')
        try:
            register_service.register_user(iNID, Username, phone, email, dateofBirth, gender, password)
            return redirect("/login")
        except ValueError as e:
            return render_template('register.html', error = str(e))
    return render_template('register.html')