import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g, session, redirect, abort
from SDataBase import SDataBase

DATABASE = '/tmp/fiks.db'
DEBUG = True
SECRET_KEY = 'dfc3d370a23c8c6fc6129c4fae226867ca8c4134'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fiks.db')))

menu = [
    {"name": "Pricing", "url": "index"},
    {"name": "Информация", "url": "about"},
    {"name": "Контакты", "url": "contact"},
]


def connect_db():
    van = sqlite3.connect(app.config['DATABASE'])
    van.row_factory = sqlite3.Row
    return van


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    dbase = SDataBase(db)
    return render_template('index.html', title='Pricing', menu=dbase.get_menu(),
                           posts=dbase.get_posts_annonce())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = SDataBase(db)
    if request.method == "POST":
        if len(request.form['name']) > 3 and len(request.form['post']) > 8:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления информации", category="error")
            else:
                flash("Информация добавлена успешно", category="success")
        else:
            flash("Ошибка добавления информации", category="error")

    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/post/<alias>")
def show_post(alias):
    db = get_db()
    dbase = SDataBase(db)
    title, post = dbase.get_post(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.route('/about')
def about():
    db = get_db()
    dbase = SDataBase(db)
    return render_template('about.html', title='Контакты для связи', menu=dbase.get_menu())



@app.route('/contact', methods=['POST', 'GET'])
def contacts():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Информация отправлена успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template("contacts.html", title="Контакты", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = SDataBase(db)

    return render_template("page404.html", title="Реквизиты для оплаты", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


# if __name__ == '__main__':
#     app.run(debug=True)
