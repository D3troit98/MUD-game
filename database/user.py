import sqlite3


def register_user():
  # Prompt the user for their name, email, and password
    userDictionary = {}
    name = input("Enter your name: ").lower()
    email = input("Enter your email: ").lower()
    password = input("Enter your password: ").lower()
    password2 = input("Enter your password: ").lower()
    score = 0
    health = 3
    level = 1
    if password == password2:
       # Connect to the database
      conn = sqlite3.connect('users.db') 

     # Creating a cursor object using the
     # cursor() method
      cursor = conn.cursor()

      #first check if a user with that email exist
      cursor.execute("SELECT * FROM USERS WHERE email = ?",(email,))
      result = cursor.fetchone()
      if result:
        print("Someone already exist with that email")
        
      
      else:
      # Queries to INSERT records.
        cursor.execute('''INSERT INTO USERS  ('name', 'email', 'password','score','health', level)VALUES (?, ? , ?,?, ?, ?)''',(name,email,password,score,health,level))
      # Print a success message
        print("Data Inserted in the table: ")
      # data=cursor.execute('''SELECT * FROM USERS''')
      # for row in data:
      #   print(row)
      
        userDictionary = {
        "name": name,
        "password":password,
        "score": score,
        "health": health,
        "level": level
    }
    else :
      # Print a success message
        print("Registration failed password doesn't match")
        
    # Commit your changes in the database 
    conn.commit()  
    # Closing the connection 
    conn.close()
    return userDictionary


def loginUser():
    # Prompt the user for their name, email, and password
    userDictionary = {}
    email = input("Enter your email: ").lower()
    password = input("Enter your password: ").lower()

    # Connect to the database
    conn = sqlite3.connect('users.db') 

    cursor = conn.cursor()

    #using where to check if username exist
    cursor.execute("SELECT * FROM USERS WHERE email = ?",(email,))

    result = cursor.fetchone()


    if result:
        if result[2] == password:
            userDictionary = {    "name": result[1],    "password":result[2],    "score": result[3],    "health": result[4],    "level": result[5]  }
            
        
        else:
            print("wrong password")
            
            
    else:
        print("User not found")    
               
            
    cursor.close()
    conn.close()  
    return userDictionary


def create_user():
  # Connecting to sqlite
  # connection object
  conn = sqlite3.connect('users.db')

  # cursor object
  cursor = conn.cursor()

 

  # Creating table

  cursor.execute("CREATE TABLE IF NOT EXISTS USERS ( Email TEXT, Name TEXT,password TEXT, Score INTEGER, Health INTEGER, level INTEGER) ")
  conn.commit()
  
  cursor.close()
  conn.close()
  

def list_users():
  conn = sqlite3.connect('users.db')
  print ("Opened database successfully")
  cursor = conn.execute("SELECT name from USERS")
  for row in cursor:
    print(row)

  print ("Operation done successfully")
  conn.close()





def storeData(p):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    new_data = (p.gold,p.hp,p.level,p.name)

    cursor.execute("UPDATE USERS SET Score=?, Health=?, level=? WHERE name=?",new_data)

    conn.commit()

    cursor.close()
    conn.close()


def listbyScore():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM USERS ORDER BY Score DESC")
    results = cursor.fetchall()
    for result in results:
        print(result)




def storeInTextFile():


    # Connect to the database
    conn = sqlite3.connect("users.db")

    # Create a cursor
    cursor = conn.cursor()

    # Execute a SQL query
    cursor.execute("SELECT * FROM USERS")

    # Fetch the data from the result set
    data = cursor.fetchall()

    # Open a text file for writing
    with open("data.txt", "w") as file:
        # Write the data to the file
        for row in data:
            file.write(str(row) + "\n")

    # Close the database connection
    conn.close()

  
    