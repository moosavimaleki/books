<xsl:template match="li[@class='selected']/p">
    <p style="background-color: blue">
        <xsl:apply-templates/>
    </p>
</xsl:template>

در اینجا، عبارت XPath با `li[@class='selected']/p` معادل انتخابگر CSS با `li.selected > p` در مثال قبلی است. آنچه CSS و XSL مشترک دارند این است که هر دو زبان‌های اعلانی برای مشخص کردن سبک‌دهی یک سند هستند.

تصور کنید اگر مجبور بودید از یک رویکرد دستوری استفاده کنید، زندگی چگونه می‌بود. در جاوااسکریپت، با استفاده از API اصلی مدل شیء سند (DOM)، نتیجه ممکن است چیزی شبیه به این باشد:
```
var liElements = document.getElementsByTagName("li");
for (var i = 0; i < liElements.length; i++) {
    if (liElements[i].className === "selected") {
        var children = liElements[i].childNodes;
        for (var j = 0; j < children.length; j++) {
            var child = children[j];
            if (child.nodeType === Node.ELEMENT_NODE && child.tagName === "P") {
                child.setAttribute("style", "background-color: blue");
            }
        }
    }
}
```

این جاوااسکریپت به صورت دستوری عنصر Sharks را تنظیم می‌کند تا پس‌زمینه آبی داشته باشد، اما کد وحشتناک است. نه تنها بسیار طولانی‌تر و درک آن سخت‌تر از معادل‌های CSS و XSL است، بلکه همچنین برخی مشکلات جدی دارد:% 