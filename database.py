import sys
import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS savedimage")
cur.execute("CREATE TABLE savedimage(id serial,title text,imagedata text)")
conn.commit()
conn.close()
