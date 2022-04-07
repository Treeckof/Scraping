d = {'a' : 1, 'b' : 2}
try:
   print(d['x'])

except KeyError:
   print('x is not found')
print('x가 없데요. 처리해주세요.')

f = open('index.html')
print(f.read())



with open('index.html') as f:
   print(f.read())

while True:
   print('1')