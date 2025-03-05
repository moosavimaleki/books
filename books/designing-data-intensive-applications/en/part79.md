*  
A third option is to encode jobs, education, and contact info as a JSON or XML document, store it on a text column
in the database, and let the application interpret its structure and content. In this setup,
you typically cannot use the database to query for values inside that encoded column. ![ddia 0201](assets/ddia_0201.png) ###### Figure 2-1. Representing a LinkedIn profile using a relational schema. Photo of Bill Gates courtesy of Wikimedia Commons, Ricardo Stuckert, Agência Brasil. 
For a data structure like a résumé, which is mostly a self-contained document, a JSON
representation can be quite appropriate: see [Example 2-1](#fig_billgates_json). JSON has the appeal of being
much simpler than XML. Document-oriented databases like MongoDB
[[9](ch02.html#MongoDB2013)],
RethinkDB
[[10](ch02.html#RethinkDB2013)],
CouchDB
[[11](ch02.html#CouchDB2014_ch2)],
and Espresso
[[12](ch02.html#Qiao2013uv_ch2)]
support this data model. ##### Example 2-1. Representing a LinkedIn profile as a JSON document ```
`{`
  `"user_id"``:`     `251``,`
  `"first_name"``:`  `"Bill"``,`
  `"last_name"``:`   `"Gates"``,`
  `"summary"``:`     `"Co-chair of the Bill & Melinda Gates... Active blogger."``,`
  `"region_id"``:`   `"us:91"``,`
  `"industry_id"``:` `131``,`
  `"photo_url"``:`   `"/p/7/000/253/05b/308dd6e.jpg"``,`
  `"positions"``:` `[`
    `{``"job_title"``:` `"Co-chair"``,` `"organization"``:` `"Bill & Melinda Gates Foundation"``},`
    `{``"job_title"``:` `"Co-founder, Chairman"``,` `"organization"``:` `"Microsoft"``}`
  `],`
  `"education"``:` `[`
    `{``"school_name"``:` `"Harvard University"``,`       `"start"``:` `1973``,` `"end"``:` `1975``},`
    `{``"school_name"``:` `"Lakeside School, Seattle"``,` `"start"``:` `null``,` `"end"``:` `null``}`
  `],`
  `"contact_info"``:` `{`
    `"blog"``:`    `"http://thegatesnotes.com"``,`
    `"twitter"``:` `"http://twitter.com/BillGates"`
  `}`
`}`
```