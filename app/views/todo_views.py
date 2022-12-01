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

@bp.route('/detail/<int:todo_id>')
def detail(todo_id):
    todo_detail = todo.query.get_or_404(todo_id)
    return render_template('detail.html', todo = todo_detail)


@bp.route('/update/<int:todo_id>')
def update(todo_id):
    todo_detail = todo.query.get_or_404(todo_id)
    return render_template('update.html', todo = todo_detail)

@bp.route('/api/update/<int:todo_id>', methods = ('POST',))
def update_api(todo_id):
    title = request.form.get('title', "title")
    description = request.form.get('description', "description")
    complete = request.form.get('complete', False)
    todo_update = todo.query.filter(todo.id == todo_id).update({'title' : title, 'description' : description, 'complete' : complete})
    db.session.commit()
    return redirect(url_for('todo.main_view'))

@bp.route('/api/delete/<int:todo_id>')
def delete_api(todo_id):
    todo_delete = todo.query.filter(todo.id == todo_id).first()
    db.session.delete(todo_delete)
    db.session.commit()
    return redirect(url_for('todo.main_view'))