### SQL databases / Relational databases
- Data can be stored in tables according to the restrictions defined by schema of that table.</br>
  Some of the examples for restrictions are `No of columns & Data types`, `Primary key` & `Foreign key`.
- The language used to queries is `SQL(Structured Query Language)`. Observe the word `Structure`, used because the</br>
  data on which these queries will operate is in structurally organized in tables nealty. That's why it's named</br>
  as SQL database.
- Complaince with ACID principles.
#### Atomicity
This principle says, entire query has to be executed successfully, else the database should be reversed to it's original state</br>
of before executing the query. This is achieved through loggin mechanism
![image](https://github.com/user-attachments/assets/5043f92e-5ba7-44da-983a-06b9b32d5adc)
Example:
![image](https://github.com/user-attachments/assets/2e2819e4-c0a3-47bf-ab81-3103ded2c2cd)
#### Consistency</br>
This principle says, query will be executed only if it meets predefined constraints putup by triggers.
![image](https://github.com/user-attachments/assets/3751de21-92ae-41e0-a817-76f63b3347f2)
Example:
Let's consider there is an trigger defined saying that the Available balance can't go less than `0`.</br>
When such trigger is in place, below query will be stopped from execution, to maintain data consistency</br>
before & after executing the query.
![image](https://github.com/user-attachments/assets/42681971-f853-4704-8bf2-d3f3ba85789d)

#### Isolation</br>
Even though the database gets request to execute 2 queries at a time, it will randomly pick any one qurey frist</br>
& only after completing the execution of first query, second query will be executed.

#### Durability</br>
All the data changes will be saved into disk, on execution of `commit`.
