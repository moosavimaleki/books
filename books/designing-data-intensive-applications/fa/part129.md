### مدل داده RDF

زبان Turtle که در [مثال 2-7](#fig_graph_n3_shorthand) استفاده کردیم، یک قالب قابل خواندن توسط انسان برای داده‌های RDF است. گاهی اوقات RDF همچنین در یک قالب XML نوشته می‌شود، که همان کار را با پرگویی بسیار بیشتری انجام می‌دهد—به [مثال 2-8](#fig_graph_rdf_xml) نگاه کنید. Turtle/N3 ترجیح داده می‌شود زیرا برای چشم‌ها بسیار راحت‌تر است، و ابزارهایی مانند Apache Jena [[42](ch02.html#Jena2013)] می‌توانند در صورت لزوم به طور خودکار بین قالب‌های مختلف RDF تبدیل کنند.

##### مثال 2-8. داده‌های [مثال 2-7](#fig_graph_n3_shorthand)، بیان شده با استفاده از نحو RDF/XML

```
<rdf:RDF xmlns="http://example.org/profiles/"
         xmlns:foaf="http://xmlns.com/foaf/0.1/"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

  <Location rdf:about="http://example.org/people/idaho">
    <name>Idaho</name>
    <type>state</type>
    <within>
      <Location rdf:about="http://example.org/people/usa">
        <name>United States</name>
        <type>country</type>
        <within>
          <Location rdf:about="http://example.org/people/namerica">
            <name>North America</name>
            <type>continent</type>
          </Location>
        </within>
      </Location>
    </within>
  </Location>

  <Person rdf:about="http://example.org/people/lucy">
    <name>Lucy</name>
    <bornIn rdf:resource="http://example.org/people/idaho"/>
  </Person>
</rdf:RDF>
```

RDF به دلیل اینکه برای تبادل داده در سراسر اینترنت طراحی شده است، چند ویژگی عجیب دارد. موضوع، گزاره و شیء یک سه‌تایی اغلب URIها هستند. به عنوان مثال، یک گزاره ممکن است یک URI مانند `http://my-company.com/namespace#within` یا `http://my-company.com/namespace#lives_in` باشد، به جای فقط WITHIN یا LIVES_IN. منطق پشت این طراحی این است که شما باید بتوانید داده‌های خود را با داده‌های شخص دیگری ترکیب کنید، و اگر آن‌ها معنای متفاوتی به کلمه within یا lives_in نسبت دهند، تعارضی ایجاد نمی‌شود زیرا گزاره‌های آن‌ها در واقع `http://other.org/foo#within` و `http://other.org/foo#lives_in` هستند. 