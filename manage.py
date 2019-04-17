from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

class Config(object):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/information'
    # 不跟踪数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS =  False

    REDIS_HOST = '17.0.0.1'
    REDIS_PORT = 6379
    REDIS_NUM = 1

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)
