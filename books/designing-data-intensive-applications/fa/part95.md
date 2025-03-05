تفاوت بین رویکردها به ویژه در مواردی که یک برنامه می‌خواهد فرمت داده‌های خود را تغییر دهد، قابل توجه است. به عنوان مثال، فرض کنید در حال حاضر نام کامل هر کاربر را در یک فیلد ذخیره می‌کنید، و به جای آن می‌خواهید نام و نام خانوادگی را جداگانه ذخیره کنید [[23](ch02.html#Irwin2013tb)].

در یک پایگاه داده سندی، شما فقط شروع به نوشتن اسناد جدید با فیلدهای جدید می‌کنید و کدی در برنامه دارید که مواردی را که اسناد قدیمی خوانده می‌شوند، مدیریت می‌کند. به عنوان مثال:
```
if (user && user.name && !user.first_name) {
    // Documents written before Dec 8, 2013 don't have first_name
    user.first_name = user.name.split(" ")[0];
}
```

از طرف دیگر، در یک طرح پایگاه داده "با نوع ایستا"، شما معمولاً یک مهاجرت به شرح زیر انجام می‌دهید:
```
ALTER TABLE users ADD COLUMN first_name text;
UPDATE users SET first_name = split_part(name, ' ', 1);      -- PostgreSQL
UPDATE users SET first_name = substring_index(name, ' ', 1);      -- MySQL
```% 