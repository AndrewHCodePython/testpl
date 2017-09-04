import re

string = "People » Scott Zoltok » View | Toronto Ultimate Club"
print(string)
out = re.search('\u00BB\s{1}(.+?)\s{1}\u00BB', string, re.UNICODE).group(1)
print (out)