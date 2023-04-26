from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/student_info')
db = client['student_info']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    regdno =request.form['regdno']
    contact = request.form['contact']
    db.students.insert_one({'name': name , 'regdno':regdno , 'contact':contact})
    return render_template('greet.html', name=name)
    

if __name__== '__main__':
    app.run(debug=True)