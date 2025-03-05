### Transparency and experimentation Part of what makes Unix tools so successful is that they make it quite easy to see what is going on: *  
The input files to Unix commands are normally treated as immutable. This means you can run the
commands as often as you want, trying various command-line options, without damaging the input
files. *  
You can end the pipeline at any point, pipe the output into less, and look at it to see if it
has the expected form. This ability to inspect is great for debugging. *  You can write the output of one pipeline stage to a file and use that file as input to the next
stage. This allows you to restart the later stage without rerunning the entire pipeline. Thus, even though Unix tools are quite blunt, simple tools compared to a query optimizer of a
relational database, they remain amazingly useful, especially for experimentation.