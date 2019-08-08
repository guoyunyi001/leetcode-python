here are some tips for writing or improving sql query, which are a summary of online articals. 
Tips:
1. Use EXISTS instead of IN to check existence of data.
notes: good resource to understand http://www.dba-oracle.com/t_exists_clause_vs_in_clause.htm
       The Exists keyword evaluates true or false, but the IN keyword will compare all values in the corresponding subuery column.  
       If you are using the IN operator, the SQL engine will scan all records fetched from the inner query. 
       On the other hand, if we are using EXISTS, the SQL engine will stop the scanning process as soon as it found a match.
  
2. Use UNION instead of the OR operator. 
   OR - makes the database fetch the results of each part of the condition separately.
   UNION - This alternative will allow you to index each of the conditions separately, 
           so the database will use the indexes to search for the results and then combine the results with the UNION clause.
 

