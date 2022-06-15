import psycopg2
import csv 

conn = psycopg2.connect("host = localhost dbname=postgres user=postgres password= port=5432")
conn.autocommit = True     
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS seoul;")
cur.execute("""CREATE TABLE seoul(측정일자 date,
                                권역명 varchar, 
                                측정소명 varchar, 
                                미세먼지  real, 
                                초미세먼지 real, 
                                오존 real, 
                                이산화질소농도 real, 
                                일산화탄소농도 real, 
                                아황산가스농도 real);
                                """)

copy_sql = """
           COPY seoul (측정일자,권역명,측정소명, 미세먼지, 초미세먼지, 오존, 이산화질소농도, 일산화탄소농도, 아황산가스농도) FROM seoul DELIMITER ',' CSV HEADER
           """
with open('C:/Users/KDB/Desktop/CP2/seoul.csv', 'r') as f:
    next(f) 
    cur.copy_expert(copy_sql, f)
    conn.commit()
    conn.close()
f.close()
