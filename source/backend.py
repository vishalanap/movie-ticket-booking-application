import sqlite3

#creating table in the database
def create_record():
    con=sqlite3.connect("movie.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (Movie_ID text PRIMARY KEY,Movie_Name text,Release_Date text,Director text,Cast text,Budget text,Duration text,Rating text,seats INT)")
    con.commit()
    con.close()

#storing movie records into the table 'book'  
def insert_record(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating,50))
    con.commit()
    con.close()

#fetching all the records in database
def view_record():
    con=sqlite3.connect("movie.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

#booking the seats 
def book_movies(Movie_ID="",Movie_Name=""):
    con=sqlite3.connect("movie.db")    
    cur=con.cursor()
    cur.execute("UPDATE book SET seats = seats - 1 WHERE (Movie_ID=? OR Movie_Name = ?) AND seats>0",(Movie_ID,Movie_Name))
    con.commit()
    con.close()

#checking availability of the seats
def available_seats(Movie_ID="",Movie_Name=""):
    con=sqlite3.connect("movie.db")    
    cur=con.cursor()
    cur.execute("SELECT seats FROM book WHERE Movie_ID=? OR Movie_Name = ?",(Movie_ID,Movie_Name))
    temp=cur.fetchall()
    con.commit()
    con.close()
    return temp

#deleting the movie record
def delete_record(Movie_ID = "",Movie_Name = "",Release_Date="",Rating = ""):    
    con=sqlite3.connect("movie.db")    
    cur=con.cursor()
    query = "DELETE FROM book WHERE Movie_ID = '" + str(Movie_ID)
    query += "' OR Movie_Name = '" + str(Movie_Name)
    query += "' OR Release_Date = '" + str(Release_Date)
    query += "' OR Rating = '" + str(Rating) + "'"
    cur.execute(query)
    con.commit()
    con.close()  

#searching movies based on given criteria
def search_record(Movie_ID = "",Movie_Name = "",Release_Date = "",Duration = "",Rating = ""):  
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    query = "SELECT * FROM book WHERE Movie_ID = '" + str(Movie_ID)
    query += "' OR Movie_Name = '" + str(Movie_Name)
    query += "' OR Release_Date = '" + str(Release_Date)
    query += "' OR Duration = '" + str(Duration)
    query += "' OR Rating = '" + str(Rating) + "'"
    cur.execute(query)
    rows=cur.fetchall()
    con.close()    
    return rows