```
`cat`` ``/var/log/nginx/access.log`` ``|`` `[![1](assets/1.png)](#callout_batch_processing_CO1-1)`
  ``awk`` ``'{print $7}'`` ``|`` `[![2](assets/2.png)](#callout_batch_processing_CO1-2)`
  ``sort``             ``|`` `[![3](assets/3.png)](#callout_batch_processing_CO1-3)`
  ``uniq`` ``-c``          ``|`` `[![4](assets/4.png)](#callout_batch_processing_CO1-4)`
  ``sort`` ``-r`` ``-n``       ``|`` `[![5](assets/5.png)](#callout_batch_processing_CO1-5)`
  ``head`` ``-n`` ``5``          `[![6](assets/6.png)](#callout_batch_processing_CO1-6)
``` [![1](assets/1.png)](#co_batch_processing_CO1-1) Read the log file. [![2](assets/2.png)](#co_batch_processing_CO1-2) Split each line into fields by whitespace, and output only the seventh such field from each
line, which happens to be the requested URL. In our example line, this request URL is
/css/typography.css. [![3](assets/3.png)](#co_batch_processing_CO1-3)  Alphabetically sort the list of requested URLs. If some URL has been
requested n times, then after sorting, the file contains the same URL repeated n times in a row. [![4](assets/4.png)](#co_batch_processing_CO1-4)  The uniq command filters out repeated lines in its input by checking
whether two adjacent lines are the same. The -c option tells it to also output a counter: for
every distinct URL, it reports how many times that URL appeared in the input. [![5](assets/5.png)](#co_batch_processing_CO1-5) The second sort sorts by the number (-n) at the start of each line, which is the number of
times the URL was requested. It then returns the results in reverse
(-r) order, i.e. with the largest number
first.