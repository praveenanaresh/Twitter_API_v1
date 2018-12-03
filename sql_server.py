

import pyodbc


connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=xxxx;Database=xxxx;Uid=xxxx;Pwd=xxxx;'

# Use .connect (DB API 2.0) to get a Connection Object
conn = pyodbc.connect(connection_string,autocommit=True) # autocommit = True, since it is the SQL Server way

# Create the cursor object
curs = conn.cursor()



# Insert some cpi data (R.B.A.R) !
# We are using the .executemany DB API V2.0 Method
import csv
insert_query = 'insert into twitter_analytics_2018 (USER_HASHTAGS,USER_TWEETS,USER_NAME,USER_LOCATION) values (?,?,?,?)'
with open(r'/Users/pb/Desktop/Documents/MIS_5400/Project/Twitter-API/saved_tweets_new.csv', 'r',encoding='utf8') as cpi_file:
    cpi = csv.reader(cpi_file)
    curs.executemany(insert_query, cpi)



# Commit and close the connection
conn.commit()
conn.close()




curs.execute(bulk_insert_sql)
conn.commit()
curs.close()
conn.close()


