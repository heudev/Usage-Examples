import os

os.system("mkdir templates")
os.system("mkdir static")
os.system("mkdir static\img")
os.system("mkdir static\js")
os.system("mkdir static\css")

with open("app.py", "a") as file:
    file.write("""
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<x>")
def error404(x):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
""".strip())

with open("templates/theme.html", "a") as file:
    file.write(""" 
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css">
    <link rel="shortcut icon" type="image/png" href="https://picsum.photos/50" />
    {% block head %}
    {% endblock head %}
</head>
<body class="bg-dark text-white">
    <nav class="navbar navbar-dark bg-gradient border-bottom border-5 border-warning rounded-bottom">
        <div class="container-fluid">
            <a class="navbar-brand ms-xl-5" href="/">
                <img src="https://picsum.photos/200" height="30" class="d-inline-block align-text-top rounded">
                <i class="text-decoration-underline"><b>Flask project</b></i>
            </a>
        </div>
    </nav>
    {% block body %}
    {% endblock body %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""".strip())

with open("templates/index.html", "a") as file:
    file.write("""
{% extends "theme.html" %}

{% block head %}
<title>index</title>
{% endblock head %}

{% block body %}
<h1 class="text-center mt-5">Python</h1>
{% endblock body %}
""".strip())
