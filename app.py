from flask import Flask
from flask import request
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)

def scrape_for(query):
    url = "https://panoramafirm.pl/szukaj?k={}".format(query)
    company_selector = "#company-list li.company-item"
    company_name_selector = "a.company-name"
    company_mail_selector = "a.icon-envelope"
    company_phone_selector = "a.icon-telephone"
    company_address_selector = "div.address"
    
    response = urlopen(url)
    html = BeautifulSoup(response.read())
    selected_elements = html.select(company_selector)
    
    result = []
    
    for e in selected_elements:
#         out_str += e.select(company_name_selector)[0].getText() + "<br />"
        #  maili, numerów telefonów, adresów
        result.append({
            "name": e.select(company_name_selector)[0].getText(),
            "mail": e.select(company_mail_selector)[0]["data-company-email"],
            "phone": e.select(company_phone_selector)[0]["data-original-title"],
            "address": e.select(company_address_selector)[0]["href"],
        })
        
    return result

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
    return page_with("<code>" + str(scrape_for(query)) + "</code>")

@app.route("/vcard/<url>")
def vcard(url):
    return ""

app.run("0.0.0.0", 8080)
