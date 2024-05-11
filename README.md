### Introduction to FastAPI and SQLALCHEMY

This is a short implementation of fastapi to perform basic CRUD operations using SQLITE database.
In this repository, I have implemented FastAPI to get, put, post and delete field of a database.
Pydantic model is used to create base model and ORM is used to map the object to the table.
Two tables are created 'users' and 'items'. These table have many-to-many mapping. 'owner_id' is used as 
a Foreign_Key in 'items' table to map the id of the user in 'users' table. 

### Funtions Performed:-
 1. Users can be created and added to the 'users' table.
 2. Users can be retrieved from the table either all, or by user_id
 3. Items can be created, its owner can be assigned and added to the 'items' table.
 4. Items can be retrieved from the table either all, or by item_id
 5. Users can be removed by 'user_id'
 6. Items can be removed by 'item_id'
 7. Users can be updated
 8. Items can be updated 
