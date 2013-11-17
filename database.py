import sys
import os
import psycopg2
import urlparse

conn = None
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS savedimage")
cur.execute("CREATE TABLE savedimage(id serial,title text,imagedata text)")
con.commit()
con.close()
