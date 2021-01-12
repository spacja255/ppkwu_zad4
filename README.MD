# PPKWU - ZADANIE 4 - MOBILNY VCARD

## Details

API generating a mobile page using the search engine from `https://panoramafirm.pl/szukaj`, which allows you to generate a vCard file for each entry found

## Endpoints

### Request

`GET /`

### Response

Web page with search engine

### Request

`GET /search`

- `query` is string containing text to search for

### Response

Web page with search results

`POST /vcard`

- `name` is comapny name
- `mail` is comapny email address
- `phone` is comapny phone number
- `address` is comapny address

### Response

vCard file containing informations about selected company

### Example

```
BEGIN:VCARD
VERSION:3.0
ADR:;;ul. Wierzbowa 12\, 05-503 Robercin;;;;
EMAIL:rrrobert@vp.pl
FN:Hydraulika Montaż Instalacji Sanitarnych i Grzewczych Robert Rosłoniec
TEL:501 083 795
END:VCARD
```
