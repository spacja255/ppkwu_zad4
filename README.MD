# PPKWU - ZADANIE 4 - MOBILNY VCARD

## Details

API generating a mobile page using the search engine from `https://panoramafirm.pl/szukaj`, which allows you to generate a vCard file for each entry found

## Endpoints

### Request

`GET /`

### Response

Web page with search engine

### Request

`GET /search/<query>`

- `<query>` is string containing text to search for

### Response

Web page with search results

`GET /vcard/<url>`

- `<url>` is string containing url for selected company

### Response

vCard file containing informations about selected company
