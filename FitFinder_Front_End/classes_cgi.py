#!/usr/bin/python
import cgi
import cgitb
import sqlite3


cgitb.enable()

print("Content-Type: text/html\r\n\r\n")
print('''
<!DOCTYPE html>
<head>
<title>FitFinder Results</title>
<link href="https://fonts.googleapis.com/css?family=Arimo|Merriweather|Noto+Serif+SC|Open+Sans|Open+Sans+Condensed:300|Roboto" rel="stylesheet">
<style>
table{
    border =1;
    font-family: 'Roboto', sans-serif;
    width: 80%;
    margin-left:auto;
    margin-right:auto;
    background-color:rgba(202,202,202,0.9);
    font-size:12pt;
}
h1{
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Roboto', sans-serif;
}
p{
    font-size:12pt;
    width:80%;
    margin-left:auto;
    margin-right:auto;
    font-family: 'Roboto', sans-serif;
}

body{
    background-image:url("Img/atHome6.jpg");
}

footer{
    width:80%;
    margin-left:auto;
    margin-right:auto;
    background-color:rgba(202,202,202,0.9)
}
</style>

</head>
<body>''')

def get_google_link(address):
    return "https://www.google.com/maps/place/"+address

form = cgi.FieldStorage()
classes = form.getvalue("class")

days = ""
if form.getvalue("mon"):
      days += '"%Mon%" '
if form.getvalue("tue"):
      days += '"%Tue%" '
if form.getvalue("wed"):
      days += '"%Wed%" '
if form.getvalue("thu"):
      days += '"%Thu%" '
if form.getvalue("fri"):
      days += '"%Fri%" '
if form.getvalue("sat"):
      days += '"%Sat%" '
if form.getvalue("sun"):
      days += '"%Sun%" '
day_list = days.split()
where = " OR ".join(["day LIKE {}".format(i) for i in day_list])

limit = form.getvalue("limit")

print("<table border = 1>")
print("<tr>")
print("<th>Center</th>")
print("<th>Address</th>")
print("<th>Class</th>")
print("<th>Day</th>")
print("<th>Start Time</th>")
print("<th>Length</th>")
print("<th>Price</th>")
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
<td>{}</td>
</tr>
'''
url_template = '''<a href="{}" target="_blank">Website</a>'''
address_template = '''<a href="{}" target="_blank">{}</a>'''

conn = sqlite3.connect("fitfinder.db")
c = conn.cursor()

query = '''
SELECT center, address, class, day, start_time, length, price, url
FROM class_table
WHERE ({})
AND (class LIKE "%{}%")
GROUP BY center, address, class, day, start_time, length, price
ORDER BY RANDOM()
LIMIT {};
'''.format(where,classes,limit)


c.execute(query)

result = c.fetchall()
if result != []:
    for row in result:
        print(row_template.format(row[0],address_template.format(get_google_link(row[1]),row[1]),row[2],row[3],row[4],row[5],row[6],url_template.format(row[7])))

img = '''<a href="Img/class_avai.jpg">Visualize It!</a>'''
print(row_template.format(img,'','','','','','',''))
print("</table>")

print("</body>")

print('''
<footer>
<hr/>
<a href="index.html"><img src="Img/goback2.png"></a>
</footer>
''')
print("</html>")
