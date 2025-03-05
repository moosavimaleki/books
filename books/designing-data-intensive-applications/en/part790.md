```
$remote_addr - $remote_user [$time_local] "$request"
$status $body_bytes_sent "$http_referer" "$http_user_agent"
``` So, this one line of the log indicates that on February 27, 2015, at 17:55:11 UTC, the server
received a request for the file /css/typography.css from the client IP address 216.58.210.78. The
user was not authenticated, so $remote_user is set to a hyphen (-). The response status was 200
(i.e., the request was successful), and the response was 3,377 bytes in size. The web browser was
Chrome 40, and it loaded the file because it was referenced in the page at the URL
[http://martin.kleppmann.com/](http://martin.kleppmann.com/). ## Simple Log Analysis Various tools can take these log files and produce pretty reports about your website traffic, but
for the sake of exercise, let’s build our own, using basic Unix tools. For example, say you want to
find the five most popular pages on your website. You can do this in a Unix shell as
follows:[i](ch10.html#idm140605758638848)