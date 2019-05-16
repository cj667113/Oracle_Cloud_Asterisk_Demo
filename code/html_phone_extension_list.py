import mysql.connector
import os
print("trying")
cnx = mysql.connector.connect(user='primary_test', password='test_password', host='10.0.0.10', port='3306', database='Authentication')
print("done")
mycursor = cnx.cursor()
sql = "SELECT * FROM users WHERE Extension"
mycursor.execute(sql)
myresult = mycursor.fetchall()
cnx.close()
collect=[]
for x in myresult:
        precollect=[]
        for y in x:
                y=(str(unicode(y)).strip("u'"))
                precollect.append(y)
        collect.append(precollect)


pre_html="""
<html>
<head>
</head>
<body>
<center>
<table style="width:100%" border="1">
<tr>
<th>
Name
</th>
<th>
Extension
</th>
</tr>
"""
post_html="""
</center>
</table>
</body>
</html>
"""

sip_list=[]
for x in collect:
        exten="""
<tr>
<td>"""+x[1]+"""</td>
<td>"""+x[3]+"""</td>
"""
        sip_list.append(exten)
for x in sip_list:
        print(x)
f = open("/var/www/html/phone_extension.html","w+")
f.write(pre_html)
for x in sip_list:
        f.write(x)
f.write(post_html)
f.close()
