#!/usr/bin/python
import cgi
import cgitb
import requests
import sqlite3
from gym import *


cgitb.enable()

print("Content-Type: text/html\r\n\r\n")
print('''
<!DOCTYPE html>
<head>
<title>FitFinder Results</title>
<link href="https://fonts.googleapis.com/css?family=Arimo|Merriweather|Noto+Serif+SC|Open+Sans|Open+Sans+Condensed:300|Roboto" rel="stylesheet">

<style>
table{
    border =2;
    font-family: 'Roboto', sans-serif;
    width: 80%;
    margin-left:auto;
    margin-right:auto;
    background-color:rgba(202,202,202,0.9);
    font-size:14pt;
}
h1{
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Cagliostro', sans-serif;
}
p{
    font-size:12pt;
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Cagliostro', sans-serif;
}

body{
    background-image:url("Img/gym2.jpg")
}

footer{
    width:80%;
    margin-left:auto;
    margin-right:auto;
    background-color:rgba(202,202,202,0.9)
}

#img{
    width:80%;
    margin-left:auto;
    margin-right:auto;
}
</style>

</head>
<body>''')

def get_google_link(address):
    return "https://www.google.com/maps/place/"+address

form = cgi.FieldStorage()
sort = form.getvalue("sort")

if form.getvalue("zip"):
    zip_code = form.getvalue("zip")
else:
    zip_code = "10003"

limit = form.getvalue("limit")
executed = gym("gym",zip_code)
#write to table completed
print("<table border = 1>")
print("<tr>")
print("<th>Gym</th>")
print("<th>Address</th>")
print("<th>City</th>")
print("<th>Distance(in meters)</th>")
print("<th>Rating</th>")
print("<th>Contact</th>")
print("<th>Link</th>")
print("</tr>")

row_template = '''
<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</tr>
'''
conn = sqlite3.connect("fitfinder.db")
c = conn.cursor()

if sort == "rating":
    query_template = '''
    SELECT name, address_1, city, distance, rating, phone,url
    FROM gym_table
    WHERE zip_code = {}
    ORDER BY {} DESC
    LIMIT {};
    '''
elif sort == "distance":
    query_template = '''
    SELECT name, address_1, city, distance, rating, phone,url
    FROM gym_table
    WHERE zip_code = {}
    ORDER BY {}
    LIMIT {};
    '''
query = query_template.format(zip_code,sort,limit)

c.execute(query)
result = c.fetchall()


url_template = '''<a href="{}" target="_blank">Website</a>'''
address_template= '''<a href="{}" target="_blank">{}</a>'''

for row in result:
    print(row_template.format(row[0],address_template.format(get_google_link(row[1]),row[1]),row[2],row[3],row[4],row[5],url_template.format(row[6])))

plot = '''
<a href="Img/plot/{}.jpg">Visualize It!</a>
'''

zipc = ['10002', '10003', '10005', '10007', '10009', '10011', '10012', '10014', '10016', '10018', '10019', '10022',
       '10023', '10025', '10027', '10028', '10029', '10030', '10032', '10033', '10034', '10035', '10036', '10038',
       '10039', '10040', '10065', '10075', '10128', '10172', '10280', '11101', '11103']
if zip_code in zipc:
    print(row_template.format(plot.format(zip_code),'','','','','',''))
print("</table>")





print("</body>")

print('''
<footer>
<hr/>
<a href="index.html"><img src="Img/goback2.png"></a>
</footer>
''')

print("</html>")
