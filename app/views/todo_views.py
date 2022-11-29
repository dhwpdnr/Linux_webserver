from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from app import db
from app.models import todo

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/main')
def main_view():
    todo_list = todo.query.all()
    # 리스트 들어올 자리
    # render 할때 같이 뿌려줌
    print(todo_list)
    return render_template('main.html', todo_list = todo_list)

# @bp.route('/detail')


@bp.route('/create')
def create():
    return render_template('create.html')


@bp.route('/api/create', methods = ('POST',))
def create_api():
    title = request.form.get('title', "title")
    description = request.form.get('description', "description")
    complete = request.form.get('complete', False)
    create_query = todo(title=title, description=description, complete=complete)
    db.session.add(create_query)
    db.session.commit()
    return redirect(url_for('todo.main_view'))