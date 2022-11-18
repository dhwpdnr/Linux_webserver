from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)


@app.route('/login')
def login():  # put application's code here
    if (request.method == 'GET'):
        return render_template('login.html')

    elif (request.method == 'POST'):
        # 아이디 비밀번호 확인하는 로직
        return redirect(url_for())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method == 'GET'):
        return render_template('signup.html')

    elif (request.method == 'POST'):


        try:
            user_id = request.form["user_id"]
            user_pw = request.form["user_pw"]
            user_name = request.form["user_name"]

            with sql.connect("database.db") as con:
                # db 입력창에 입력커서 놓기.
                cur = con.cursor()

                # db에 값 입력. (메모리상 입력o, db에 입력x)
                cur.execute("INSERT INTO user (name,user_id,user_passwd) VALUES (?,?,?)", (user_name, user_id, user_pw))

                con.commit()  # db에 값 저장. (데이터베이스에 입력됨.)
                msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:  # try를 하던 except을 하던 finally는 무조건 한번 실행됨.
            return render_template("login.html", msg=msg)  # 파이썬에 있는 msg객체를 result.html에 전달.
            con.close()  # db 닫음.



if __name__ == '__main__':
    app.run()
