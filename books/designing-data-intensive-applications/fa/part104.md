    <li class="selected">
        <p>Sharks</p>
        <ul>
            <li>Great White Shark</li>
            <li>Tiger Shark</li>
            <li>Hammerhead Shark</li>
        </ul>
    </li>
    <li>
        <p>Whales</p>
        <ul>
            <li>Blue Whale</li>
            <li>Humpback Whale</li>
            <li>Fin Whale</li>
        </ul>
    </li>

[![1](assets/1.png)](#co_data_models_and_query_languages_CO1-1) آیتم انتخاب شده با کلاس CSS "selected" علامت‌گذاری شده است.
[![2](assets/2.png)](#co_data_models_and_query_languages_CO1-2) Sharks عنوان صفحه انتخاب شده فعلی است.

حالا فرض کنید می‌خواهید عنوان صفحه انتخاب شده فعلی پس‌زمینه آبی داشته باشد، تا به صورت بصری برجسته شود. این کار با استفاده از CSS آسان است:
```
li.selected > p {
    background-color: blue;
}
```

در اینجا انتخابگر CSS با عبارت `li.selected > p` الگوی عناصری را اعلام می‌کند که می‌خواهیم سبک آبی را به آنها اعمال کنیم: یعنی، تمام عناصر `<p>` که والد مستقیم آنها یک عنصر `<li>` با کلاس CSS از نوع `selected` است. عنصر Sharks در مثال با این الگو مطابقت دارد، اما Whales مطابقت ندارد زیرا والد `<li>` آن فاقد `class="selected"` است.

اگر به جای CSS از XSL استفاده می‌کردید، می‌توانستید کار مشابهی انجام دهید:% 