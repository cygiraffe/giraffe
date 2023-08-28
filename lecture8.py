import re
#p = re.compile('[a-z]+')
#m = p.match('python')
#print(m)

#p = re.compile('[a-z]+')
#m = p.search('3 python')
#print(m)

p = re.compile('[a-z]+')
m = p.findall('life is too short')
print(m)

a=re.compile('[a-z]', re.IGNORECASE)
print(a.match('python'))
print(a.match('Python'))
print(a.match('PYTHON'))