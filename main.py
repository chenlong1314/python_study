import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='11111111', db='mysql', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    print "Database version : %s" % data


except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

finally:
    if conn:
        conn.close()

