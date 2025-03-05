```
```
    ```` `[![1](assets/1.png)](#callout_data_models_and_query_languages_CO1-1)`
        ````Sharks```` `[![2](assets/2.png)](#callout_data_models_and_query_languages_CO1-2)`
        ````
            ````Great White Shark````
            ````Tiger Shark````
            ````Hammerhead Shark````
        ````
    ````
    ````
        ````Whales````
        ````
            ````Blue Whale````
            ````Humpback Whale````
            ````Fin Whale````
        ````
    ````
```
``` [![1](assets/1.png)](#co_data_models_and_query_languages_CO1-1) The selected item is marked with the CSS class "selected". [![2](assets/2.png)](#co_data_models_and_query_languages_CO1-2) Sharks is the title of the currently selected page. 
Now say you want the title of the currently selected page to have a blue background, so that it is
visually highlighted. This is easy, using CSS: ```
`li``.selected` `>` `p` `{`
    `background-color``:` `blue``;`
`}`
``` Here the CSS selector li.selected > p declares the pattern of elements to which we want to apply
the blue style: namely, all  elements whose direct parent is an  element with a CSS class
of selected. The element Sharks in the example matches this pattern, but Whales
does not match because its  parent lacks class="selected". 
If you were using XSL instead of CSS, you could do something similar: