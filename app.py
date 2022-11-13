from flask_mysqldb import MySQL
from flask import request,redirect,render_template,session,Flask,jsonify
import MySQLdb.cursors
# from flask_ngrok import run_with_ngrok

app = Flask("__name__",template_folder="./template")
# run_with_ngrok(app)
app.secret_key = 'Tahve bqltuyej tbrjereq qobfd MvIaTq cmanmvpcuxsz iesh tihkel CnTu dretpyauritompeanstd '
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'chitchat'
app.config['MYSQL_PORT'] = 3306
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

mysql = MySQL(app)
@app.route('/register',methods=['POST'] )
def register():
    if not session and session['loggedin']:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f"select * from account where username = '{username}' or email = '{email}'")
        account = cursor.fetchall()
        if account:
            return render_template('login.html',errmsg="Username\email already exist")
        else:
            session['loggedin'] = True
            session['name'] = username
            return render_template('chat.html',errmsg="Successfully logged in")

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
            # query = f"select * from account where from = '{username}' and to = 'guru' order by time and date"
            # cursor.execute(query)
            # chatr = cursor.fetchall()
            # msg = {}
            # content = []
            # if chatr:
            #     msg =  {'time' : chatr['time'],'date' : chatr['date'] ,'msg' : chatr['msg']}
            #     content.append(msg)
            #     return render_template('chat.html',jsonify(content))
            # else:
            return render_template('chat.html',msg = 'Start new message',g="hi how are you")
        else:
            return render_template('login.html',msg = "Invalid username/password ")
    else:
        return render_template('login.html',msg = "😑😑 Enter the Username and password")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',errmsg = "UH OH! You're lost.")
@app.errorhandler(405)
def page_not_found(e):
    return render_template('error.html',errmsg="Invalid Access")
@app.route('/chat')
def chat():
    if session['loggedin']: 
        return render_template('chat.html')
    else:
        return render_template('login.html',errmsg="Invalid Access")
@app.route('/logout')
def logout():
    session.pop('loggedin')
    session.pop('name')
    return redirect('/')
if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)

    # app.run()