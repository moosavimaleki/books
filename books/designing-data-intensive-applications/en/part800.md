
The parsing of each record (i.e., a line of input) is more vague. Unix tools commonly split a line
into fields by whitespace or tab characters, but CSV (comma-separated), pipe-separated, and other
encodings are also used. Even a fairly simple tool like xargs has half a dozen command-line
options for specifying how its input should be parsed. The uniform interface of ASCII text mostly works, but it’s not exactly beautiful: our log analysis
example used {print $7} to extract the URL, which is not very readable. In an ideal world this
could have perhaps been {print $request_url} or something of that sort. We will return to this
idea later. Although it’s not perfect, even decades later, the uniform interface of Unix is still something
remarkable. Not many pieces of software interoperate and compose as well as Unix tools do: you can’t
easily pipe the contents of your email account and your online shopping history through a custom
analysis tool into a spreadsheet and post the results to a social network or a wiki. Today it’s an
exception, not the norm, to have programs that work together as smoothly as Unix tools do.