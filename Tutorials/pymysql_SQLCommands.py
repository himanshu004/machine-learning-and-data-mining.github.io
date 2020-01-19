#pip install pymysql
import pymysql

def main():
    
    # Defining and manipulating database

    # Establish database connection
    conn = pymysql.connect("localhost","root","","workshop")
    print('Database Connected Successfully!!')
    
    # Create a cursor
    cur = conn.cursor()

    # Create a table
    cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")
    songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
    for song in songs:
        cur.execute("INSERT INTO song (title) VALUES (%s)", song)

    idNum=input('which id do you want')
    cur.execute("SELECT * FROM song WHERE id =" + idNum)
    print(cur.fetchall())
    conn.commit()

    # Close the connection
    conn.close()
    
if __name__ == '__main__':
  main()
