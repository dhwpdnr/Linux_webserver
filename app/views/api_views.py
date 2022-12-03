from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
from app import db
from app.models import users

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/signup', methods = ('POST',))
def signup_api():
    user_id = request.form['user_id']
    user_password = request.form['user_pw']
    user_name = request.form['user_name']
    signup_query = users(user_id=user_id,user_password=user_password, user_name=user_name)
    db.session.add(signup_query)
    db.session.commit()
    return redirect(url_for('main.login'))

@bp.route('/login', methods=('POST',))
def login_api():
    user_id = request.form['user_id']
    user_password = request.form['user_pw']
    login_query = users.query.filter(users.user_id == user_id,users.user_password==user_password).all()
    if len(login_query) == 0 :
        return redirect(url_for('main.validate'))
    return redirect(url_for('todo.main_view'))
