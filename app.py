from flask_mysqldb import *
from flask import *
import MySQLdb.cursors

app = Flask("__name__",template_folder="./template")
app.secret_key = 'Tahve bqltuyej tbrjereq qobfd MvIaTq cmanmvpcuxsz iesh tihkel CnTu dretpyauritompeanstd '
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'chitchat'
app.config['MYSQL_PORT'] = 3306
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


mysql = MySQL(app)

@app.route('/',methods=['POST','GET'])
def login():
    if session and session['loggedin']:
        return render_template('chat.html')
    return render_template('login.html',msg = "Please login to continue")
@app.route('/loginsubmission',methods=['POST'])
def loginsub():
    username = request.form['username']
    password = request.form['password']
    if username and password : 
        query = f'select * from account where username = "{username}" and password = "{password}"'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['name'] = username
            return render_template('chat.html')
        else:
            return render_template('login.html',msg = "Invalid username/password ")
    else:
        return render_template('error.html',msg = "Oops !!!!😑😑Invalid access")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')
if __name__== "__main__":
    app.run(debug=True)
