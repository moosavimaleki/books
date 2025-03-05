```
``
    ``
        ``
    ``
``
``` Here, the XPath expression li[@class='selected']/p is equivalent to
the CSS selector li.selected > p in the previous example. What CSS and XSL have in common is that
they are both declarative languages for specifying the styling of a document. Imagine what life would be like if you had to use an imperative approach. In JavaScript, using the
core Document Object Model (DOM) API, the result might look something like this: ```
`var` `liElements` `=` `document``.``getElementsByTagName``(``"li"``);`
`for` `(``var` `i` `=` `0``;` `i` `<` `liElements``.``length``;` `i``++``)` `{`
    `if` `(``liElements``[``i``].``className` `===` `"selected"``)` `{`
        `var` `children` `=` `liElements``[``i``].``childNodes``;`
        `for` `(``var` `j` `=` `0``;` `j` `<` `children``.``length``;` `j``++``)` `{`
            `var` `child` `=` `children``[``j``];`
            `if` `(``child``.``nodeType` `===` `Node``.``ELEMENT_NODE` `&&` `child``.``tagName` `===` `"P"``)` `{`
                `child``.``setAttribute``(``"style"``,` `"background-color: blue"``);`
            `}`
        `}`
    `}`
`}`
``` 
This JavaScript imperatively sets the element Sharks to have a blue background, but the code is
awful. Not only is it much longer and harder to understand than the CSS and XSL equivalents, but it
also has some serious problems: