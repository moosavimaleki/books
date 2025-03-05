*  How many more bananas than usual did we sell during our latest promotion? *  Which brand of baby food is most often purchased together with brand X diapers? 
These queries are often written by business analysts, and feed into reports that help the management
of a company make better decisions (business intelligence). In order to differentiate this pattern
of using databases from transaction processing, it has been called online analytic processing
(OLAP) [[47](ch03.html#Codd1993ww)].[iv](ch03.html#idm140605777918240)
The difference between OLTP and OLAP is not always clear-cut, but some typical characteristics are
listed in [Table 3-1](#tab_oltp_vs_olap). Table 3-1. Comparing characteristics of transaction processing versus analytic systems Property
Transaction processing systems (OLTP)
Analytic systems (OLAP) Main read pattern Small number of records per query, fetched by key Aggregate over large number of records Main write pattern Random-access, low-latency writes from user input Bulk import (ETL) or event stream Primarily used by End user/customer, via web application