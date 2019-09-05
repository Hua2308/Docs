* GET all column names:
```
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = <DATABASE_NAME> AND TABLE_NAME = <TABLE_NAME>
```

* INSERT or UPDATE:
```
INSERT INTO <TABLE>(Key, Field1, Field2, Field3) VALUS(<key_value>, <value>, <value>, <value>) ON DUPLICATE KEY UPDATE Field1 = <value> AND Field2 = <value>
```
	*  The statement first tries to insert a new row into the table. If a duplicate error occurs, it will update the existing row with the value specified in the **ON DUPLICATE KEY UPDATE** clause.
