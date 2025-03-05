*  If the selected class is removed (e.g., because the user clicks a different page), the blue
color won’t be removed, even if the code is rerun—and so the item will remain highlighted
until the entire page is reloaded. With CSS, the browser automatically detects when the li.selected > p
rule no longer applies and removes the blue background as soon as the selected class is
removed. *  If you want to take advantage of a new API, such as document.getElementsByClassName("selected")
or even document.evaluate()—which may improve performance—you have to rewrite the code.
On the other hand, browser vendors can improve the performance of CSS and XPath without breaking
compatibility. 
In a web browser, using declarative CSS styling is much better than manipulating styles imperatively in
JavaScript. Similarly, in databases, declarative query languages like SQL turned out to be much
better than imperative query APIs.[vi](ch02.html#idm140605782079584) ## MapReduce Querying MapReduce is a programming model for processing large amounts of data in bulk across many
machines, popularized by Google
[[33](ch02.html#Dean2004ua_ch2)]. A limited form of MapReduce is supported by
some NoSQL datastores, including MongoDB and CouchDB, as a mechanism for performing read-only
queries across many documents.