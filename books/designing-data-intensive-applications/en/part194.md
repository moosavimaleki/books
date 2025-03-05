Internal analyst, for decision support What data represents Latest state of data (current point in time) History of events that happened over time Dataset size Gigabytes to terabytes Terabytes to petabytes At first, the same databases were used for both transaction processing and analytic queries. SQL
turned out to be quite flexible in this regard: it works well for OLTP-type queries as well as
OLAP-type queries. Nevertheless, in the late 1980s and early 1990s, there was a trend for companies
to stop using their OLTP systems for analytics purposes, and to run the analytics on a separate
database instead. This separate database was called a data warehouse. ## Data Warehousing 
An enterprise may have dozens of different transaction processing systems: systems
powering the customer-facing website, controlling point of sale (checkout) systems in physical
stores, tracking inventory in warehouses, planning routes for vehicles, managing suppliers,
administering employees, etc. Each of these systems is complex and needs a team of people to
maintain it, so the systems end up operating mostly autonomously from each other.