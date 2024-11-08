Will implement below system step by step by learning theory, followed by implementing same thing whatever discussed in theory with code. 
#### 01_flask_server
On the first chapter, will create a simple flask server.</br> 
The duty of this server is to provide a response based on the data in a dictionary in flask program.

#### 02_sql_database
Since the data stored in this dictionary is not stored in any database, data inside it will be gone once we stop the server.</br>
Will add an `sql` database named `SQLite` & store the application data inside this database.

#### 03_caching_and_nosql
- As of now, even though same request comes to server, each time it is processed & the response is provided.</br>
  Instead of this, will store the response inside an `no_sql` database named `TinyDB`.
- Will also pratically verify wether we are getting data from database/cahce.
