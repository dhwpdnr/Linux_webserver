from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'INDEX'


@bp.route('/hello')
def hello():
    return 'Hello'