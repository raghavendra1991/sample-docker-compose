from flask import Flask, request
from flask_mysqldb import MySQL

app=Flask(__name__)
# Configure db
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return '<html><body><form method="POST" action="">Name <input type="text" name="name" /><br>Email <input type="email" name="email" /><br><input type="submit"></form></body></html>'
if __name__ == '__main__':
    app.run(host='0.0.0.0')
