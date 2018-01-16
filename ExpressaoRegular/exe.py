import re #biblioteca de expressão regular

'''str = 'jailson é abencoado por Deus'
match = re.search(r'por\s\w\w\w\w',str)
if match:
    print("Abençoado",match.group())
else:
    print("did not find")
'''

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(),match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
result = displaymatch(valid.match("akt5q"))
print(result)
