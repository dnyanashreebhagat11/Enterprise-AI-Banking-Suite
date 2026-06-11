from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models.user import db, User
import bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'banking_secret_key_2026'

app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql+pymysql://root:dnyanu%402027@localhost/banking_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

jwt = JWTManager(app)


@app.route('/')
def home():

    return """
    <h1>Enterprise AI Banking Suite</h1>

    <br>

    <a href='/register'>Register</a>

    <br><br>

    <a href='/login'>Login</a>
    """


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        new_user = User(
            name=name,
            email=email,
            password=hashed_password.decode('utf-8')
        )

        db.session.add(new_user)
        db.session.commit()

        return "Registration Successful!"

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if user:

            if bcrypt.checkpw(
                password.encode('utf-8'),
                user.password.encode('utf-8')
            ):

                access_token = create_access_token(
                    identity=user.email
                )

                return f"""
                Login Successful!<br><br>

                JWT Token:<br><br>

                {access_token}
                """

            return "Wrong Password"

        return "User Not Found"

    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/profile')
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return f"""
    Welcome {current_user}<br><br>

    Protected Route Access Granted
    """
@app.route('/user-info')
@jwt_required()
def user_info():

    current_user = get_jwt_identity()

    user = User.query.filter_by(
        email=current_user
    ).first()

    return {
        "name": user.name,
        "email": user.email
    }
@app.route('/logout')
def logout():

    return """
    Logout Successful
    """
@app.route('/dashboard-data')
@jwt_required()
def dashboard_data():

    current_user = get_jwt_identity()

    return {
        "message": "Dashboard Access Granted",
        "user": current_user
    }

if __name__ == "__main__":
    app.run(debug=True)