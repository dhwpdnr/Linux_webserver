from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'INDEX'


@bp.route('/hello')
def hello():
    return 'Hello'

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/signup')
def signup():
    return render_template('signup.html')