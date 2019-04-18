from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager


class Config(object):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/information'
    # 不跟踪数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS =  False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_NUM = 1
    # 加密字符串
    SECRET_KEY = "dsadsafasfwqwqdsa21321wqewq"
    # 调整session存储位置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT,db=REDIS_NUM)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400*2


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=Config.REDIS_NUM)

# 开启csrf后端保护机制
csrf = CSRFProtect(app)

# 穿件session拓展类对象
Session(app)

manager = Manager(app)

@app.route('/')
def index():
    session['name'] = 'curry'
    return 'hello world!'

if __name__ == '__main__':
    # app.run(debug=True)
    #python manage.py runserver -h   -p    -d
    manager.run()
