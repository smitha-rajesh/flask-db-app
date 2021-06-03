"""
This Flask MySql app takes in 3 fields from the form and adds into the MySql DB
"""

from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = 'testqxf2'
app.config['MYSQL_DB'] = 'employees'
 
mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        cursor = mysql.connection.cursor()
        
        cursor.execute("CREATE TABLE Employee (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255), email varchar(255), department varchar(255))")
        cursor.execute("CREATE TABLE Department (id INT, name varchar(255))")
        
        cursor.execute("INSERT INTO Employee (name, email, department) VALUES (%s, %s, %s)",(name, email, department))
        cursor.execute("INSERT INTO Department (name) VALUES (%s)", (name))
        
        mysql.connection.commit()
        cursor.close()
        return f"Records inserted successfully into Employees and Department table!"

if __name__ == "__main__":
    app.run(host='localhost', port=5000)