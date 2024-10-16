from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta

# d = second
d=timedelta(minutes=1999999999999995)

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = d


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        if user=='':
            flash('Kindly enter your name')
            return redirect(url_for('login'))
            
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        # flash('Your session exppired, login again')
        return render_template('login.html')
    
@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        flash(user)
        return render_template('user.html')
    else:
        flash('Your session expired, login again')
        return redirect(url_for("login"))
    
    
@app.route('/logout')
def logout():
    session.pop("user",None)
    flash('You logged out, login again to use this site')
    return redirect(url_for("login"))

app.run(debug=True,host='0.0.0.0',port=4000)
