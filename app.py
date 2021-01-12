from flask import Flask
from flask import Response
from flask import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from vobject import vCard

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
        result.append({
            "name": e.select(company_name_selector)[0].getText(),
            "mail": e.select(company_mail_selector)[0]["data-company-email"],
            "phone": e.select(company_phone_selector)[0]["title"],
            "address": e.select(company_address_selector)[0].getText()
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
    
def vCardButtonFor(company):
    return """
        <form method="post" action="/vcard">
            <input type="hidden" name="name" value=\"""" + company["name"] + """\" />
            <input type="hidden" name="mail" value=\"""" + company["mail"] + """\" />
            <input type="hidden" name="phone" value=\"""" + company["phone"] + """\" />
            <input type="hidden" name="address" value=\"""" + company["address"] + """\" />
            <input type="submit" value="Generuj vCard" />
        </form>
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
    content = ""
    
    for company in scrape_for(query):
        content +=  "<div style=\"margin: 20px 0px\">" + \
                        "<div>Nazwa: " + company["name"] + "</div>" + \
                        "<div>Mail: " + company["mail"] + "</div>" + \
                        "<div>Telefon: " + company["phone"] + "</div>" + \
                        "<div>Adres: " + company["address"] + "</div>" + \
                        vCardButtonFor(company) + \
                    "</div>"
                    
    return page_with(content)

@app.route("/vcard", methods = ["POST"])
def vcard():
    vc = vCard()
    
    vc.add("fn")
    vc.fn.value = request.form.get("name")
    
    vc.add("email")
    vc.email.value = request.form.get("mail")
     
    vc.add("tel")
    vc.tel.value = request.form.get("phone")
     
#     vc.add("adr")
#     vc.adr.value = request.form.get("address")
    
    return Response(vc.serialize(), mimetype="text/vcard")

app.run("0.0.0.0", 8080)
