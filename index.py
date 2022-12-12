import os
from flask import Flask, request, send_from_directory, render_template, session
from usero import *
# Create Flask app
app = Flask(__name__)

app.secret_key = 'Vi1XR1FGD5})I8q2XuO,htl-5eF3bAR'



# Set the route for the file download page
@app.route("/")
def index():
    if 'username' in session and 'password' in session and login_to_user(session['username'], session['password']):
        # Get the list of files in the specified directory
        categories = os.listdir('database')
        files = []
        for i in categories:
            tmp_list = []
            for x in os.listdir("database/"+i):
                tmp_list.append(x)
            files.append(tmp_list)
        # Render the file download page template, passing the list of files as a variable
        return render_template("index.html", categories=categories, files=files)
    return render_template("login.html", display="none") 

@app.route("/login")
def login():
    return render_template("login.html", display="none")

@app.route("/logout")
def logout():
    session['username'] = ""
    session['password'] = ""
    return render_template("login.html", display="none") 

@app.route("/try_login", methods=['POST'])
def try_login():
    if request.method == 'POST':
        if login_to_user(request.form["name"], request.form["pass"]):
            print("Logged in")
            session['username'] = request.form["name"]
            session['password'] = request.form['pass']
            # Get the list of files in the specified directory
            categories = os.listdir('database')
            files = []
            for i in categories:
                tmp_list = []
                for x in os.listdir("database/"+i):
                    tmp_list.append(x)
                files.append(tmp_list)
            # Render the file download page template, passing the list of files as a variable
            return render_template("index.html", categories=categories, files=files)   
        else:
            print("Not logged in")
            return render_template("login.html", display="")

# Set the route for file downloads
@app.route("/download/<path:filename>")
def download(filename):
    # Serve the specified file from the specified directory
    return send_from_directory("database", filename, as_attachment=True)

# Run the app
if __name__ == "__main__":
    app.run(host="localhost", port=8080)
