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
refined=[]
for x in collect:
        if 1000<=int(x[3])<=1999:
                refined.append(x)


base_setup="""
[general]
alwaysauthreject=yes
videosupport=yes
disallow=all
allow=ulaw,alaw,h263,h264,h263p
register => primary:welcome@10.10.0.5/secondary
register => primary:welcome@10.30.0.4/tertiary

[secondary]
type=friend
secret=welcome
context=incoming
host=dynamic
qualify=yes

[tertiary]
type=friend
secret=welcome
context=incoming
host=dynamic
qualify=yes
"""
sip_list=[]
for x in refined:
        exten="""
["""+x[3]+"""]
type=friend
callerid="""+'"'+x[1]+'"'+"""
secret="""+x[2]+"""
host=dynamic
context=LocalExt
"""
        sip_list.append(exten)
for x in sip_list:
        print(x)
f = open("/etc/asterisk/sip.conf","w+")
f.write(base_setup)
for x in sip_list:
        f.write(x)
f.close
asterisk_restart="sudo systemctl restart asterisk"
os.system(asterisk_restart)
