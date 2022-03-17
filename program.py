from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("temp.html")

@app.route("/admin")
def admin():
    return "<h2> 🎀🎀🎀Welcome to Admin Page🎀🎀🎀 </h2> <hr/>"

@app.route("/user")
def user():
    return "<h2> Welcome to user Page😎😎😎  </h2> <hr/>"


@app.route("/authenticate",methods=['POST'])
def checkLogin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

        if email=='admin@edu.in' and password == "12345":

            #forwarding data from python to html
            return render_template('admin.html')
        else:
            return render_template('user.html')

if __name__ =="__main__":
    app.run(debug=True)