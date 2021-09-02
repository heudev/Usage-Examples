from flask import Flask, request, render_template, redirect, flash, session, make_response, url_for, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "aasdasdasdqweqwddasdasdacxzxcasdads"

# ------------------------------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")

# ------------------------------------------------------------------


class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password


user1 = Users("enes", "123")
user2 = Users("joe", "456")
user3 = Users("james", "789")
database = [user1, user2, user3]


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        for data in database:
            if username == data.username and password == data.password:
                session["username"] = username
                return render_template("admin.html")
            else:
                flash("error")
                return redirect("/login")
    else:
        return render_template("login.html")

# ------------------------------------------------------------------


@app.route("/urlfor")
def urlfor():
    return redirect(url_for("users", name="enes", surname="uysal"))


@app.route("/login/<name>/<surname>")
def users(name, surname):
    return render_template("users.html", name=name, surname=surname)

# ------------------------------------------------------------------


@app.route("/file", methods=["POST", "GET"])
def filee():
    if request.method == "POST":
        f = request.files.get("file")
        f.save(secure_filename(f.filename))
        flash("Dosya yüklendi")
        return redirect("/file")
    else:
        return render_template("file.html")

# ------------------------------------------------------------------


@app.route("/session")
def sessionn():
    if "username" not in session:
        session["session_name"] = "session_value"
    return render_template("index.html")

# ------------------------------------------------------------------


@app.route("/cookie")
def cookie():
    getcookie = request.cookies.get("get")
    if not getcookie:
        response = make_response(render_template("index.html"))
        response.set_cookie("cookie_name", "cookie_value")
        return response

# ------------------------------------------------------------------


@app.route("/logoutall")
def logoutall():
    for key in list(session.keys()):
        session.pop(key)
    flash("Logged Out All")
    return redirect("/")

# ------------------------------------------------------------------


@app.route("/logout")
def logout():
    del session["session_name"]
    flash("Logged Out")
    return redirect("/")

# ------------------------------------------------------------------


@app.route("/abort")
def abortt():
    abort(404)

# ------------------------------------------------------------------


@app.route("/<x>")
def error(x):
    return redirect("/")

# ------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)


""" 
from werkzeug.security import generate_password_hash, check_password_hash

hashpassword = generate_password_hash("password")
# >>> pbkdf2:sha256:150000$JFPyfGS0$469d56a1d45f8dadb48f03d3be5d422874d4a8904492bcb8ca138c6bec6b370f

check_password_hash(hashpassword, "password")
# >>> True or False
"""
