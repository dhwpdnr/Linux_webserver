from flask import Flask, render_template, request, redirect, url_for

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
        value = request.form
        user_id = request.form["user_id"]
        user_pw = request.form["user_pw"]
        user_name = request.form["user_name"]

        #이부분에 DB에 저장하는 로직 들어감

        print(value)
        print(user_id)
        print(user_pw)
        print(user_name)
        return redirect(url_for('login'))


# @app.route('/api/signup', methods=['POST'])
# def api_signup():



if __name__ == '__main__':
    app.run()
