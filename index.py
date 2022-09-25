from flask import Flask, render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'containers-us-west-63.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'EpDh7YzTphxYiB1tq4h1'
app.config['MYSQL_DB'] = 'railway'
app.config['MYSQL_PORT'] = '6259'
 
mysql = MySQL(app)



@app.route('/')
def home():
    return 'Welcome to my first Python Page hosted in web'

 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql = "CREATE TABLE info_table ( FNAME CHAR(20) NOT NULL, LNAME CHAR(20), AGE INT )"
        cursor.execute(sql)
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
