### SQL databases / Relational databases
- Data can be stored in tables according to the restrictions defined by schema of that table.</br>
  Some of the examples for restrictions are `No of columns & Data types`, `Primary key` & `Foreign key`.
- The language used to queries is `SQL(Structured Query Language)`. Observe the word `Structure`, used because the</br>
  data on which these queries will operate is in structurally organized in tables nealty. That's why it's named</br>
  as SQL database.
- Complaince with ACID principles.

#### Atomicity
- `Atom` is somethng which can't be split any more. In the sameway, Atomicity principle says</br>
"treat entire query as single transaction", even though it is doing multilpe operations inside that single query.
- Treating the entire query as a single transaction means, execute the query only if it gets succeeded on all operations</br>
performed by that query else rollback the database to it's original state of before executing the query.
![image](https://github.com/user-attachments/assets/2e2819e4-c0a3-47bf-ab81-3103ded2c2cd)

#### Isolation</br>
- Even though the database gets request to execute 2 queries at a time, it will randomly pick any one qurey frist</br>
& only after completing the execution of first query, second query will be executed.
- Observe that `Atomicity` principle is dealing with single query, where as the `Isolation` principle is dealing</br>
with multiple queries.
- Doing so will protect from below dangers.
  1. Dirty reads
  2. Phantom reads
  3. Non repeatable reads

#### Consistency</br>
- This principle says, query will be executed only if it meets predefined constraints setup by triggers.
- Let's consider there is an trigger, saying that the Available balance can't go less than `0`.</br>
When such trigger is in place, below query will be stopped from execution, to maintain data consistency</br>
before & after executing the query.
![image](https://github.com/user-attachments/assets/42681971-f853-4704-8bf2-d3f3ba85789d)



#### Durability</br>
All the data changes will be saved into disk, on execution of `commit`.
