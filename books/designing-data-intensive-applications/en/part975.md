The click may never come if the user abandons their search, and even if it comes, the time between
the search and the click may be highly variable: in many cases it might be a few seconds, but it
could be as long as days or weeks (if a user runs a search, forgets about that browser tab, and then
returns to the tab and clicks a result sometime later). Due to variable network delays, the click
event may even arrive before the search event. You can choose a suitable window for the join—for
example, you may choose to join a click with a search if they occur at most one hour apart. Note that embedding the details of the search in the click event is not equivalent to joining the
events: doing so would only tell you about the cases where the user clicked a search result, not
about the searches where the user did not click any of the results. In order to measure search
quality, you need accurate click-through rates, for which you need both the search events and the
click events.