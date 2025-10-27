from flask import Flask, render_template
from flask_login import LoginManager
from database import Session
from models.user import User
from auth import auth_bp
from products import products_bp
from flask import Flask

app = Flask(__name__)

app.secret_key = "segredo_muito_seguro"

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    db = Session()
    user = db.get(User, int(user_id))
    db.close()
    return user


app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
