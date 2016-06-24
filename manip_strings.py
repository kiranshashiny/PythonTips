import re
import json

#  Here I am inserting the string with double quotes.
#  \1 is what I am looking for in the re.sub()
#  import re at the beginning of the file.

line="hello world"
print "Printing raw string"

print line

print " Printing the string after inserting double-quotes beginning and ending of string"

line = re.sub(r'(.*)', r'"\1"', line.rstrip())
print(line)
