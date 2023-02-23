import re

test_string = """
ct
cat
caat
caat
caaat
cacat
cacacat
"""
test_string2 = """
\etc
\\abc
\\\def 
"""
p = re.compile(r'\\..')
q = p.finditer(test_string2)
print(test_string2)
for i in q:
    print(i)