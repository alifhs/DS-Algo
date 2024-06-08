### How to create an index ?

Run the below command to create an index on a column


```
create index customers_company_name on customers(company_name);
```

### Check how much time it takes to query

```
explain analyze select contact_name from customers where company_name='Alfreds Futterkiste';
```



### 1. Improved Query Performance

- **Faster Data Retrieval**: Indexes are designed to speed up the retrieval of data. When a query searches for records based on an indexed column, the database can quickly locate the data using the index, rather than scanning every row in the table.
- **Reduced I/O Operations**: By minimizing the need to scan the entire table, indexes reduce the number of input/output operations, making data retrieval more efficient.

### 2. Types of Indexes

- **B-tree Indexes**: The default index type in PostgreSQL and many other databases. It's well-suited for a wide variety of queries, including equality and range queries.
- **Hash Indexes**: Used for equality comparisons. However, their use is limited compared to B-tree indexes.

### 3. Storage and Maintenance Overhead

- **Additional Storage**: Indexes require additional storage space. The size depends on the number of columns indexed, the data type of these columns, and the number of rows in the table.
- **Maintenance Costs**: Indexes need to be updated whenever data is inserted, updated, or deleted. This can slow down write operations (INSERT, UPDATE, DELETE) because the index also needs to be maintained.


### 4. Estimation of extra storage

- If you have a 200 KB database and you add a new index on an integer column with around 10,000 rows, the index might consume approximately 240 KB. This would more than double the size of your database to around 440 KB.
