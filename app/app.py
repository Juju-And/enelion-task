from flask import Flask
from models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'coderslab',
    'db': 'enelion',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def main():
    return 'Hello World!'




# @app.route('/generate_data')
# def generate();
#     pass












app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()
