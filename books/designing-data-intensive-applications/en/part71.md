# Chapter 2. Data Models and Query Languages

# Chapter 2. Data Models and Query Languages The limits of my language mean the limits of my world. Ludwig Wittgenstein, Tractatus Logico-Philosophicus (1922) ![](assets/ch02-map-ebook.png) 
Data models are perhaps the most important part of developing software, because they have such a
profound effect: not only on how the software is written, but also on how we think about the problem
that we are solving. Most applications are built by layering one data model on top of another. For each layer, the key
question is: how is it represented in terms of the next-lower layer? For example: 1.  
As an application developer, you look at the real world (in which there are people,
organizations, goods, actions, money flows, sensors, etc.) and model it in terms of objects or
data structures, and APIs that manipulate those data structures. Those structures are often
specific to your application. 2.  When you want to store those data structures, you express them in terms of a general-purpose
data model, such as JSON or XML documents, tables in a relational database, or a graph model.