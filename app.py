from flask import Flask, request, render_template, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db
from family import Family

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@ipserver/database'

db.init_app(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand) # init, migrate, upgrade
fam = Family('Rodriguez')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/family', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/family/<int:id>', methods=['GET','PUT', 'DELETE'])
def family():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass

@manager.command
def hello():
    "Just say hello"
    print("hello")

if __name__ == '__main__':
    manager.run()