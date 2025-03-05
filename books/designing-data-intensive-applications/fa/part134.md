##### مثال 2-10. زیرمجموعه‌ای از داده‌های [شکل 2-5](#fig_datamodels_graph)، نمایش داده شده به عنوان حقایق Datalog

```
name(namerica, 'North America').
type(namerica, continent).

name(usa, 'United States').
type(usa, country).
within(usa, namerica).

name(idaho, 'Idaho').
type(idaho, state).
within(idaho, usa).

name(lucy, 'Lucy').
born_in(lucy, idaho).
```

حالا که داده‌ها را تعریف کرده‌ایم، می‌توانیم همان پرس‌وجوی قبلی را بنویسیم، همانطور که در [مثال 2-11](#fig_datalog_query) نشان داده شده است. کمی متفاوت از معادل آن در Cypher یا SPARQL به نظر می‌رسد، اما نگذارید این شما را دلسرد کند. Datalog زیرمجموعه‌ای از Prolog است، که ممکن است قبلاً دیده باشید اگر علوم کامپیوتر خوانده باشید.

##### مثال 2-11. همان پرس‌وجوی [مثال 2-4](#fig_cypher_query)، بیان شده در Datalog

```
within_recursive(Location, Name) :- name(Location, Name).     /* Rule 1 */

within_recursive(Location, Name) :- within(Location, Via),    /* Rule 2 */
                                    within_recursive(Via, Name).

migrated(Name, BornIn, LivingIn) :- name(Person, Name),       /* Rule 3 */
                                    born_in(Person, BornLoc),
                                    within_recursive(BornLoc, BornIn),
                                    lives_in(Person, LivingLoc),
                                    within_recursive(LivingLoc, LivingIn).

?- migrated(Who, 'United States', 'Europe').
/* Who = 'Lucy'. */
``` 