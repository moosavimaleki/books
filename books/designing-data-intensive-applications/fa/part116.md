CREATE TABLE vertices (
    vertex_id   integer PRIMARY KEY,
    properties  json
);

CREATE TABLE edges (
    edge_id     integer PRIMARY KEY,
    tail_vertex integer REFERENCES vertices (vertex_id),
    head_vertex integer REFERENCES vertices (vertex_id),
    label       text,
    properties  json
);

CREATE INDEX edges_tails ON edges (tail_vertex);
CREATE INDEX edges_heads ON edges (head_vertex);
```

برخی از جنبه‌های مهم این مدل عبارتند از:

1. هر رأس می‌تواند یک یال داشته باشد که آن را به هر رأس دیگری متصل می‌کند. هیچ طرحی وجود ندارد که محدود کند چه نوع چیزهایی می‌توانند یا نمی‌توانند با هم مرتبط باشند.

2. با داشتن هر رأس، می‌توانید به طور کارآمد هم یال‌های ورودی و هم یال‌های خروجی آن را پیدا کنید، و بنابراین گراف را پیمایش کنید—یعنی، یک مسیر را از طریق زنجیره‌ای از رئوس دنبال کنید—هم به جلو و هم به عقب. (به همین دلیل است که [مثال 2-2](#fig_graph_sql_schema) شاخص‌هایی روی هر دو ستون tail_vertex و head_vertex دارد.)

3. با استفاده از برچسب‌های مختلف برای انواع مختلف روابط، می‌توانید چندین نوع مختلف اطلاعات را در یک گراف واحد ذخیره کنید، در حالی که همچنان یک مدل داده تمیز را حفظ می‌کنید.% 