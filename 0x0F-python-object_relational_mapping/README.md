Python - Object-relational mapping


 0. Get all states
   Python script that uses MySQLdb
  to list all states in the database `hbtn_0e_0_usa`.


 1. Filter states
   Python script that uses MySQLdb
  to list all states with names starting with `N` in the database `hbtn_0e_0_usa`.
  

 2. Filter states by user input
 Python script that uses
  MySQLdb to display all values matching a given name in the `states` table of
  the database `hbtn_0e_0_usa`.
  

 3. SQL Injection...
 Python script
  that uses MySQLdb to display all values matching a given name in the `states`
  table of the database `hbtn_0e_0_usa`.
  

 4. Cities by states
  Python script that uses
  MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
  

 5. All cities by state
   Python script that uses MySQLdb
  to list all cities of a given state in the database `hbtn_0e_4_usa`.
  

 6. First state model
 Python module defining a class `State`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

 7. All states via SQLAlchemy
  Python script
  that uses SQLAlchemy to list all `State` objects from the database
  `hbtn_0e_6_usa`.
  
 8. First state
  Python script
  that uses SQLAlchemy to print the first `State` object from the database
  `hbtn_0e_6_usa`, ordered by `states.id`.
  

 9. Contains `a`
  Python script
  that uses SQLAlchemy to list all `State` objects that contain the letter `a`
  in the database `hbtn_0e_6_usa`.
  

 10. Get a state
   Python script that
  uses SQLAlchemy to print the `id` of the `State` object with name matching that
  passed as argument in the database `hbtn_0e_6_usa`.
  

 11. Add a new state
 Python script that
  uses SQLAlchemy to add the `State` object "Louisiana" to the database
`hbtn_0e_6_usa`.
  

 12. Update a state
  Python
  script that uses SQLAlchemy to change the name of the `State` object with
  `id = 2` in the database `hbtn_0e_6_usa` to "New Mexico".
  


 13. Delete states
  Python script
  that uses SQLAlchemy to delete all `State` objects with a name containing the
  letter `a` from the database `hbtn_0e_6_usa`.


 14. Cities in state
  Python module defining a class `City`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.

 15. City relationship
  Python module defining a
  class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `states`.
   Python module defining a
  class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `cities`.
  Python script that uses SQLAlchemy to add the `State` "California" with `City`
  
 16. List relationship
  Python script that uses SQLAlchemy to list all `State` and corresponding
  `City` objects in the database `hbtn_0e_101_usa`.

 17. List city
  Python script that uses SQLAlchemy to list all `City` objects from the database
  `hbtn_0e_101_usa`.

