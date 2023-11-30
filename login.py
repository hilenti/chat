from flask import Flask, render_template, request, jsonify
import functions
app = Flask(__name__, template_folder='html_css')

show_login = True  # 根据需要设置是否显示登录部分
show_registration = False # 根据需要设置是否显示注册部分


@app.route('/')
def home():
    return render_template('login.html', show_login=show_login, show_registration=show_registration)


@app.route('/toggle_registration')
def toggle_registration():
    global show_login, show_registration
    show_login = not show_login
    show_registration = not show_registration
    return jsonify({'show_login': show_login, 'show_registration': show_registration})


@app.route('/login', methods=['POST'])
def login():
    phone = request.form['phone']
    password = request.form['password']
    print(password, phone)

    return f'Login attempt with Phone: {phone} and Password: {password}'


@app.route('/register', methods=['POST'])
def register():
    name = request.form['reg-username']
    phone = request.form['reg-phone']
    password = request.form['reg-password']
    re_password = request.form['re-password']
    if password == re_password and len(phone) == 11:
        functions.registered(name, phone, password)
    
    return f'Registration attempt with Name: {name}, Phone: {phone}, and Password: {password}'


if __name__ == '__main__':
    app.run(debug=True)