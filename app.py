from flask import Flask
from flask import request
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)

def scrape_for(query):
    url = "https://panoramafirm.pl/szukaj?k={}".format(query)
    company_selector = "#company-list li.company-item"
    company_name_selector = "a.company-name"
    
    response = urlopen(url)
    html = BeautifulSoup(response.read())
    selected_elements = html.select(company_selector)
    
    out_str = ""
    
    for e in selected_elements:
        out_str += e.select(company_name_selector)[0].getText() + "<br />"
        
    return out_str

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
    query = request.args.get("query")
    return page_with("<code>" + scrape_for(query) + "</code>")

@app.route("/vcard/<url>")
def vcard(url):
    return ""

app.run("0.0.0.0", 8080)
