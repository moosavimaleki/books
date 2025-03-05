[![6](assets/6.png)](#co_batch_processing_CO1-6)  Finally, head outputs just the first five lines (-n 5) of input,
and discards the rest. The output of that series of commands looks something like this: ```
4189 /favicon.ico
3631 /2013/05/24/improving-security-of-ssh-private-keys.html
2124 /2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html
1369 /
 915 /css/typography.css
``` Although the preceding command line likely looks a bit obscure if you’re unfamiliar with Unix tools,
it is incredibly powerful. It will process gigabytes of log files in a matter of seconds, and you
can easily modify the analysis to suit your needs. For example, if you want to omit CSS files from
the report, change the awk argument to '$7 !~ /\.css$/ {print $7}'. If you want to count top
client IP addresses instead of top pages, change the awk argument to '{print $1}'. And so on. 
We don’t have space in this book to explore Unix tools in detail, but they are very much worth
learning about. Surprisingly many data analyses can be done in a few minutes using some combination
of awk, sed, grep, sort, uniq, and xargs, and they perform surprisingly well
[[8](ch10.html#Drake2014vm)].