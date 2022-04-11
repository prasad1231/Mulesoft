
#importing sqlite3 module
import sqlite3

#defining connection and cursor
connection = sqlite3.connect('training.db')  #training.db is the database created before

cursor = connection.cursor()

#creating table movies with required required attributes[columns]
cmd1= """CREATE TABLE  IF NOT EXISTS
MOVIES(NAME TEXT, ACTOR TEXT, ACTRESS TEXT, DIRECTOR TEXT,YEAR_OF_RELEASE INTEGER)"""

cursor.execute(cmd1)

#adding/inserting values into table movies
cursor.execute("INSERT INTO MOVIES VALUES ('IRON MAN','ROBERT DOWNEY','GWYNETH PALTROW','JON FAVREAU',2008)")
cursor.execute("INSERT INTO MOVIES VALUES ('BAHUBALI','PRABHAS','ANUSHKA','RAJAMOULI',2015)")
cursor.execute("INSERT INTO MOVIES VALUES ('KGF','YASH','SRINIDHI','PRASHANT NEEL',2016)")
cursor.execute("INSERT INTO MOVIES VALUES ('3 IDIOTS','AAMIR','KAREENA','RAJKUMAR HIRANI',2009)")
cursor.execute("INSERT INTO MOVIES VALUES ('RED NOTICE','DWYANE JOHNSON','GAL GADOT','RAWSON',2021)")
cursor.execute("INSERT INTO MOVIES VALUES ('DON','SHAHRUKH','PRIYANKA','FARHAN',2006)")


#querying data from the table
cursor.execute("SELECT * FROM MOVIES")
cursor.execute("SELECT NAME FROM MOVIES WHERE ACTOR='PRABHAS'")  
#the last query's output is displayed 


#additional commands
#cursor.execute("SELECT * FROM MOVIES WHERE YEAR_OF_RELEASE=2008")-----query based on year of release
#------DELETE COMMAND-----cursor.execute("DELETE FROM MOVIES WHERE DIRECTOR='FARHAN'")--------entire row is deleted
#------DROP COMMAND-----cursor.execute("DROP TABLE MOVIES")------movies table is completly deleted
#------ALTER COMMAND-----cursor.execute("ALTER TABLE MOVIES ADD(RATING INTEGER)")--------addition of new column


#displaying the output
res=cursor.fetchall()
print(res)
