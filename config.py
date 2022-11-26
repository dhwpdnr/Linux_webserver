# db = {
#     # 데이터베이스에 접속할 사용자 아이디
#     'user': 'root',
#     # 사용자 비밀번호
#     'password': 'test1234',
#     # 접속할 데이터베이스의 주소 (같은 컴퓨터에 있는 데이터베이스에 접속하기 때문에 localhost)
#     'host': 'localhost',
#     # 3306 포트를 통해 연결됨
#     'port': 3306,
#     # 실제 사용할 데이터베이스 이름
#     'database': 'test'
# }
#
# DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False