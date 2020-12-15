from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ""
 
@app.route("/search/<query>")
def search(query):
    return ""

@app.route("/vcard/<url>")
def vcard(url):
    return ""

app.run("0.0.0.0", 8080)
