![ddia 0309](assets/ddia_0309.png) ###### Figure 3-9. Example of a star schema for use in a data warehouse. Usually, facts are captured as individual events, because this allows maximum flexibility of
analysis later. However, this means that the fact table can become extremely large. A big
enterprise like Apple, Walmart, or eBay may have tens of petabytes of transaction history in its data
warehouse, most of which is in fact tables [[56](ch03.html#Harris2013un)]. 
Some of the columns in the fact table are attributes, such as the price at which the product was
sold and the cost of buying it from the supplier (allowing the profit margin to be calculated).
Other columns in the fact table are foreign key references to other tables, called dimension
tables. As each row in the fact table represents an event, the dimensions represent the who,
what, where, when, how, and why of the event. For example, in [Figure 3-9](#fig_dwh_schema), one of the dimensions is the product that was sold. Each row in
the dim_product table represents one type of product that is for sale, including its stock-keeping
unit (SKU), description, brand name, category, fat content, package size, etc. Each row in the
fact_sales table uses a foreign key to indicate which product was sold in that particular
transaction. (For simplicity, if the customer buys several different products at once, they are
represented as separate rows in the fact table.)