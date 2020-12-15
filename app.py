from flask import Flask
from flask import request

app = Flask(__name__)

def page_with(content):
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Mobilny vCard</title>
        </head>
        <body>
            """ + content + """
        </body>
        </html>
    """

@app.route("/")
def index():
    return page_with("""
        <form method="get" action="/search">
            <input type="text" name="query" placeholder="Enter query..." />
            <input type="submit" value="Search" />
        </form>
    """)
 
@app.route("/search")
def search():
    return page_with(request.args.get("query"))

@app.route("/vcard/<url>")
def vcard(url):
    return ""

app.run("0.0.0.0", 8080)
