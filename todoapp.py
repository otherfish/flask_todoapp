from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:mypassword@localhost:5432/todoapp'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
from views import *
if __name__ == '__main__':
    app.run('0.0.0.0',debug='true')