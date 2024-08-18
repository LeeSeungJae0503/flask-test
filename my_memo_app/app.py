from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from login_manager import login_manager
from controllers import setup_routes

app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysqlpswd@localhost/my_memo_app'
# SQLAlchemy의 수정 추적 기능을 비활성화합니다. (성능상의 이유로 권장됩니다.)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 세션 및 쿠키에 대한 보안 향상을 위해 필요한 비밀 키를 설정합니다.
app.config['SECRET_KEY'] = 'mysecretkey'


# 데이터베이스 및 로그인 관리자 초기화
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# 라우팅 설정
setup_routes(app)

# 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()